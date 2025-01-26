from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from forum.models import EventUser


# Create profile signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        EventUser.objects.create(user=instance)
        print("Profile Created")


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if not instance.is_superuser:
        try:
            instance.eventuser.save()
            print("Profile Updated")
        except EventUser.DoesNotExist:
            # Handle the case where the EventUser does not exist
            EventUser.objects.create(user=instance)
