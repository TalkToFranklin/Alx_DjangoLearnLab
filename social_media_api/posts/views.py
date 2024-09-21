'''
from django.shortcuts import render

# Create your views here.
'''

# Week 15 - Task 1 - step 3 - Create Views for CRUD Operations Using Django REST Framework’s viewsets

User = get_user_model() # Week 15 - Task 2 - step 3 - Create Views for CRUD Operations Using Django REST Framework’s viewsets

from rest_framework import viewsets, permissions, filters, generics, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend # Week 15 - Task 1 - step 5_2 - Add filtering capabilities to the PostViewSet
from rest_framework.decorators import api_view, permission_classes # Week 15 - Task 2 - step 3 - Implement the Feed Functionality
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import User, Post, Like
from django.contrib.auth import get_user_model # Week 15 - Task 2 - step 3  - Implement the Feed Functionality - ppty 3
from notifications.models import Notification # Week 15 - Task 2 - step 3 - Implement the Feed Functionality

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


# Week 15 - Task 3 - step 2_1 - Implement views to handle liking and unliking posts

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Post, Like
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

User = get_user_model()

class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({'message': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate a notification for the post's author when the post is liked
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked',
            target=post,
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)

# Code already inserted into Class LikePostView
# Week 15 - Task 3 - step 2_2 - Implement views to Generate Notifications for Likes

# Generate a notification for the post's author when the post is liked
def create_like_notification(user, post):
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target=post,
        target_content_type=ContentType.objects.get_for_model(post),
        target_object_id=post.id
    )

generics.get_object_or_404(Post, pk=pk)