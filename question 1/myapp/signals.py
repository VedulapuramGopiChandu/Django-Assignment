import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, created, **kwargs):
    print(f"Signal handler started for user: {instance.username}")
    time.sleep(5)  # Simulating delay
    print(f"Signal handler finished for user: {instance.username}")
