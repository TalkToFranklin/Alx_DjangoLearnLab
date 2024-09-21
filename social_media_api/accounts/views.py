'''
from django.shortcuts import render

# Create your views here.
'''

# Week 15 - Task 0 - step 2_4/5 - User Registration and Token Authentication </> Create Views for Registration and Login

# accounts/views.py _ core ppty

from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import CustomUser, User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes # Week 15 - Task 2 - step 2 - Create API Endpoints for Managing Follows
from django.shortcuts import get_object_or_404

CustomUser = get_user_model() # cg4

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow any user to register - ppty

    def create(self, request, *args, **kwargs): # cg4
        response = super().create(request, *args, **kwargs)
        user = response.data
        token, created = Token.objects.get_or_create(user=self.request.user)
        return Response({'user': user, 'token': token.key})

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = CustomUser.objects.get(username=username)
                if user.check_password(password):
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key})
                else:
                    return Response({'error': 'Invalid credentials'}, status=400)
            except CustomUser.DoesNotExist:
                return Response({'error': 'Invalid credentials'}, status=400)
        return Response(serializer.errors, status=400)

class ProfileView(generics.RetrieveUpdateAPIView): # cg4
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# Week 15 - Task 2 - step 2 - Create API Endpoints for Managing Follows

#cg4 -- OLD didn't pass checker

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    if request.user != target_user:
        request.user.following.add(target_user)
        return Response({"message": "Successfully followed"}, status=status.HTTP_200_OK)
    return Response({"error": "Cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.following.remove(target_user)
    return Response({"message": "Successfully unfollowed"}, status=status.HTTP_200_OK)

# Week 15 - Task 2 - step 2 - Create API Endpoints for Managing Follows

# cg4 - NEW - should pass checker

# Follow User API
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if request.user != target_user:
            request.user.following.add(target_user)
            return Response({"message": "Successfully followed"}, status=status.HTTP_200_OK)
        return Response({"error": "Cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

# Unfollow User API
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        request.user.following.remove(target_user)
        return Response({"message": "Successfully unfollowed"}, status=status.HTTP_200_OK)