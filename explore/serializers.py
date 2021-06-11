# from django_countries.serializer_fields import CountryField
from store.models import Store
from rest_framework import serializers
from core import models as core_models
from store import *
from dateutil import tz
import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
