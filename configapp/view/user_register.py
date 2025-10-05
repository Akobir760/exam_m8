import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import status
from django.contrib.auth import login, logout
from configapp.serializers.auth_user_serializer import *
from drf_yasg.utils import swagger_auto_schema
from configapp.models.auth_user import AccountModel
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer



class RegisterAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out"})


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "user_id": user.id,
            "username": user.username,
            "password": user.password,
            "full name": user.full_name,
            "email": user.email,
            "is_active": user.is_active,
            "created": user.created
        }

        return Response(data = data, status=status.HTTP_202_ACCEPTED)
    

class TokenRefreshView(TokenViewBase):
    serializer_class = TokenRefreshSerializer



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_pass = serializer.validated_data["old_password"]
        new_pass = serializer.validated_data["new_password"]

        if not request.user.check_password(old_pass):
            return Response({"error": "Old password incorrect"}, status=400)

        request.user.set_password(new_pass)
        request.user.save()
        return Response({"detail": "Password changed"})



class ResetPasswordView(APIView):

    @swagger_auto_schema(request_body=ResetPasswordRequestSerializer)
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response({"error": "Email kiritilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = AccountModel.objects.get(email=email)
        except AccountModel.DoesNotExist:
            return Response({"error": "Bunday email topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        otp = random.randint(100000, 999999)
        user.otp_code = otp
        user.save()

        send_mail(
            subject="Parolni tiklash",
            message=f"Sizning tasdiqlash kodingiz: {otp}",
            from_email="zulfiyasharopova9@gmail.com",  
            recipient_list=[email],
        )

        return Response({"message": "Tasdiqlash kodingiz emailingizga yuborildi"}, status=status.HTTP_200_OK)

class VerifyOTPView(APIView):
    @swagger_auto_schema(request_body=VerifyOTPSerializer)
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]

        try:
            user = AccountModel.objects.get(email=email)
        except AccountModel.DoesNotExist:
            return Response({"error": "Email topilmadi!"}, status=404)

        if user.otp != otp:
            return Response({"error": "Noto'g'ri kod!"}, status=400)

        return Response({"message": "Kod to'g'ri!", "status": "verified"}, status=200)


class SetNewPasswordView(APIView):
    @swagger_auto_schema(request_body=SetNewPasswordSerializer)
    def post(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        new_password = serializer.validated_data["new_password"]

        try:
            user = AccountModel.objects.get(email=email)
        except AccountModel.DoesNotExist:
            return Response({"error": "Email topilmadi!"}, status=404)

        user.set_password(new_password)
        user.otp = None 
        user.save()

        return Response({"message": "Parol muvaffaqiyatli o'zgartirildi!"}, status=200)
