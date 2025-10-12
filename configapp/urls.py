from django.urls import path
from configapp.view.views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # AUTH API
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/me/', MeView.as_view()),
    path('auth/change-password/', ChangePasswordView.as_view()),
    path("auth/reset-password/", ResetPasswordView.as_view()),
    path("auth/verify-otp/", VerifyOTPView.as_view()),
    path("auth/set-new-password/", SetNewPasswordView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),

    # USERS MANAGEMENT
    path('users/', UsersListAPIVIew.as_view()),
    path('users/create/student/', StudentAPIView.as_view()),
    path('users/create/teacher/', TeacherCreateAPI.as_view()),
    path('users/create/superuser/', SuperUserAPIView.as_view()),
    path('users/delete/user/<int:pk>/', DeleteUserAPIView.as_view()),
    path('users/delete/teacher/<int:pk>/', DeleteTeacherAPIView.as_view()),
    path('users/delete/student/<int:pk>/', DeleteStudentAPIView.as_view()),

    # STUDENT MANAGEMENT
    path("users/students/", StudentsListAPI.as_view()),
    path("users/student/<int:pk>/", StudentsListAPI.as_view()),
    path("users/update/student/<int:pk>/", UpdateStudentApi.as_view()),
    path("users/update/student/<int:pk>/", UpdateStudentApi.as_view()),
    path("users/get-students-by-ids/", GetStudentsByIdsAPIView.as_view()),
    path("student-groups/<int:student_id>/", StudentGroupsAPIView.as_view()),
    path("api/v1/attendance/student/<int:student_id>/", StudentAttendanceByMonthAPIView.as_view()),

    # TEACHER MANAGEMENT
    path("users/teachers/", TeacherApiView.as_view(), name="teacher_list"),
    path("users/teacher/<int:pk>/", TeacherApiView.as_view(), name="teacher_detail"),
    path("users/update/teacher/<int:id>/", UpdateTeacherAPI.as_view(), name="teacher_update"),
    path("users/get-teachers-by-ids/", GetTeachersByIdsAPIView.as_view(), name="get_teachers_by_ids"),
    path("teacher-groups/<int:teacher_id>/", TeacherGroupsAPIView.as_view(), name="teacher_groups"),
    path("teacher-group/<int:teacher_id>/<int:group_id>/", TeacherGroupDetailView.as_view(), name="teacher_group_detail"),
    path('attendance/by-date/', AttendanceFilterView.as_view(), name='attendance-by-date'),



    # ATTENDANCE APIs
    path("attendances/attendance/", AttendanceRetrieveAPiView.as_view()),
    path("attendances/attendance/create/attendance/", AttendaceCreateAPIView.as_view()),
    path("attendances/attendance/<int:pk>/", AttendanceRetrieveAPiView.as_view()),
    path("attendances/attendance/<int:pk>/delete/attendance/", AttendanceDeleteAPIView.as_view()),
    path("attendances/attendance/<int:pk>/update/attendance/", AttendanceUpdateAPIView.as_view()),

    # ATTENDANCE STATUS ishladi
    path("attendances/status/", AttendanceLevelGetAPIView.as_view()),
    path("attendances/status/create/status/", AttendanceLevelAPIView.as_view()),
    path("attendances/status/<int:pk>/", AttendanceLevelGetAPIView.as_view()),
    path("attendances/status/<int:pk>/delete/status/", AttendanceLevelDeleteAPI.as_view()),
    path("attendances/status/<int:pk>/update/status/", AttendanceLevelUpdateAPI.as_view()),

    # COURSES APIs ishladi
    path("courses/courses/", CourseGetAPIView.as_view()),
    path("courses/courses/create/course/", CourseCreateAPIView.as_view()),
    path("courses/courses/<int:pk>/", CourseGetAPIView.as_view()),
    path("courses/courses/<int:pk>/delete/course/", CourseDeleteAPI.as_view()),
    path("courses/courses/<int:pk>/update/course/", CourseChangeAPI.as_view()),
    path("courses/get-groups-by-ids/", GetGroupsByIdsApiView.as_view()),

    # GROUPS APIs
    path("courses/groups/", GroupsListAPI.as_view()),
    path("courses/groups/create/group/", GroupCreateAPIView.as_view()),
    path("courses/groups/<int:pk>/", GroupsListAPI.as_view()),
    path("courses/groups/<int:pk>/add-student/", AddStudentToGroupAPIView.as_view()),
    path("courses/groups/<int:pk>/add-teacher/", AddTeacherToGroupAPIView.as_view()),
    path("courses/groups/<int:pk>/delete/group/", GroupDeleteAPI.as_view()),
    path("courses/groups/<int:pk>/remove-student/", RemoveStudentFromGroupAPIView.as_view()),
    path("courses/groups/<int:pk>/remove-teacher/", RemoveTeacherFromGroupAPIView.as_view()),
    path("courses/groups/<int:pk>/update/group/", GroupUpdateAPI.as_view()),


    # HOMEWORKS API
    path("courses/homework-reviews/", HomeworkReviewListAPI.as_view()),
    path("courses/homework-reviews/create/homework-review/", HomeworkReviewCreateAPI.as_view()),
    path("courses/homework-reviews/<int:pk>/", HomeworkReviewListAPI.as_view()),
    path("courses/homework-reviews/<int:pk>/delete/homework-review/", HomeworkReviewDelAPI.as_view()),
    path("courses/homework-reviews/<int:pk>/update/homework-review/", HomeworkReviewUpdateAPI.as_view()),

    path("courses/homework-submissions/", HomeworkSubmissionsListAPI.as_view()),
    path("courses/homework-submissions/create/homework-submission/", HomewrokSubmissionCreateAPI.as_view()),
    path("courses/homework-submissions/<int:pk>/", HomeworkSubmissionsListAPI.as_view()),
    path("courses/homework-submissions/<int:pk>/delete/homework-submission/", HomeworkSubmissionDElAPI.as_view()),
    path("courses/homework-submissions/<int:pk>/update/homework-submission", HomeworkSubmissionUpdateAPI.as_view()),

    path("courses/homeworks/", HomeworkListAPI.as_view()),
    path("courses/homeworks/create/homework/", HomeworkCreateAPI.as_view()),
    path("courses/homeworks/<int:pk>/", HomeworkListAPI.as_view()),
    path("courses/homeworks/<int:pk>/delete/homework/ ", HomeworkUpdateAPI.as_view()),

    # SUBJECT API's
    path("courses/subjects/", SubjectListAPI.as_view()),
    path("courses/subjects/create/subject/", SubjectCreateAPI.as_view()),
    path("courses/subjects/<int:pk>/ ", SubjectListAPI.as_view()),
    path("courses/subjects/<int:pk>/delete/subject/ ", SubjectDelAPI.as_view()),
    path("courses/subjects/<int:pk>/update/subject/ ", SubjectUpdateAPI.as_view()),

    # TABLE API's
    path("courses/tables/", TableListAPI.as_view()),
    path("courses/tables/create/table/", TableCreateAPI.as_view()),
    path("courses/tables/<int:pk>/ ", TableListAPI.as_view()),
    path("courses/tables/<int:pk>/delete/table/ ", TableDelAPI.as_view()),
    path("courses/tables/<int:pk>/update/table/", TableUpdateAPI.as_view()),

    path("courses/table-types/", TableTypeListAPI.as_view()),
    path("courses/table-types/create/tabletype/", TableTypeCreateAPI.as_view()),
    path("courses/table-types/<int:pk>/ ", TableTypeListAPI.as_view()),
    path("courses/table-types/<int:pk>/delete/tabletype/", TableTypeDelAPI.as_view()),
    path("courses/table-types/<int:pk>/update/tabletype/", TableTypeUpdate.as_view()),

    # PAYMENT API's
    path("payments/payment-type/", PaymentTypeListAPI.as_view()),
    path("payments/payment-type/create/payment-type/ ", PaymentTypeCreateAPI.as_view()),
    path("payments/payment-type/<int:pk>/ ", PaymentTypeListAPI.as_view()),
    path("payments/payment-type/<int:pk>/delete/payment-type/ ", PaymentDelAPI.as_view()),
    path("payments/payment-type/<int:pk>/update/payment-type/ ", PaymentUpdateAPI.as_view()),

    path("payments/payment/", PaymnetListAPI.as_view()),
    path("payments/payment/create/payment/", PaymentCteateAPI.as_view()),
    path("payments/payment/<int:pk>/", PaymnetListAPI.as_view()),
    path("payments/payment/<int:pk>/delete/payment/", PaymentDelAPI.as_view()),
    path("payments/payment/<int:pk>/update/payment/", PaymentUpdateAPI.as_view()),
    
]