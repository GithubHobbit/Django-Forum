from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    realname = models.CharField(max_length=30, blank=True)
    favourite_topics = models.ManyToManyField('forum.Topic')
    email = models.EmailField(blank=True)
    avatar = models.ImageField(upload_to='accounts/images/avatar/', null=True, max_length=255, blank=True)

    def __str__(self):
        return self.username

# Create your models here.
