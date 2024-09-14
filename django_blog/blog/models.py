'''
from django.db import models

# Create your models here.
''' 

# Week 14 - Task 0 Step_3_1 Create blog_post model

# blog/models.py

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    published_date = models.DateTimeField(auto_now_add=True)  # Date when the post was published
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Author of the post

    def __str__(self):
        return self.title