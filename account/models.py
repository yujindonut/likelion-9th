from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=200)
    age = models.CharField(max_length=30)
    partner = models.CharField(max_length=30)