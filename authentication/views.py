from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.views import APIView
from authentication import serializers as auth_serializers
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
# from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRenderer, LoginRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (
    smart_str,
    force_str,
    smart_bytes,
    DjangoUnicodeDecodeError,
)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
# from .utils import Util
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
from authentication.models import User
from authentication.serializers import RegisterSerializer
import os
import json
from django.http import HttpResponse, JsonResponse

class PhoneOTPRegisterView(APIView):
    # serializer_class = RegisterSerializer
    # renderer_classes = (UserRenderer,)
    def post(self, request):
        data = request.data
        user = User.objects.filter(phone = data.get("phone"))
        if not user:
            User.objects.create(
                phone = data.get("phone"),
                password = make_password(data.get("phone")))
        return Response({"status":"OTP Send!"}, status=status.HTTP_200_OK)

class PhoneOTPVarifyView(generics.GenericAPIView):
    serializer_class = auth_serializers.OTPLoginSerializer
    # renderer_classes = (UserRenderer,) 
    def post(self, request):
        user = request.data
        phone = user.get("phone", None)
        pin = user.get("pin", None)
        if pin == "123456":
            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"Incorrect Pin!"}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        print(user)
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(phone=user_data["phone"])
        user.email = request.data.get("email","")
        user.username = request.data.get("username","")
        user.save()
        token = RefreshToken.for_user(user).access_token
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = auth_serializers.LoginSerializer
    renderer_classes = (LoginRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)