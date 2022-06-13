from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    favorite_food = models.CharField(max_length=200)
