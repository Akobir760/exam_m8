from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login, logout
from configapp.serializers.auth_user_serializer import LoginSerializer, ChangePasswordSerializer
from drf_yasg.utils import swagger_auto_schema


class LoginView(APIView):
    permission_classes = [AllowAny]

    swagger_auto_schema(request_body=LoginSerializer)
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
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "full_name": request.user.full_name,
            "email": request.user.email,
        })


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

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
