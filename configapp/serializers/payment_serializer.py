from configapp.models.payment import Payment, PaymentType
from rest_framework import serializers

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields  = '__all__'


class PaymentSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"