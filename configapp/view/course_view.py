from rest_framework.views import APIView, Response, status
from configapp.serializers.course_serializer import *
from drf_yasg.utils import swagger_auto_schema
from configapp.serializers.group_serializer import GroupSerializer

class CourseCreateAPIView(APIView):
    @swagger_auto_schema(request_body=CourseSerializer)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class CourseGetAPIView(APIView):
    def get(self, request, pk):
        if pk:
            try:
                course = Course.objects.get(pk=pk)
            except:
                return Response({"message":"Kurs topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CourseSerializer(course)
            
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        else:
            try:
                courses = Course.objects.all()
            except:
                return Response({"message":"Courselar topilmadi"}, status=status.HTTP_304_NOT_MODIFIED)
            
            serializer = CourseSerializer(courses, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CourseDeleteAPI(APIView):
    def post(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except:
            return Response({"message":"Kurs topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        course.delete()
        return Response({"message":"Kurs o'chirildi!"}, status=status.HTTP_204_NO_CONTENT)
    

class CourseChangeAPI(APIView):
    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetGroupsByIdsApiView(APIView):
    def post(self, request):
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"detail": "IDs ro'yxati yuborilmadi"}, status=status.HTTP_400_BAD_REQUEST)

        groups = Group.objects.filter(id__in=ids)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


