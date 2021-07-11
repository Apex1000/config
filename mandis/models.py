from leads.models import Category
from django.db import models
from core.models import TimestampedModel,Cities,UPLOAD_TO


class Product(TimestampedModel):
    CATEGORY = (
        ("FRUITS", "Fruits"),
        ("VEGGE", "Vegetables"),
        ("OTH", "Other")
    )
    product_name = models.CharField(max_length=255,blank=True, null=True)
    category = models.CharField(
        max_length=20, null=True, blank=True, choices=CATEGORY
    )
    
    def __str__(self):
        return "{}".format(self.product_name)

class Mandi(TimestampedModel):
    mandi_name = models.CharField(max_length=255,blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to = UPLOAD_TO,blank=True, null=True)
    product = models.ForeignKey(
        Product,
        related_name="product",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        "core.Cities",
        related_name="city",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return "{}".format(self.mandi_name)