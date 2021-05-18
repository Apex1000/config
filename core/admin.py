from django.contrib import admin
from core import models as core_models
# Register your models here.

admin.site.register(core_models.Country)
admin.site.register(core_models.State)
admin.site.register(core_models.Cities)
admin.site.register(core_models.Language)