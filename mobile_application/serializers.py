from rest_framework import serializers
from panel_user.models import Profile
from store import models as store_models
from haversine import haversine, Unit

class DistanceProximitySerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = store_models.Store
        fields = "__all__"
    
    def get_distance(self,obj):
        logitude = self.context["request"].query_params.get("logitude")
        latitude = self.context["request"].query_params.get("latitude")
        user = (float(logitude), float(latitude))
        store = (float(obj.latitude),float(obj.logitude))
        return str(haversine(user, store))[:6]