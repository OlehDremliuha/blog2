from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='postUploads')
    title = models.TextField(max_length=100)
    text = models.TextField()



class Comment(models.Model):

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()


class Profile(models.Model):

    userId = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default="userAvatars/user.png", upload_to='userAvatars')
    bio = models.TextField()

    def __str__(self):
        return self.userId.username

