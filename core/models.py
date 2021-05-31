from django.db import models
import uuid
from datetime import datetime, date
length = 255



TIMESCALE = [
                str( date.today())+" 01:00:00",
                str( date.today())+" 01:15:00",
                str( date.today())+" 01:30:00",
                str( date.today())+" 01:45:00",
                str( date.today())+" 02:00:00",
                str( date.today())+" 02:15:00",
                str( date.today())+" 02:30:00",
                str( date.today())+" 02:45:00",
                str( date.today())+" 03:00:00",
                str( date.today())+" 03:15:00",
                str( date.today())+" 03:30:00",
                str( date.today())+" 03:45:00",
                str( date.today())+" 04:00:00",
                str( date.today())+" 04:15:00",
                str( date.today())+" 04:30:00",
                str( date.today())+" 04:45:00",
                str( date.today())+" 05:00:00",
                str( date.today())+" 05:15:00",
                str( date.today())+" 05:30:00",
                str( date.today())+" 05:45:00",
                str( date.today())+" 06:00:00",
                str( date.today())+" 06:15:00",
                str( date.today())+" 06:30:00",
                str( date.today())+" 06:45:00",
                str( date.today())+" 07:00:00",
                str( date.today())+" 07:15:00",
                str( date.today())+" 07:30:00",
                str( date.today())+" 07:45:00",
                str( date.today())+" 08:00:00",
                str( date.today())+" 08:15:00",
                str( date.today())+" 08:30:00",
                str( date.today())+" 08:45:00",
                str( date.today())+" 09:00:00",
                str( date.today())+" 09:15:00",
                str( date.today())+" 09:30:00",
                str( date.today())+" 09:45:00",
                str( date.today())+" 10:00:00",
                str( date.today())+" 10:15:00",
                str( date.today())+" 10:30:00",
                str( date.today())+" 10:45:00",
                str( date.today())+" 11:00:00",
                str( date.today())+" 11:15:00",
                str( date.today())+" 11:30:00",
                str( date.today())+" 11:45:00",
                str( date.today())+" 12:00:00",
                str( date.today())+" 12:15:00",
                str( date.today())+" 12:30:00",
                str( date.today())+" 12:45:00",
                str( date.today())+" 13:00:00",
                str( date.today())+" 13:15:00",
                str( date.today())+" 13:30:00",
                str( date.today())+" 13:45:00",
                str( date.today())+" 14:00:00",
                str( date.today())+" 14:15:00",
                str( date.today())+" 14:30:00",
                str( date.today())+" 14:45:00",
                str( date.today())+" 15:00:00",
                str( date.today())+" 15:15:00",
                str( date.today())+" 15:30:00",
                str( date.today())+" 15:45:00",
                str( date.today())+" 16:00:00",
                str( date.today())+" 16:15:00",
                str( date.today())+" 16:30:00",
                str( date.today())+" 16:45:00",
                str( date.today())+" 17:00:00",
                str( date.today())+" 17:15:00",
                str( date.today())+" 17:30:00",
                str( date.today())+" 17:45:00",
                str( date.today())+" 18:00:00",
                str( date.today())+" 18:15:00",
                str( date.today())+" 18:30:00",
                str( date.today())+" 18:45:00",
                str( date.today())+" 19:00:00",
                str( date.today())+" 19:15:00",
                str( date.today())+" 19:30:00",
                str( date.today())+" 19:45:00",
                str( date.today())+" 20:00:00",
                str( date.today())+" 20:15:00",
                str( date.today())+" 20:30:00",
                str( date.today())+" 20:45:00",
                str( date.today())+" 21:00:00",
                str( date.today())+" 21:15:00",
                str( date.today())+" 21:30:00",
                str( date.today())+" 21:45:00",
                str( date.today())+" 22:00:00",
                str( date.today())+" 22:15:00",
                str( date.today())+" 22:30:00",
                str( date.today())+" 22:45:00",
                str( date.today())+" 23:00:00",
                str( date.today())+" 23:15:00",
                str( date.today())+" 23:30:00",
                str( date.today())+" 23:45:00",
                str( date.today())+" 00:00:00",
                str( date.today())+" 00:15:00",
                str( date.today())+" 00:30:00",
                str( date.today())+" 00:45:00",
            ]

SCORE = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]

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