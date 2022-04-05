from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from django.utils import timezone
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pic = models.ImageField(
    #     upload_to='profile_pics', default='profile_pics/avatar.png')
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=100)


    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    # image = models.ImageField(upload_to='posts')
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.PositiveIntegerField(null=True)
    # dislikes = models.PositiveIntegerField(null = True)
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-posted_on']

    def get_absolute_url(self):

        return reverse("post-detail", kwargs={"pk": self.pk})


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    posted_on = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    

    def __str__(self):
        return f'{self.user.id} Comments'


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id.id} UserFollowing'


