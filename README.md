# Django-Assignment
## Question1:By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance.
Answer: By default, Django signals are executed synchronously. This means that when a signal is triggered, all the registered receivers are called immediately, and the process will not move forward until the signal receivers have finished executing.
**Code**:
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulating a delay
    print("Signal handler finished")

def create_user():
    print("Starting user creation")
    user = User.objects.create(username='testuser')
    print("User creation finished")
Explanation:
In this code, we trigger the signal by creating a new User instance. The signal handler (my_signal_receiver) introduces a 5-second delay using time.sleep(5). The main process will wait for the signal handler to complete before printing "User creation finished", proving that Django signals are executed synchronously.




## Question2:Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance.
Answer: Yes, Django signals run in the same thread as the caller by default. Both the function that triggers the signal and the signal handler are executed in the same thread.
**Code**:
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

def create_user():
    print(f"User creation running in thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser')
Explanation:
When you run the create_user() function, both the user creation process and the signal handler will print the name of the current thread. Since both will show "MainThread", this demonstrates that the signal handler is executed in the same thread as the calling function.




## Question3:By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance.
Answer: Yes, Django signals run in the same database transaction as the caller. This means if a signal is triggered inside a transaction, and that transaction is rolled back, the changes made by the signal handler will also be rolled back.
**code:**
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal handler started - updating user profile")
    instance.profile = 'Updated in Signal'  # Example action
    instance.save()

def create_user_with_transaction():
    try:
        with transaction.atomic():
            print("Transaction started")
            user = User.objects.create(username='testuser')
            raise Exception("Simulated failure - rolling back transaction")
    except Exception as e:
        print(f"Transaction failed: {e}")
Explanation:
In this code, we use transaction.atomic() to wrap the user creation in a database transaction. The signal handler is triggered after the User instance is created. However, we raise an exception to simulate a failure, which causes the entire transaction (including the signal handler's changes) to be rolled back. This proves that Django signals participate in the same database transaction as the code that triggers them.

## customDescription: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
**code:**
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define the iterator method to yield length and width as dictionaries
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rectangle = Rectangle(length=5, width=10)

# Iterating over the rectangle instance
for dimension in rectangle:
    print(dimension)
Explanation:
__init__() method: Initializes the Rectangle object with length and width.
__iter__() method: Defines how the object should behave when iterated over. It uses yield to return the dimensions in the specified dictionary format.
When you run this code, it will first return {'length': 5} and then {'width': 10}.
