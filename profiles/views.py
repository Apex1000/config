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

from profiles.exceptions import ProfileDoesNotExist
from profiles.models import Profile
from profiles.renderers import ProfileJSONRenderer
from profiles.serializers import (
    ProfileUpdateSerializer,
    ProfileSerializer
)
from authentication import models as auth_models


class ProfileRetrieveAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (ProfileJSONRenderer,)
    serializer_class = ProfileSerializer
    update_serializer_class = ProfileUpdateSerializer

    def retrieve(self, request, *args, **kwargs):
        username = request.user
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        try:
            # We use the `select_related` method to avoid making unnecessary
            # database calls.
            profile = Profile.objects.select_related("user").get(
                user__phone=username
            )
            # user = panel_models.PanelUser.select_related('user')
        except Profile.DoesNotExist:
            raise ProfileDoesNotExist

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        username = request.user
        data = request.data
        profile = Profile.objects.select_related("user").get(
                user__phone=username
            )
        data["user"] = username.id
        serializer = self.update_serializer_class(profile,data=data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)