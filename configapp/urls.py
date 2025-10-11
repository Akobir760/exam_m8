from django.urls import path
from configapp.view.views import *

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
    path('users/create/user/', RegisterAPIView.as_view()),

    # USERS MANAGEMENT
    path('users/', UsersListAPIVIew.as_view()),
    path('users/create/student/', StudentAPIView.as_view()),
    path('users/create/teacher/', TeacherCreateAPI.as_view()),
    path('users/create/superuser/', SuperUserAPIView.as_view()),
    path('users/create/user/', RegisterAPIView.as_view()),
    path('users/delete/user/{id}/', DeleteUserAPIView.as_view()),

    # STUDENT MANAGEMENT
    path("users/students/", StudentsListAPI.as_view()),
    path("users/student/{id}/", StudentsListAPI.as_view()),
    path("users/update/student/{id}/", UpdateStudentApi.as_view()),
    path("users/update/student/{id}/", UpdateStudentApi.as_view()),
    path("users/get-students-by-ids/", GetStudentsByIdsAPIView.as_view()),
    path("student-groups/{student_id}/", StudentGroupsAPIView.as_view()),
    path("api/v1/attendance/student/{student_id}/", StudentAttendanceByMonthAPIView.as_view()),

    # TEACHER MANAGEMENT
    path("users/teachers/", TeacherApiView.as_view(), name="teacher_list"),
    path("users/teacher/<int:id>/", TeacherApiView.as_view(), name="teacher_detail"),
    path("users/update/teacher/<int:id>/", UpdateTeacherAPI.as_view(), name="teacher_update"),
    path("users/get-teachers-by-ids/", GetTeachersByIdsAPIView.as_view(), name="get_teachers_by_ids"),
    path("teacher-groups/<int:teacher_id>/", TeacherGroupsAPIView.as_view(), name="teacher_groups"),
    path("teacher-group/<int:teacher_id>/<int:group_id>/", TeacherGroupDetailView.as_view(), name="teacher_group_detail"),


    # ATTENDANCE APIs
    path("attendances/attendance/", AttendanceRetrieveAPiView.as_view()),
    path("attendances/attendance/create/attendance/", AttendaceCreateAPIView.as_view()),
    path("attendances/attendance/{id}/", AttendanceRetrieveAPiView.as_view()),
    path("attendances/attendance/{id}/delete/attendance/", AttendanceDeleteAPIView.as_view()),
    path("attendances/attendance/{id}/update/attendance/", AttendanceUpdateAPIView.as_view()),

    # ATTENDANCE STATUS
    path("attendances/status/", AttendanceLevelGetAPIView.as_view()),
    path("attendances/status/create/status/", AttendaceCreateAPIView.as_view()),
    path("attendances/status/{id}/", AttendanceLevelGetAPIView.as_view()),
    path("attendances/status/{id}/delete/status/", AttendanceLevelDeleteAPI.as_view()),
    path("attendances/status/{id}/update/status/", AttendanceLevelUpdateAPI.as_view()),

    # COURSES APIs
    path("courses/courses/", CourseGetAPIView.as_view()),
    path("courses/courses/create/course/", CourseCreateAPIView.as_view()),
    path("courses/courses/{id}/", CourseGetAPIView.as_view()),
    path("courses/courses/{id}/delete/course/", CourseDeleteAPI.as_view()),
    path("courses/courses/{id}/update/course/", CourseChangeAPI.as_view()),
    path("courses/courses/{id}/update/course/", CourseChangeAPI.as_view()),
    path("courses/get-groups-by-ids/", GetGroupsByIdsApiView.as_view()),

    # GROUPS APIs
    path("courses/groups/", GroupsListAPI.as_view()),
    path("courses/groups/create/group/", GroupCreateAPIView.as_view()),
    path("courses/groups/{id}/", GroupsListAPI.as_view()),
    path("courses/groups/{id}/add-student/", AddStudentToGroupAPIView.as_view()),
    path("courses/groups/{id}/add-teacher/", AddTeacherToGroupAPIView.as_view()),
    path("courses/groups/{id}/delete/group/", GroupDeleteAPI.as_view()),
    path("courses/groups/{id}/remove-student/", RemoveStudentFromGroupAPIView.as_view()),
    path("courses/groups/{id}/remove-teacher/", RemoveTeacherFromGroupAPIView.as_view()),
    path("courses/groups/{id}/update/group/", GroupUpdateAPI.as_view()),


    # HOMEWORKS API
    path("courses/homework-reviews/", HomeworkReviewListAPI.as_view()),
    path("courses/homework-reviews/create/homework-review/", HomeworkReviewCreateAPI.as_view()),
    path("courses/homework-reviews/{id}/", HomeworkReviewListAPI.as_view()),
    path("courses/homework-reviews/{id}/delete/homework-review/", HomeworkReviewDelAPI.as_view()),
    path("courses/homework-reviews/{id}/update/homework-review/", HomeworkReviewUpdateAPI.as_view()),

    path("courses/homework-submissions/", HomeworkSubmissionsListAPI.as_view()),
    path("courses/homework-submissions/create/homework-submission/", HomewrokSubmissionCreateAPI.as_view()),
    path("courses/homework-submissions/{id}/", HomeworkSubmissionsListAPI.as_view()),
    path("courses/homework-submissions/{id}/delete/homework-submission/", HomeworkSubmissionDElAPI.as_view()),
    path("courses/homework-submissions/{id}/update/homework-submission", HomeworkSubmissionUpdateAPI.as_view()),

    path("courses/homeworks/", HomeworkListAPI.as_view()),
    path("courses/homeworks/create/homework/", HomeworkCreateAPI.as_view()),
    path("courses/homeworks/{id}/", HomeworkListAPI.as_view()),
    path("courses/homeworks/{id}/delete/homework/ ", HomeworkUpdateAPI.as_view()),

    # SUBJECT API's
    path("courses/subjects/", SubjectListAPI.as_view()),
    path("courses/subjects/create/subject/", SubjectCreateAPI.as_view()),
    path("courses/subjects/{id}/ ", SubjectListAPI.as_view()),
    path("courses/subjects/{id}/delete/subject/ ", SubjectDelAPI.as_view()),
    path("courses/subjects/{id}/update/subject/ ", SubjectUpdateAPI.as_view()),

    # TABLE API's
    path("courses/tables/", TableListAPI.as_view()),
    path("courses/tables/create/table/", TableCreateAPI.as_view()),
    path("courses/tables/{id}/ ", TableListAPI.as_view()),
    path("courses/tables/{id}/delete/table/ ", TableDelAPI.as_view()),
    path("courses/tables/{id}/update/table/", TableUpdateAPI.as_view()),

    path("courses/table-types/", TableTypeListAPI.as_view()),
    path("courses/table-types/create/tabletype/ ", TableTypeCreateAPI.as_view()),
    path("courses/table-types/{id}/ ", TableTypeListAPI.as_view()),
    path("courses/table-types/{id}/delete/tabletype/ ", TableTypeDelAPI.as_view()),
    path("courses/table-types/{id}/update/tabletype/ ", TableTypeUpdate.as_view()),

    # PAYMENT API's
    path("payments/payment-type/", PaymentTypeListAPI.as_view()),
    path("payments/payment-type/create/payment-type/ ", PaymentTypeCreateAPI.as_view()),
    path("payments/payment-type/{id}/ ", PaymentTypeListAPI.as_view()),
    path("payments/payment-type/{id}/delete/payment-type/ ", PaymentDelAPI.as_view()),
    path("payments/payment-type/{id}/update/payment-type/ ", PaymentUpdateAPI.as_view()),

    path("payments/payment/", PaymnetListAPI.as_view()),
    path("payments/payment/create/payment/", PaymentTypeCreateAPI.as_view()),
    path("payments/payment/{id}/", PaymnetListAPI.as_view()),
    path("payments/payment/{id}/delete/payment/", PaymentDelAPI.as_view()),
    path("payments/payment/{id}/update/payment/", PaymentUpdateAPI.as_view()),
    
]