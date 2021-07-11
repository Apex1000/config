from django.db import models
from django.db.models import manager
from core import models as core_models

class Store(core_models.TimestampedModel):
    image = models.ImageField(upload_to = core_models.UPLOAD_TO,blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    query = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    logitude = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(core_models.Cities, related_name='store_city', on_delete=models.CASCADE,blank=True, null=True)
    connected_to = models.ManyToManyField(core_models.Cities, related_name="panelusers", blank=True)
    fulladdr = models.TextField(blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    addr1 = models.CharField(max_length=255, blank=True, null=True)
    addr2 = models.CharField(max_length=255, blank=True, null=True)
    addr3 = models.CharField(max_length=255, blank=True, null=True)
    addr4 = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name
        
class StoreDescription(core_models.TimestampedModel):
    product = models.ForeignKey(
        Store,
        related_name="store",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.product.name
