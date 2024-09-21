# Week 15 - Task 0 - step 3_1 - Set up URL routes for registration, login, and profile management:

# accounts/urls.py
from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'), # Week 15 - Task 2 - step 4_1 - Define URL Patterns for New Features in accounts app
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]
