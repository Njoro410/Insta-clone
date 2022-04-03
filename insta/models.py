from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics',default = 'avatar.png')
    bio = models.TextField(max_length=100)
    
    def __str__(self):
        return f'{self.user.username} Profile'