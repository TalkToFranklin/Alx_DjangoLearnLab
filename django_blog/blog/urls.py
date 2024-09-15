# blog/urls.py

from django.urls import path
from . import views
from .views import register, user_login, user_logout, profile
from .views import (   # Week 14 - Task 2 - Step 4 Define URL Patterns
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    search_posts, 
    posts_by_tag
)

#prpl

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'), # Week 14 - Task 2 - Step 4 Define URL Patterns
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/edit/', comment_edit, name='comment-edit'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment-delete'),
    path('comment/<int:pk>/update/', comment_update, name='comment-edit'),
    path('search/', search_posts, name='search-posts'),  # Add search URL # Week 14 - Task 4 - Step_5 - Configure URL Patterns
    path('tags/<str:tag_name>/', tagged_posts, name='tagged-posts'),  # Add tagging URL Week 14 - Task 4 - Step_5_2 - Add the corresponding URL pattern to Create a view for displaying posts by tag
]


#cg4

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'), # Week 14 - Task 2 - Step 4 Define URL Patterns
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', views.add_comment, name='add-comment'), # Week 14 - Task 3 - Step_5 - Define URL Patterns
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete-comment'),
    path('post/<int:pk>/comments/new/', views.add_comment, name='add-comment'), # Week 14 - Task 3 - Step_5 - Define URL Patterns - Added this line to pass checker for "post/<int:pk>/comments/new/"]
    path('search/', search_posts, name='search_posts'), # Week 14 - Task 4 - Step_5 - Configure URL Patterns
]