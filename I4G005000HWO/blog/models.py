from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    Tilte = models.CharField(max_length=200)
    Text = models.TextField()
    Author=models.ForeignKey(User, on_delete=models.CASCADE,)
    Created_date=models.DateTimeField()
    Publish_date=models.DateTimeField()


