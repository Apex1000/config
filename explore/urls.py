from django.urls import path, include
from explore import views as explore_views

urlpatterns = [
    path("trending/", explore_views.ExploreTrending.as_view(), name="trending"),
]
