from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class OwnStory(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    story = models.TextField(max_length=450)
    cover = models.TextField(max_length=150, default="null")
    # published = models.IntegerField()
    published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('ownstory')
    
class StoryTitle(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    cover = models.TextField(max_length=150, default="null")
    
    def __str__(self):
        return self.title
    
    
    
class Meta:
        ordering = ['-date']