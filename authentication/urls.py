from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from authentication.views import *

urlpatterns = [
    path("register-get-otp/", PhoneOTPRegisterView.as_view(), name="register_get_otp"),
    path("register-verify-otp/", PhoneOTPVarifyView.as_view(), name="register_verify_otp"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
]

