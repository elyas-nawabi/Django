from django.db import models


# Create your models here.
class User(models.Model):
    def __str__(self):
         return self.username
    url = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)    
    groups = models.CharField(max_length=100)
class Group(models.Model):
    def __str__(self):
         return self.name
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
