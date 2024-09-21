'''
from django.shortcuts import render

# Create your views here.
'''

# Week 15 - Task 1 - step 3 - Create Views for CRUD Operations Using Django REST Framework’s viewsets

User = get_user_model() # Week 15 - Task 2 - step 3 - Create Views for CRUD Operations Using Django REST Framework’s viewsets

from rest_framework import viewsets, permissions, filters, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend # Week 15 - Task 1 - step 5_2 - Add filtering capabilities to the PostViewSet
from rest_framework.decorators import api_view, permission_classes # Week 15 - Task 2 - step 3 - Implement the Feed Functionality
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import User
from django.contrib.auth import get_user_model # Week 15 - Task 2 - step 3  - Implement the Feed Functionality - ppty 3

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [filters.SearchFilter] # Week 15 - Task 1 - step 5_2 - Add filtering capabilities to the PostViewSet
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Week 15 - Task 2 - step 3 - Implement the Feed Functionality

# cg4

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    # Add serialization for posts if necessary
    post_data = [{'title': post.title, 'content': post.content, 'author': post.author.username} for post in posts]
    return Response(post_data, status=status.HTTP_200_OK)

# ppty

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Get the current user - cgpt 4
        user = self.request.user
        # Get all users that the current user follows
        following_users = user.following.all()
        # Filter posts where the author is in the list of followed users and order by created_at
        return Post.objects.filter(author__in=following_users).order_by('-created_at')