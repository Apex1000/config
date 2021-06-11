import io
import json
import random
import re
from django.db.models import Q
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
from explore import serializers as explore_serializers
now = date.today()

class ExploreTrending(ListAPIView):
    serializer_class = explore_serializers.StoreSerializer
    
    def get_queryset(self):
        return store_models.Store.objects.filter(city__name__in = ["PRAYAGRAJ"])[:10]
    