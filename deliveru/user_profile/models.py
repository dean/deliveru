from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    '''Extension of the User class provided by Django.'''
    name = models.TextField()
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, unique=True)
