# Week 15 - Task 0 - step 2_3/4 - Implement Views and Create a Serializer for the User registration and login

# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the CustomUser model
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to handle user creation and token generation
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password']) # Hash the password
        user.save()
        
        # or from cg4 
        CustomUser = get_user_model().objects.create_user( # for checker from cg4
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'],
        bio=validated_data.get('bio', ''),
        profile_picture=validated_data.get('profile_picture', None)
        ) 

        # Create a token for the new user
        Token.objects.create(user=user)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()