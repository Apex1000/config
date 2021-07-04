# from django_countries.serializer_fields import CountryField
from store.models import Store
from rest_framework import serializers
from core import models as core_models
from store import *
from dateutil import tz
import datetime
import pytz
import random
tz = pytz.timezone('Asia/Kolkata')

def store_image():
    images = [
        "https://img.icons8.com/cotton/250/000000/warehouse.png",
        "https://img.icons8.com/plasticine/250/000000/warehouse-1.png",
        "https://img.icons8.com/dusk/250/000000/warehouse.png",
        "https://img.icons8.com/color/250/000000/storage_1.png",
    ]
    return random.choice(images)

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
        return store_image()