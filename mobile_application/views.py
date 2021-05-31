import io
import json
import random
import re
# from django_countries import countries
from django.db.models import Q
# from django_countries.fields import Country
# from phonenumbers.phonenumberutil import region_code_for_number
# from phonenumbers.phonenumberutil import region_code_for_country_code
# import phonenumbers
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListCreateAPIView,
)
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
import store
# from core.permissions import IsOwner
# from .functions import LogActivity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from leads import models as lead_models
from leads import serializers as lead_serializers
from panel_user import models as panel_models
from panel_user import serializers as panel_serializers
from core import models as core_models
from store import models as store_models
from mobile_application import serializers as mobile_application_serializers
from haversine import haversine, Unit
from geopy.geocoders import Nominatim

now = date.today()

class DistanceProximityAPIView(ListAPIView):
    serializer_class = mobile_application_serializers.DistanceProximitySerializer
    def get_queryset(self):
        logitude = self.request.query_params.get("logitude")
        latitude = self.request.query_params.get("latitude")
        geolocator = Nominatim(user_agent="mobile_app")
        location = geolocator.reverse(logitude+","+latitude)
        address = location.raw['address']['city']
        store_objs = store_models.Store.objects.filter()
        return store_objs
    