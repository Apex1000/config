# from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from core import models as core_models
from .models import *
from dateutil import tz
import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')

class LogsScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = LogsScore
        fields = "__all__"