from django.shortcuts import render

# Create your views here.
from django.db import transaction
from django.contrib.auth.models import User

def create_user_with_transaction():
    try:
        with transaction.atomic():
            print("Transaction started")
            user = User.objects.create(username='testuser')
            raise Exception("Simulated failure - rolling back transaction")
    except Exception as e:
        print(f"Transaction failed: {e}")
