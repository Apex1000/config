from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "category",
    )
    search_fields = [
        "id",
        "product_name",
        "category",
    ]

class MandiAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "mandi_name",
        "price",
        "product",
        "city",
    )
    search_fields = [
        "id",
        "mandi_name",
        "price",
        "product__product_name",
        "city",
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Mandi, MandiAdmin)