from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="APPLICATION API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authentication.urls")),
    path("mobile/", include("mobile_application.urls")),
    path("profile/", include("profiles.api_urls")),
    path("upload/", include("uploader.urls")),
    path("explore/", include("explore.urls")),
    ### Leads ###
    path("lead/", include("leads.urls")),
   
    ### Panel User ####
    path("users/", include("panel_user.urls")),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path(
        "api/api.json/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-swagger-ui",
    ),    
    # url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
