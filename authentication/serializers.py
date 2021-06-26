from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (
    smart_str,
    force_str,
    smart_bytes,
    DjangoUnicodeDecodeError,
)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        "username": "The username should only contain alphanumeric characters"
    }

    class Meta:
        model = User
        fields = [ "password", "phone"]

    def validate(self, attrs):
        # email = attrs.get("email", "")
        # username = attrs.get("username", "")

        # if not username.isalnum():
        #     raise serializers.ValidationError(self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class OTPLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255, required=False)
    tokens = serializers.SerializerMethodField()
    phonenumber = serializers.CharField(max_length=255, read_only=True)

    def get_tokens(self, obj):
        print(obj["phonenumber"],"fr")
        user = User.objects.get(phone=obj["phonenumber"])

        return {"refresh": user.tokens()["refresh"], "access": user.tokens()["access"]}

    def validate(self, data):
        phone = data.get("phone", None)
        user = User.objects.get(phone=phone)
        print(user)
        if not user:
            raise AuthenticationFailed("Invalid credentials, try again")
        # if not user.is_active:
        #     raise AuthenticationFailed('Account disabled, contact admin')
        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        return {"tokens": user.tokens,"phonenumber":user.phone}

        # return super().validate(attrs)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj["email"])

        return {"refresh": user.tokens()["refresh"], "access": user.tokens()["access"]}

    class Meta:
        model = User
        fields = ["email", "password", "username", "tokens"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        filtered_user_by_email = User.objects.get(email=email)
        user = authenticate(phone=filtered_user_by_email.phone, password=password)
        # print(user)
        # if (
        #     filtered_user_by_email.exists()
        #     and filtered_user_by_email[0].auth_provider != "email"
        # ):
        #     raise AuthenticationFailed(
        #         detail="Please continue your login using "
        #         + filtered_user_by_email[0].auth_provider
        #     )

        # if not user:
        #     raise AuthenticationFailed("Invalid credentials, try again")
        # if not user.is_active:
        #     raise AuthenticationFailed('Account disabled, contact admin')
        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        return {"email": user.email, "username": user.username, "tokens": user.tokens}

        return super().validate(attrs)