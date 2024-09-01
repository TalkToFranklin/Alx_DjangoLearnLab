# Week 12 - task 2 (Create the API View)

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all book instances
    serializer_class = BookSerializer # Use the BookSerializer for serialization





from django.shortcuts import render

# Create your views here.
