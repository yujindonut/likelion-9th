from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=200)
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followings'
    )
