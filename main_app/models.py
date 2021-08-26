from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Alumnus(models.Model):
    github = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.TextField(max_length=200)
    lookingfor = models.TextField(max_length=400)
    repo = models.TextField(max_length=150)
    completed = models.BooleanField(default=False)
    alumnus = models.ForeignKey(Alumnus, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Photo(models.Model):
    url = models.CharField(max_length=250)
    alumnus = models.OneToOneField(Alumnus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for alumnus_id: {self.alumnus_id} @{self.url}"