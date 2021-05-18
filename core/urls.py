from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path("city/", core_views.CityListView.as_view(), name="city"),
]
