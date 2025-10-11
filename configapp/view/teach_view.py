from configapp.serializers.teach_serializer import *
from configapp.serializers.group_serializer import GroupSerializer
from configapp.serializers.attendance_serializer import *
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import Response
from rest_framework import status
from collections import defaultdict


class TeacherApiView(APIView):
    def get(self, request, pk):
        if pk:
            try:
                teacher = Teacher.objects.get(pk=pk)
            except Teacher.DoesNotExist:
                return Response(
                    {"detail": "Teacher not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = TeacherSeriallizer(teacher)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            teachers = Teacher.objects.all()
            serializer = TeacherSeriallizer(teachers, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        

class TeacherCreateAPI(APIView):
    @swagger_auto_schema(request_body=TeacherSeriallizer)
    def post(self, request):
        serializer = TeacherSeriallizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateTeacherAPI(APIView):
    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeacherSeriallizer(instance = teacher, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class GetTeachersByIdsAPIView(APIView):
    def post(self, request):
        ids = request.data.get("ids", [])
        
        if not ids or not isinstance(ids, list):
            return Response(
                {"detail": "IDs ro'yxatini to'g'ri yuboring. Masalan: {'ids': [1, 2, 3]}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        teacher = Teacher.objects.filter(id__in=ids)
        serializer = TeacherSeriallizer(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TeacherGroupsAPIView(APIView):
    def get(self, request, student_id):
        try:
            teacher = Teacher.objects.get(id=student_id)
        except Teacher.DoesNotExist:
            return Response(
                {"detail": "Bunday o'qituvchi topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        groups = teacher.group.all()  
        serializer = GroupSerializer(groups, many=True)
        return Response({
            "student": teacher.user.username,
            "groups": serializer.data
        }, status=status.HTTP_200_OK)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from configapp.models.teach_models import Teacher
from configapp.models.group_models import Group
from configapp.serializers.group_serializer import GroupSerializer
from rest_framework.permissions  import IsAdminUser

class TeacherGroupDetailView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, teacher_id, group_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response(
                {"error": "Teacher not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            group = Group.objects.get(id=group_id, teacher=teacher)
        except Group.DoesNotExist:
            return Response(
                {"error": "Group not found or does not belong to this teacher"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = GroupSerializer(group)
        return Response(serializer.data, status=status.HTTP_200_OK)

    


class TeacherAttendanceByMonthAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, student_id):
        try:
            teacher = Teacher.objects.get(id=student_id)
        except Teacher.DoesNotExist:
            return Response(
                {"detail": "Bunday o'qituvchi topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        attendances = Attendance.objects.filter(student=teacher).order_by("created")
        serializer = AttendanceSerializer(attendances, many=True)

        grouped_data = defaultdict(list)
        for att in serializer.data:
            month_key = att["created"][:7]  
            grouped_data[month_key].append(att)

        return Response({
            "student": teacher.user.full_name if hasattr(teacher.user, 'full_name') else str(teacher.user),
            "attendance_by_month": grouped_data
        }, status=status.HTTP_200_OK)


    

class StudentAPIView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentAPIView(APIView):
#     @swagger_auto_schema(request_body=StudentSerializer)
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentsListAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk):
        if pk:
            try:
                student = Student.objects.get(pk=pk)
            except Student.DoesNotExist:
                return Response(
                    {"detail": "Student not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:

            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
class UpdateStudentApi(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(request_body=StudentSerializer)
    def put(self, request, pk):
        try:
            user = Student.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class UsersListAPIVIew(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        teachers = Teacher.objects.all()
        students = Student.objects.all()

        teacher_serializer = TeacherSeriallizer(teachers, many=True)
        student_serializer = StudentSerializer(students, many=True)

        data = {
            "teachers": teacher_serializer.data,
            "students": student_serializer.data
        }

        return Response(data=data, status=status.HTTP_200_OK)
    

class SuperUserAPIView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(request_body=SuperUserCreateSerializer)
    def post(self, request):
        serializer = SuperUserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteUserAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        user = AccountModel.objects.get(pk=pk)
        if user:
            user.delete()
            return Response({"message":"User o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"User topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        

class GetStudentsByIdsAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        ids = request.data.get("ids", [])
        
        if not ids or not isinstance(ids, list):
            return Response(
                {"detail": "IDs ro'yxatini to'g'ri yuboring. Masalan: {'ids': [1, 2, 3]}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        students = Student.objects.filter(id__in=ids)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class StudentGroupsAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response(
                {"detail": "Bunday student topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        groups = student.group.all()  
        serializer = GroupSerializer(groups, many=True)
        return Response({
            "student": student.user.username,
            "groups": serializer.data
        }, status=status.HTTP_200_OK)
    


class StudentAttendanceByMonthAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response(
                {"detail": "Bunday student topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        attendances = Attendance.objects.filter(student=student).order_by("created")
        serializer = AttendanceSerializer(attendances, many=True)

        grouped_data = defaultdict(list)
        for att in serializer.data:
            month_key = att["created"][:7]  
            grouped_data[month_key].append(att)

        return Response({
            "student": student.user.username ,
            "attendance_by_month": grouped_data
        }, status=status.HTTP_200_OK)
