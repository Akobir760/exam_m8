from rest_framework import status
from rest_framework.views import APIView, Response
from configapp.serializers.table_serializer import *
from configapp.models.permmissions import *
from drf_yasg.utils import swagger_auto_schema

class TableListAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request, pk):
        if pk:
            try:
                table = TableModel.objects.get(pk=pk)
            except TableModel.DoesNotExist:
                return Response({"message":"Jadval topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = TableSerializer(table)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        tables = TableModel.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class TableCreateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=TableSerializer)
    def post(self, request):

        serializer = TableSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TableDelAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def delete(self, request, pk):
        try:
            table = TableModel.objects.get(pk=pk)
        except TableModel.DoesNotExist:
            return Response({"message":"Jadval topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        table.delete()
        return Response({"message":"Jadval o'chirildi!"})
    

class TableUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def put(self, request, pk):
        try:
            table = TableModel.objects.get(pk=pk)
        except TableModel.DoesNotExist:
            return Response({"message":"Jadval  topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TableSerializer(instance=table, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TableTypeListAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request, pk):
        if pk:
            try:
                table_type = TableTypeModel.objects.get(pk=pk)
            except TableTypeModel.DoesNotExist:
                return Response({"message":"Table type topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = TableTypeSerializer(table_type)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        table_types = TableTypeModel.objects.all()
        serializer = TableTypeSerializer(table_types, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class TableTypeCreateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=TableTypeSerializer)
    def post(self, request):
        serializer = TableTypeSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TableTypeDelAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def delete(self, request, pk):
        try:
            table_type = TableTypeModel.objects.get(pk=pk)
        except TableTypeModel.DoesNotExist:
            return Response({"message":"Jadval turi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        table_type.delete()
        return Response({"message":"Jadval turi o'chirildi"})

class TableTypeUpdate(APIView):
    permission_classes = [IsManagerOrAdmin]

    def put(self, request, pk):
        try:
            table_type = TableTypeModel.objects.get(pk=pk)
        except TableTypeModel.DoesNotExist:
            return Response({"message":"Jadval turi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TableTypeSerializer(instance = table_type, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        

