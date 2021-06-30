from rest_framework import serializers

from profiles import models as profiles_models
from core import models as core_models
from django.conf import settings

class ProfileUpdateSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    
    class Meta:
        model = profiles_models.Profile
        fields = ("__all__")
    
    def get_phone(self, instance):
        return instance.user.phone
class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField("get_image_url")
    
    class Meta:
        model = profiles_models.Profile
        fields = (
            "image_url",
            "first_name",
            "last_name",
            "age",
            "address",
            "city",
            "state",
            "pin_code",
            "phone"
        )
    
    def get_image_url(self, instance):
        try:
            url = instance.image.url
        except:
            url = ""
        print(settings.MEDIA_URL)
        return '%s%s' % (settings.MEDIA_URL, instance.image)
    
    def get_phone(self, instance):
        return instance.user.phone