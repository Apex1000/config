from django.urls import path

from profiles.views import (
    ProfileRetrieveAPIView,
)

urlpatterns = [
    path("profile/", ProfileRetrieveAPIView.as_view(), name="panel-user"),
]
