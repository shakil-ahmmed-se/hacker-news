from django.db import models

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    url = models.URLField()
    score = models.IntegerField()
    time = models.DateTimeField()

