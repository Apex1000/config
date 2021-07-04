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
    image = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    
    class Meta:
        model = Store
        fields = (
            "id",
            "name",
            "manager",
            "phone_number",
            "fulladdr",
            "district",
            "city",
            "image",
        )
    
    def get_city(self,obj):
        return obj.city.name if obj.city else None
    
    def get_image(self,obj):
        return "https://img.icons8.com/cotton/250/000000/warehouse.png"