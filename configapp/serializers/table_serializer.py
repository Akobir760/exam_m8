from rest_framework import serializers
from configapp.models.tables import *

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"