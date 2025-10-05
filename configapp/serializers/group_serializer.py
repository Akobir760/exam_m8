from rest_framework import serializers
from configapp.models.group_models import *

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"


class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"