from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from profiles.models import Profile
from panel_user.models import PanelUserProfile
from django.conf import settings

User = get_user_model()


@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `User` instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.
    if created:
        Profile.objects.create(user=instance)
        if instance.userrole:
            PanelUserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_related_profile(sender, instance, created, *args, **kwargs):
#     # Notice that we're checking for `created` here. We only want to do this
#     # the first time the `User` instance is created. If the save that caused
#     # this signal to be run was an update action, we know the user already
#     # has a profile.
#     if created:
#         PanelUserProfile.objects.create(user=instance)