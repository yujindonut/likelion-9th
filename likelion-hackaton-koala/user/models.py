from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    birthDay = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    location = models.CharField(max_length=200)