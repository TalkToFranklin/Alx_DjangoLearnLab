'''
from django.db import models

# Create your models here.
''' 

# Week 14 - Task 0 - Step_3_1 Create blog_post model

# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from .models import Post # Week 14 - Task 3 - Step_1 Define the Comment Model
from taggit.managers import TaggableManager # Week 14 - Task 4 - Step_1 Create the Tag Model

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


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


# Week 14 - Task 4 - Step_1 Create the Tag Model

#ppty

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # Many-to-many relationship

    def __str__(self):
        return self.title


#cg4

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()  # Use taggit's TaggableManager for tagging

    def __str__(self):
        return self.title