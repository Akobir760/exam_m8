from rest_framework import serializers
from configapp.models.teach_models import * 
from configapp.models import AccountModel

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class TeacherSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"  


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class SuperUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ["username", "password", "email", "full_name"]

    def create(self, validated_data):
        user = AccountModel.objects.create_superuser(**validated_data)
        return user
    

class AddStudenttoGroupSerializer(serializers.Serializer):
    student_id = serializers.CharField()
