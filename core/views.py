import io
import json
import random
import re
# import pandas as pd
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
from itertools import islice
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
# from core.permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework.renderers import JSONRenderer
from core.renderers import DataRenderer
from django.http import HttpResponse, JsonResponse
from leads import models as lead_models
from leads import serializers as lead_serializers
from panel_user import models as panel_models
from core import models as core_models
from core import serializers as core_serializers
from core.paginations import StandardResultsSetPagination

now = date.today()
# current_time = datetime.datetime.utcnow().strftime("%H:%M:%S")
# today = datetime.date.today()

class CityListView(ListAPIView):
    serializer_class = core_serializers.CitySerializers
    renderer_classes = (DataRenderer,)
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        q = self.request.GET.get("q")
        queryset = core_models.Cities.objects.filter(display_name__contains = q)
        return queryset