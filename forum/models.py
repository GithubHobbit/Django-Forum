from django.db import models
from accounts.models import CustomUser

class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Message(models.Model):
    text = models.TextField(max_length=5000)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

# Create your models here.
