from django.db import models
from core import models as core_models

class Store(core_models.TimestampedModel):
    name = models.CharField(max_length=25, blank=True, null=True)
    latitude = models.CharField(max_length=25, blank=True, null=True)
    logitude = models.CharField(max_length=25, blank=True, null=True)
    city = models.ForeignKey(core_models.Cities, related_name='store_city', on_delete=models.CASCADE,blank=True, null=True)
    connected_to = models.ManyToManyField(core_models.Cities, related_name="panelusers", blank=True)
    def __str__(self):
        return self.name