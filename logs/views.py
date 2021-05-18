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
# from core.permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from core import models as core_models
from logs import models as logs_models
from logs import serializers as logs_serializers
from panel_user import models as panel_models

now = date.today()
# current_time = datetime.datetime.utcnow().strftime("%H:%M:%S")
# today = datetime.date.today()
def logout():
    return None

def settime(time):
    time = time.split(":")
    if int(time[1]) >= 0 and int(time[1]) < 15:
        return str(time[0]) + ":" + str("00") + ":00"
    elif int(time[1]) >= 15 and int(time[1]) < 30:
        return str(time[0]) + ":" + str("15") + ":00"
    elif int(time[1]) >= 30 and int(time[1]) < 45:
        return str(time[0]) + ":" + str("30") + ":00"
    elif int(time[1]) >= 45 and int(time[1]) < 59:
        return str(time[0]) + ":" + str("45") + ":00"
    
class LogsScoreAPIView(APIView):
    serializer_class = logs_serializers.LogsScoreSerializers
    def get(self, request):
        queryset = logs_models.LogsScore.objects.filter(user = self.request.user, created_at__date = date.today())
        time = []
        score = core_models.SCORE.copy()
        for obj in queryset:
            i_x = core_models.TIMESCALE.index(str(obj.day)+" "+str(obj.time))
            score[i_x] = obj.score
        result = {
            "time":core_models.TIMESCALE,
            "score":score
        }
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        score = data.get("score")
        day = data.get("day")
        time = data.get("time")
        data = {
            "user" : request.user.id,
            "score" : score,
            "day":day if day == str(date.today()) else logout(),
            "time": settime(time) ,
        }
        print(settime(time))
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            obj = serializer.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

