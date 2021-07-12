from django.db import models

# Create your models here
class PostModel(models.Model):
    subject = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    content = models.TextField()
