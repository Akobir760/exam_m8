from rest_framework import serializers
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.exceptions import AuthenticationFailed
from configapp.models import AccountModel, Student, Teacher


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = None
        role = None

        try:
            acc = AccountModel.objects.get(username=username)
            if acc.check_password(password):
                user = acc
                role = "account"
        except AccountModel.DoesNotExist:
            pass

        if not user:
            try:
                stu = Student.objects.get(username=username)
                if str(stu.passwords) == str(password): 
                    user = stu
                    role = "student"
            except Student.DoesNotExist:
                pass

        if not user:
            try:
                t = Teacher.objects.get(username=username)
                if str(t.password) == str(password):
                    user = t
                    role = "teacher"
            except Teacher.DoesNotExist:
                pass

        if not user:
            raise AuthenticationFailed("Foydalanuvchi topilmadi yoki parol noto‘g‘ri")

        attrs["user"] = user
        attrs["role"] = role
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = "__all__"
