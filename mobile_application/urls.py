from django.urls import path, include
from mobile_application import views as mobile_views

urlpatterns = [
    path("near-by/", mobile_views.DistanceProximityAPIView.as_view(), name="near_by"),
]
