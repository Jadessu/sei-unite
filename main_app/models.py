from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.TextField(max_length=200)
    lookingfor = models.TextField(max_length=400)
    repo = models.TextField(max_length=150)
    completed = models.BooleanField(default=False)
