from rest_framework import serializers
from django.contrib.auth import authenticate
from configapp.models import AccountModel
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from random import randint
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountModel
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        if not user.is_active:
            raise serializers.ValidationError("User is not active")
        data["user"] = user
        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)



class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is not registered.")
        return value

    def create_otp(self, email):
        otp = str(randint(100000, 999999))
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()
        send_mail(
            "Password Reset Code",
            f"Your password reset code is: {otp}",
            "no-reply@example.com",
            [email],
            fail_silently=True,
        )
        return otp


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get("email")
        otp = attrs.get("otp")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        if user.otp != otp:
            raise serializers.ValidationError("Invalid OTP code.")

        return attrs


class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)
    re_new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["re_new_password"]:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def save(self):
        email = self.validated_data["email"]
        password = self.validated_data["new_password"]

        user = User.objects.get(email=email)
        user.set_password(password)
        user.otp = None  
        user.save()
        return user
    
    
class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True, min_length=6)


