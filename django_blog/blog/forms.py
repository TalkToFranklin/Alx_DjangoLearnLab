# Week 14 - Task 1 - Step 1_1 Setup custom registration
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



# Week 14 - Task 2 - Step_2 - Create and Configure Forms

from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget # Week 14 - Task 4 - Step_2 - Modify Post Creation and Update Forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {    # Week 14 - Task 4 - Step_2_2 - Update forms.py to handle tag input
            'tags': TagWidget(), #cg4
            'content': forms.Textarea(attrs={'rows': 4}), #ppty
        }

class CommentForm(forms.ModelForm): # Week 14 - Task 3 - Step_2 Create Comment Forms
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Leave a comment...'}),
        }