from django.shortcuts import render

# Create your views here.
import threading
from django.contrib.auth.models import User

def create_user():
    print(f"User creation running in thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser')
