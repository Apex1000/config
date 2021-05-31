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

    serializer_class = auth_serializers.RegisterSerializer
    # renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # user_data = serializer.data
        # user = User.objects.get(email=user_data["email"])
        # token = RefreshToken.for_user(user).access_token
        # current_site = get_current_site(request).domain
        # relativeLink = reverse("email-verify")
        # absurl = "http://" + current_site + relativeLink + "?token=" + str(token)
        # email_body = (
        #     "Hi "
        #     + user.username
        #     + " Use the link below to verify your email \n"
        #     + absurl
        # )
        # data = {
        #     "email_body": email_body,
        #     "to_email": user.email,
        #     "email_subject": "Verify your email",
        # }

        # Util.send_email(data)
        if user.get("phone"):
            return Response({"error":"Phone Number Requried!"}, status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.filter(phone=user.get("phone"))
        if user_obj:
            return Response({"error":"Phone Number Already Exists!"}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create(
                phone = user.get("phone"),
                email = user.get("email"),
                username = user.get("username"),
                password = make_password(user.get("password"))
            )
        return Response({"status":"User Created!"}, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = auth_serializers.LoginSerializer
    # renderer_classes = (LoginRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)