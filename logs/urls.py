from django.urls import path, include
from logs import views as logs_views

urlpatterns = [
    path("logs-score/", logs_views.LogsScoreAPIView.as_view(), name="logs_score"),
]
