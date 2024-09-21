# Week 15 - Task 2 - step 4_2 - Define URL Patterns for viewing notifications

from django.urls import path
from .views import NotificationListView, MarkNotificationsAsReadView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/mark-as-read/', MarkNotificationsAsReadView.as_view(), name='mark-as-read'),
]