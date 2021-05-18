from rest_framework import status
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    GenericAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from .serializers import (
    ProfileSerializer,
)
# from profiles.exceptions import ProfileDoesNotExist
from panel_user.models import Profile
# from profiles.renderers import ProfileJSONRenderer


class ProfileAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Profile, user=self.request.user)
        return obj