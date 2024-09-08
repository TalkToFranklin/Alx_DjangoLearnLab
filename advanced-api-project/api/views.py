from django.shortcuts import render

# Create your views here.

# Week 13 - Task 1 - step 1 

# api/views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read for all, create for authenticated users

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read for all, update/delete for authenticated users

""" Above or below prplxty takeover """

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow read access to everyone

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    """
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete books



# Week 13 - Task 2 - Step 1_3 - Integrate Filtering in the View

# api/views.py

from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books with filtering, searching, and ordering capabilities.
    - Filtering: Users can filter by title, author name, and publication year.
    - Searching: Users can search by title and author name.
    - Ordering: Users can order results by title and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [permissions.AllowAny]  # Allow read access to everyone

    # Set up filtering, searching, and ordering
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['title', 'author__name', 'publication_year']  # Fields to filter by
    search_fields = ['title', 'author__name']  # Fields to search
    ordering_fields = ['title', 'publication_year']  # Fields to order by
    ordering = ['title']  # Default ordering

    filters.OrderingFilter
