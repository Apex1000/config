from django.db import models
from core import models as core_models

class UserRoles(core_models.TimestampedModel):
    name = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name

class Provider(core_models.TimestampedModel):
    name = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.name

class PanelUserProfile(core_models.TimestampedModel):
    user = models.OneToOneField("authentication.User",on_delete=models.CASCADE)
    user_type = models.ForeignKey(UserRoles, related_name='profile_userroles', on_delete=models.CASCADE,blank=True, null=True)
    assigned = models.ManyToManyField("self", related_name="panelusers", blank=True)
    cities = models.ManyToManyField(core_models.Cities, blank=True)
    # provider = models.ForeignKey(Provider, related_name='profile_provider', on_delete=models.CASCADE,blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
