'''from django.shortcuts import render

# Create your views here.
'''

# Week 15 - Task 3 - step 3_1 - Create a view to fetch notifications for the authenticated user

from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.filter(unread=True)


# Week 15 - Task 3 - step 3_2 - Create a view to Mark Notifications as Read - cg4

class MarkNotificationsAsReadView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        notifications = request.user.notifications.filter(unread=True)
        notifications.update(unread=False)
        return Response({'message': 'Notifications marked as read'}, status=status.HTTP_200_OK)
