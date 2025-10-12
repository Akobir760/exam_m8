from rest_framework.views import APIView, Response, status
from drf_yasg.utils import  swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from configapp.serializers.homework_serializer import *
from configapp.models.permmissions import *

class HomeworkReviewListAPI(APIView):
    permission_classes = [IsManagerOrAdmin]
    def get(self, request, pk=None):
        if pk:
            try:
                homework_review = HomeworkReview.objects.get(pk=pk)
            except:
                return Response({"message":"Izoh topilmadi"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = HomeworkReviewSerializer(homework_review)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        reviews = HomeworkReview.objects.all()
        serializer = HomeworkReviewSerializer(reviews, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class HomeworkReviewCreateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=HomeworkReviewSerializer)
    def post(self, request):
        serializer = HomeworkReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeworkReviewDelAPI(APIView):
    permission_classes = [IsManagerOrAdmin]


    def delete(self, request, pk):
        try:
            homework_review = HomeworkReview.objects.get(pk=pk)
        except HomeworkReview.DoesNotExist:
            return Response({"message":"Izoh topilmadi"}, status=status.HTTP_400_BAD_REQUEST)
        
        homework_review.delete()

        return Response({"message":"Izoh o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
    

class HomeworkReviewUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=HomeworkReviewSerializer)
    def put(self, request, pk):
        try:
            homework_review = HomeworkReview.objects.get(pk=pk)
        except:
            return Response({"message":"Izoh topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = HomeworkReviewSerializer(instance = homework_review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class HomeworkSubmissionsListAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request, pk=None):
        if pk:
            try:
                homework_submission = HomeworkSubmission.objects.get(pk=pk)
            except:
                return Response({"message":"Vazifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = HomeworkSubmissionSerializer(homework_submission)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        homework_submissions = HomeworkSubmission.objects.all()
        serializer = HomeworkSubmissionSerializer(homework_submissions, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class HomewrokSubmissionCreateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=HomeworkSubmissionSerializer)
    def post(self, request):
        serializer = HomeworkSubmissionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeworkSubmissionDElAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def delete(self, request, pk):
        try:
            homework_submission = HomeworkSubmission.objects.get(pk=pk)
        except HomeworkSubmission.DoesNotExist:
            return Response({"message":"Vazifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        homework_submission.delete()

        return Response({"message":"Vazifa o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
    

class HomeworkSubmissionUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]
    @swagger_auto_schema(request_body=HomeworkSubmissionSerializer)

    def put(self, request, pk):
        try:
            homework_submission = HomeworkSubmission.objects.get(pk=pk)
        except:
            return Response({"message":"Vazifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = HomeworkSubmissionSerializer(instance = homework_submission, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class HomeworkListAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request, pk=None):
        if pk:
            try:
                homework = Homework.objects.get(pk=pk)
            except:
                return Response({"message":"Vazifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = HomeworkSerializer(homework)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        homework = Homework.objects.all()
        serializer = HomeworkSerializer(homework, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class HomeworkCreateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=HomeworkSerializer)
    def post(self, request):

        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeworkDelAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def delete(self, request, pk):

        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({"message":"Vazifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        homework.delete()
        return Response({"message":"Vazifa o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
    

class HomeworkUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=HomeworkSerializer)
    def put(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except:
            return Response({"message":"Vazifa topilmadi"})
        
        serializer = HomeworkSerializer(instance=homework, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectListAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def get(self, request, pk=None):
        if pk:
            try:
                subject = Subject.objects.get(pk=pk)
            except:
                return Response({"message":"Fan topilmadi"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = SubjectSerializer(subject)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class SubjectCreateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=SubjectSerializer)
    def post(self, request):

        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubjectDelAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    def delete(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"message":"Fan topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        
        subject.delete()

        return Response({"message":"fan o'chirildi"}, status=status.HTTP_204_NO_CONTENT)


class SubjectUpdateAPI(APIView):
    permission_classes = [IsManagerOrAdmin]

    @swagger_auto_schema(request_body=SubjectSerializer)
    def put(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"message":"Fan topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SubjectSerializer(instance=subject, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        
