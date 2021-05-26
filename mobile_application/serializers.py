from rest_framework import serializers
from panel_user.models import Profile
from store import models as store_models

class DistanceProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = store_models.Store
        fields = "__all__"