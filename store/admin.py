from django.contrib import admin
from store import models as store_models

admin.site.register(store_models.Store)
