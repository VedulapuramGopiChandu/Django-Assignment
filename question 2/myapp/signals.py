import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Receiver function to check the thread name
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")




