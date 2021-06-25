from django.db import models
import uuid
from datetime import datetime, date
length = 255

UPLOAD_TO = "invoice_file"

class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ["-created_at", "-updated_at"]

class Country(models.Model):
    name = models.CharField(max_length=length, blank=True, null=True)
    mobile_code = models.CharField(max_length=5)

    def __str__(self):
        return str(self.name)


class State(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="country_state", default=None
    )
    name = models.CharField(max_length=100)
    qb_code = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return "%s" % (self.name)


class Cities(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    state = models.ForeignKey(
        State,
        on_delete = models.CASCADE,
        related_name = "state_cities",
        default=None,
        blank=True,
        null=True
    )
    display_name = models.CharField(max_length=500)
    connected_to = models.ManyToManyField("self", related_name="panelusers", blank=True)

    def __str__(self):
        return "%s" % (self.display_name)

class Language(models.Model):
    language = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.language)

class ProductType(TimestampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class Status(TimestampedModel):
    status = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return "%s" % (self.status)