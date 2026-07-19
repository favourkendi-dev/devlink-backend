from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# This function runs automatically every time a User is saved
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Without this check, a Profile would try to get created every time a User is saved even when the User is updated We only want to create a Profile when a new User is created
    if created:
        Profile.objects.create(user=instance)