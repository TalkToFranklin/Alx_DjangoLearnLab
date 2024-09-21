# Week 15 - Task 1 - step 4_1 - Configure URL Routing

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('', PostViewSet.as_view({'get': 'list'}), name='post-list'), # Week 15 - Task 2 - step 4_1 - Define URL Patterns for New Features in accounts app
    path('feed/', FeedView.as_view(), name='feed'),  # Add feed route here
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'), # Week 15 - Task 3 - step 4_1 -  Define URL Patterns for liking and unliking posts
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'), # " "
]
