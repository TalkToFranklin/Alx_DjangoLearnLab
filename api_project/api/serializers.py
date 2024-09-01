# Week 12 - task 2 (Create the Serializer) api/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', '__all__']  # Include all fields you want to serialize 