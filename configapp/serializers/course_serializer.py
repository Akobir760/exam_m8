from rest_framework import serializers
from configapp.models.teach_models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"