from django.contrib import admin

from authentication.models import User

class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "username",
        "email",
        "created_at",
    )
    search_fields = [
        "id",
        "username",
    ]

admin.site.register(User,LeadAdmin)