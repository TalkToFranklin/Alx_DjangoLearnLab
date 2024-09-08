# Week 13 - step 4

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model. Serializes all fields of the Book model 
    and includes custom validation to ensure the publication year is not in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author'] # Include all fields

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model. Serializes the name field and includes a nested BookSerializer 
    to dynamically serialize related books.
    """
    books = BookSerializer(many=True, read_only=True) # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books'] # Include author's name and related books

# Week 13 - Task 1 - step 3

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic before saving the book
        print("Creating a new book...")
        serializer.save()


# Week 13 - Task 0 - step 5

"""
This file contains serializers for the API app.
BookSerializer serializes book data including custom validation for the publication year.
AuthorSerializer serializes author data along with nested books using the BookSerializer.
"""
