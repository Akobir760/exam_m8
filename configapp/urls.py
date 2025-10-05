from django.urls import path
from configapp.view.user_register import *

urlpatterns = [
    path('auth/login/', LoginView.as_view()),
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/me/', MeView.as_view()),
    path('auth/change-password/', ChangePasswordView.as_view()),
    path("auth/reset-password/", ResetPasswordView.as_view()),
    path("auth/verify-otp/", VerifyOTPView.as_view()),
    path("auth/set-new-password/", SetNewPasswordView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
]