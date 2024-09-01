# Week 12 - task 2 (Configure URL Patterns)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # URL for the BookList API endpoint
    path('', include(router.urls)), # The API URLs are now determined automatically by the router & Include the router's URLs
]