from django.urls import path, include
from panel_user import views as panel_views

urlpatterns = [
    path("profile/", panel_views.ProfileAPIView.as_view(), name="register"),
]
