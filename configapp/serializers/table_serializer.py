from rest_framework import serializers
from configapp.models.tables import *

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableTypeModel
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableModel
        fields = "__all__"