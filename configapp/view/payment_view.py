from configapp.serializers.payment_serializer import *
from rest_framework.views import APIView, Response, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser

class PaymentTypeCreateAPI(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(request_body=PaymentTypeSerializer)
    def post(self, request):
        serializer = PaymentTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaymentTypeListAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk=None):
        if pk:
            try:
                payment_type = PaymentType.objects.get(pk=pk)
            except PaymentType.DoesNotExist:
                return Response({"message":"Payment type topilmadi!"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = PaymentTypeSerializer(payment_type)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        payment_types = PaymentType.objects.all()
        serializer = PaymentTypeSerializer(payment_types, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class PaymentTypeDelAPI(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        try:
            payment_type = PaymentType.objects.get(pk=pk)
        except PaymentType.DoesNotExist:
            return Response({"message":"Payment type topilmadi!"}, status=status.HTTP_400_BAD_REQUEST)
        
        payment_type.delete()
        return Response({"message":"Payment type o'chirildi!"}, status=status.HTTP_200_OK)
    

class PaymentTypeUpdateAPI(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        try:
            payment_type = PaymentType.objects.get(pk=pk)
        except PaymentType.DoesNotExist:
            return Response({"message":"Payment type topilmadi!"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PaymentTypeSerializer(instance=payment_type, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PaymentCteateAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=PaymentSeriaizer)
    def post(self, request):
        serializer = PaymentSeriaizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PaymnetListAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            try:
                payment = Payment.objects.get(pk=pk)
            except Payment.DoesNotExist:
                return Response({"message":"Payment topilmadi!"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = PaymentSeriaizer(payment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        payments = Payment.objects.all()
        serializer = PaymentSeriaizer(payments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        


class PaymentDelAPI(APIView):
    permission_classes = [IsAdminUser]
    def delete(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({"message":"Payment topilmadi!"}, status=status.HTTP_400_BAD_REQUEST)

        payment.delete()

        return Response({"message":"payment o'chirildi!"}, status=status.HTTP_200_OK)
    

class PaymentUpdateAPI(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return Response({"message":"Payment topilmadi!"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PaymentSeriaizer(instance=payment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)