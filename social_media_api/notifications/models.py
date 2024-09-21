'''
from django.db import models

# Create your models here.
'''

# Week 15 - Task 3 - step 1_2 - Create a Notification model to track notifications in notifications app - ppty

# notifications/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)  # Describes the action (e.g., "liked", "followed")
    
    # Generic foreign key to allow different types of targets (e.g., Post, Comment)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')

    timestamp = models.DateTimeField(auto_now_add=True)

    unread = models.BooleanField(default=True) # cg4

    def __str__(self):
        return f'Notification from {self.actor.username} to {self.recipient.username}: {self.verb}'