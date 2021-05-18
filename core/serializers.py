# from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from core import models as core_models
from .models import *
from dateutil import tz
import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = core_models.Cities
        fields = "__all__"