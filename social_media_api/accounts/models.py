'''
from django.db import models

# Create your models here.
'''

# Week 15 - Task 0 - step 2_1 - Create a Custom User Model

# accounts/models.py
from django.contrib.auth.models import AbstractUser, get_user_model
from django.db import models

User = get_user_model() # Week 15 - Task 2 - step 1 - Update the User Model to Handle Follows

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
