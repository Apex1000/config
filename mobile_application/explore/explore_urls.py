from django.urls import path, include
from mobile_application.explore.explore_views import *

urlpatterns = [
    path("trending/", ExploreTrending.as_view(), name="trending"),
    path("store-description/", StoreDescriptionAPIView.as_view(), name="store_description"),
    # path("store-filter/", UserViewSet.as_view(), name="trending"),
]
