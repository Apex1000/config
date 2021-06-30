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
        d = {}
        data = request.data
        print(username.id)
        if data.get("first_name"):
            d["first_name"] = data.get("first_name")
        if data.get("last_name"):
            d["last_name"] = data.get("last_name")
        if data.get("age"):
            d["age"] = data.get("age")
        if data.get("address"):
            d["address"] = data.get("address")
        if data.get("city"):
            d["city"] = data.get("city")
        if data.get("state"):
            d["state"] = data.get("state")
        if data.get("pin_code"):
            d["pin_code"] = data.get("pin_code")
        if data.get("image"):
            d["image"] = data.get("image")

        profile = Profile.objects.select_related("user").get(
                user__phone=username
            )
        d["user"] = username.id
        serializer = self.update_serializer_class(profile,data=d)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)