from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.fields import CharField, DateTimeField

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')
