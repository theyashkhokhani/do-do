from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Folder

@receiver(post_save, sender=User)
def new_user_created(sender, instance, created, **kwargs):
    if created:
        # print(f"New user created: {instance.username}") # For DEBUGGING
        Folder.objects.create(name="Home", user=instance)