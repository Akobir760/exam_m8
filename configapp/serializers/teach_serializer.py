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
    


class ExamSerializer(serializers.ModelSerializer):
    passed_students = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all()
    )
    failed_students = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all()
    )

    class Meta:
        model = Exam
        fields = [
            'id', 'title', 'date', 'group', 'teacher', 'passed_students', 'failed_students'
        ]

class ExamIdSerializer(serializers.Serializer):
    exam_id = serializers.IntegerField()


class Activefilterserializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()