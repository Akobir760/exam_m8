from rest_framework.views import APIView, Response, status
from configapp.serializers.group_serializer import *
from drf_yasg.utils import swagger_auto_schema
from configapp.models.teach_models import *
from rest_framework.permissions import IsAdminUser
from configapp.models.permmissions import *


class GroupsListAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk):
        if pk:
            try:
                group = Group.objects.get(pk=pk)
            except:
                return Response({"message":"Guruh topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = GroupSerializer(group)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class GroupCreateAPIView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(request_body=GroupSerializer)
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GroupDeleteAPI(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, pk):
        group = Group.objects.get(pk=pk)
        if group:
            group.delete()
            return Response({"message":"Guruh o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"Guruh topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
class GroupUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]
    def put(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
        except:
            return Response({"message":"Guruh topilmadi!"}, status=status.HTTP_204_NO_CONTENT)
        
        serializer = GroupSerializer(instance=group, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        


class AddStudentToGroupAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, id):  
        student_id = request.data.get("student_id")

        if not student_id:
            return Response({"detail": "student_id yuborilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(id=id)
        except Group.DoesNotExist:
            return Response({"detail": "Bunday group topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Bunday student topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        group.students.add(student)
        group.save()

        return Response({"detail": f"{student} guruhga qo'shildi"}, status=status.HTTP_200_OK)
    


class RemoveStudentFromGroupAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, id): 
        student_id = request.data.get("student_id")

        if not student_id:
            return Response({"detail": "student_id yuborilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(id=id)
        except Group.DoesNotExist:
            return Response({"detail": "Bunday group topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Bunday student topilmadi"}, status=status.HTTP_404_NOT_FOUND)

       
        if student not in group.students.all():
            return Response({"detail": "Bu talaba bu guruhda emas"}, status=status.HTTP_400_BAD_REQUEST)

        group.students.remove(student)
        group.save()

        return Response({"detail": f"{student} guruhdan chiqarildi"}, status=status.HTTP_200_OK)
    


class AddTeacherToGroupAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, id):  
        teacher_id = request.data.get("teacher_id")

        if not teacher_id:
            return Response({"detail": "teacher_id yuborilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(id=id)
        except Group.DoesNotExist:
            return Response({"detail": "Bunday group topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Bunday student topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        group.teachers.add(teacher)
        group.save()

        return Response({"detail": f"{teacher} guruhga qo'shildi"}, status=status.HTTP_200_OK)
    



class RemoveTeacherFromGroupAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, id): 
        teacher_id = request.data.get("teacher_id")

        if not teacher_id:
            return Response({"detail": "teacher_id yuborilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            group = Group.objects.get(id=id)
        except Group.DoesNotExist:
            return Response({"detail": "Bunday group topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Bunday student topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        if teacher not in group.students.all():
            return Response({"detail": "Bu talaba bu guruhda emas"}, status=status.HTTP_400_BAD_REQUEST)

        group.teachers.remove(teacher)
        group.save()

        return Response({"detail": f"{teacher} guruhdan chiqarildi"}, status=status.HTTP_200_OK)
            