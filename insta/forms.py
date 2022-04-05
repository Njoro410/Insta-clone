from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Comments, Post, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('profile',)
        fields = ('image','name','caption')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        
        fields = ('content',)
        
# class UpdateUserForm(forms.ModelForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ['username','email']
        
# class UpdateProfileForm(forms.ModelForm):   
#     class Meta:
#         model = Profile
#         fields = ['profile_pic']