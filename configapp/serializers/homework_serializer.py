from rest_framework import serializers
from configapp.models.homework import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = "__all__"


class HomeworkReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkReview
        fields = "__all__"