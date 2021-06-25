import uuid
from django.db import models
from core.models import TimestampedModel
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from core.models import UPLOAD_TO

def image_upload_to(instance, filename):
    uid = str(uuid.uuid4())
    ext = filename.split(".")[-1].lower()
    return "profile-images/{}/{}.{}".format(instance.pk, uid, ext)


class Profile(TimestampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField("authentication.User", on_delete=models.CASCADE, related_name="profile_user")
    image = models.ImageField(upload_to=UPLOAD_TO, blank=True)
    contact_verified = models.BooleanField(default=False)
    first_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="First Name"
    )
    last_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Last Name"
    )
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="City"
    )
    state = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="State"
    )
    pin_code = models.CharField(
        max_length=6, null=True, blank=True
    )

    def __str__(self):
        return str(self.user.phone)
