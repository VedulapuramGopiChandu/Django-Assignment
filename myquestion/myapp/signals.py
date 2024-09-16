from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Receiver function that performs a database operation
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal handler started - updating user profile")
    instance.profile = 'Updated in Signal'  # Example action
    instance.save()
    print("Signal handler finished")
