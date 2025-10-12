from drf_yasg import openapi
from rest_framework.views import APIView
from configapp.serializers.attendance_serializer import *
from rest_framework.views import Response, status
from drf_yasg.utils import swagger_auto_schema
from configapp.models.permmissions import *
from django.utils.dateparse import parse_datetime


class AttendanceRetrieveAPiView(APIView):
    permission_classes = [IsManagerOrAdmin]
    def get(self, request, pk=None):
        if pk:
            try:
                attendance = Attendance.objects.get(pk=pk)
            except Attendance.DoesNotExist:
                return Response(
                    {"detail": "Davomat topilmadi."},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = AttendanceSerializer(attendance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            attendances = Attendance.objects.all()
            serializer = AttendanceSerializer(attendances, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class AttendaceCreateAPIView(APIView):
    permission_classes = [IsManagerOrAdmin]
    @swagger_auto_schema(request_body=AttendanceSerializer)
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendance = serializer.save()
        return Response(AttendanceSerializer(attendance).data, status=201)

    

class AttendanceUpdateAPIView(APIView):
    permission_classes = [IsManagerOrAdmin]
    @swagger_auto_schema(request_body=AttendanceSerializer)
    def put(self, request, pk):
        try:
            print(request.data)
            attendance = Attendance.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = AttendanceSerializer(instance = attendance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AttendanceDeleteAPIView(APIView):
    permission_classes = [IsManagerOrAdmin]
    def delete(self, request, pk):
        attendance = Attendance.objects.get(pk=pk)
        if attendance:
            attendance.delete()
            return Response({"message":"davomat o'chirildi!"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"message":"davomat topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    


class AttendanceLevelAPIView(APIView):
    permission_classes = [IsManagerOrAdmin]
    @swagger_auto_schema(request_body=AttendaceLevelSerializer)
    def post(self, request):
        serializer = AttendaceLevelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AttendanceLevelGetAPIView(APIView):
    permission_classes = [IsManagerOrAdmin]
    def get(self, request, pk=None):
        if pk:
            try:
                print(request.data)
                attendance_level = AttendanceLevel.objects.get(pk=pk)

            except:
                return Response(status==status.HTTP_404_NOT_FOUND)
            
            serializer = AttendaceLevelSerializer(attendance_level)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        attendance_levels = AttendanceLevel.objects.all()
        serializer = AttendaceLevelSerializer(attendance_levels, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class AttendanceLevelDeleteAPI(APIView):
    permission_classes = [IsManagerOrAdmin]
    def delete(self, request, pk):
        attendance_level = AttendanceLevel.objects.get(pk=pk)

        if attendance_level:
            attendance_level.delete()
            return Response({"message":"davomat statusi o'chirildi!"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"message":"Davomat statusi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)


class AttendanceLevelUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]
    @swagger_auto_schema(request_body=AttendaceLevelSerializer)
    def put(self, request, pk):
        print(request.data)
        attendance_level = AttendanceLevel.objects.get(pk=pk)
        if attendance_level:
            serializer = AttendaceLevelSerializer(instance=attendance_level, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"message":"Davomat statusi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        


class AttendanceFilterView(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'start_date': openapi.Schema(type=openapi.TYPE_STRING, format='date-time', description="Boshlanish sanasi"),
                'end_date': openapi.Schema(type=openapi.TYPE_STRING, format='date-time', description="Tugash sanasi"),
            },
            required=['start_date', 'end_date']
        ),
        responses={200: AttendanceSerializer(many=True)}
    )
    def post(self, request):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        if not start_date or not end_date:
            return Response({'error': 'Ikkala sana ham yuborilishi kerak!'}, status=status.HTTP_400_BAD_REQUEST)

        attendances = Attendance.objects.filter(created__range=[start_date, end_date])
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
