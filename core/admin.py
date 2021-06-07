from django.contrib import admin
from core import models as core_models
# Register your models here.

class CitiesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "state")
    search_fields = ["id", "name"]

admin.site.register(core_models.Country)
admin.site.register(core_models.State)
admin.site.register(core_models.Cities, CitiesAdmin)
admin.site.register(core_models.Language)