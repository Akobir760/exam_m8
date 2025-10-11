from rest_framework.views import APIView
from configapp.serializers.attendance_serializer import *
from rest_framework.views import Response, status
from drf_yasg.utils import swagger_auto_schema
from configapp.models.permmissions import *


class AttendanceRetrieveAPiView(APIView):
    permission_classes = [IsManagerOrAdmin]
    def get(self, request, pk):
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
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AttendanceUpdateAPIView(APIView):
    permission_classes = [IsManagerOrAdmin]
    def put(self, request, pk):
        try:
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
    def post(self, request, pk):
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
    def get(self, request, pk):
        if pk:
            try:
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
    def post(self, request, pk):
        attendance_level = AttendanceLevel.objects.get(pk=pk)

        if attendance_level:
            attendance_level.delete()
            return Response({"message":"davomat statusi o'chirildi!"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"message":"Davomat statusi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)


class AttendanceLevelUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]
    def put(self, request, pk):
        attendance_level = AttendanceLevel.objects.get()
        if attendance_level:
            serializer = AttendaceLevelSerializer(instance=attendance_level, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"message":"Davomat statusi topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        


