# Week 12 - task 2 (Configure URL Patterns)

from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # URL for the BookList API endpoint
]