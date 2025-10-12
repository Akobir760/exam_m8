from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from configapp.models import AccountModel
from configapp.serializers.auth_user_serializer import *
import random
from django.core.mail import send_mail


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        role = serializer.validated_data["role"]

        if isinstance(user, AccountModel):
            login(request, user)

        refresh = RefreshToken.for_user(user if isinstance(user, AccountModel) else AccountModel.objects.first())

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "role": role,
            "username": user.username,
        })


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Tizimdan chiqildi"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        
        return Response({
            "id": user.id,
            "username": user.username,
            "is_staff": getattr(user, "is_staff", False),
            "is_manager": getattr(user, "is_manager", False),
        })


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old = serializer.validated_data["old_password"]
        new = serializer.validated_data["new_password"]

        user = request.user
        print(user)
        if not user.check_password(old):
            return Response({"error": "Eski parol noto'g'ri"}, status=400)
        user.set_password(new)
        user.save()
        return Response({"detail": "Parol o'zgartirildi"})




class ResetPasswordView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def post(self, request):
        email = request.data.get("email")
        print(email)
        if not email:
            return Response({"error": "Email kiritilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        user_type = None

        if AccountModel.objects.filter(email=email).exists():
            user = AccountModel.objects.get(email=email)
            user_type = "account"
        elif Teacher.objects.filter(email=email).exists():
            user = Teacher.objects.get(email=email)
            user_type = "teacher"
        elif Student.objects.filter(email=email).exists():
            user = Student.objects.get(email=email)
            user_type = "student"
        else:
            return Response({"error": "Email topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        otp = str(random.randint(100000, 999999))
        user.otp = otp  
        user.save()
    
        try:
            send_mail(
                subject="Parolni tiklash uchun OTP kodi",
                message=f"Sizning OTP kodingiz: {otp}\n\nIltimos, ushbu kodni 5 daqiqa ichida kiriting.",
                from_email=None,  # DEFAULT_FROM_EMAIL ishlatiladi
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception as e:
            return Response({"error": f"Email yuborishda xatolik: {str(e)}"}, status=500)

        return Response({
            "detail": f"OTP {user_type} uchun yuborildi. Iltimos, emailingizni tekshiring."
        }, status=200)



class VerifyOTPView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=VerifyOTPSerializer)
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        try:
            if AccountModel.objects.filter(email=email).exists():
                user = AccountModel.objects.get(email=email)
                user_type = "account"
            elif Teacher.objects.filter(email=email).exists():
                user = Teacher.objects.get(email=email)
                user_type = "teacher"
            elif Student.objects.filter(email=email).exists():
                user = Student.objects.get(email=email)
                user_type = "student"
            # else:
            #     return Response({"error": "Email topilmadi"}, status=status.HTTP_404_NOT_FOUND)            
            if user.otp == otp:
                return Response({"detail": "OTP tasdiqlandi"})
            return Response({"error": "OTP noto'g'ri"}, status=400)
        except AccountModel.DoesNotExist:
            return Response({"error": "Email topilmadi"}, status=404)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from configapp.models import AccountModel, Teacher, Student
from configapp.serializers.auth_user_serializer import SetNewPasswordSerializer


class SetNewPasswordView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=SetNewPasswordSerializer)
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        new_password = request.data.get("new_password")

        user = None
        user_type = None

        if AccountModel.objects.filter(email=email).exists():
            user = AccountModel.objects.get(email=email)
            user_type = "account"
        elif Teacher.objects.filter(email=email).exists():
            user = Teacher.objects.get(email=email)
            user_type = "teacher"
        elif Student.objects.filter(email=email).exists():
            user = Student.objects.get(email=email)
            user_type = "student"
        else:
            return Response({"error": "Email topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        if hasattr(user, "otp") and user.otp != otp:
            return Response({"error": "OTP noto'g'ri"}, status=status.HTTP_400_BAD_REQUEST)

        if hasattr(user, "set_password"):
            user.set_password(new_password)
        else:
            if hasattr(user, "password"):
                user.password = make_password(new_password)
            elif hasattr(user, "passwords"):
                user.passwords = make_password(new_password)
            else:
                return Response({"error": "Parol maydoni topilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        if hasattr(user, "otp"):
            user.otp = None

        user.save()

        return Response({
            "detail": "Yangi parol o‘rnatildi",
            "user_type": user_type
        }, status=status.HTTP_200_OK)

