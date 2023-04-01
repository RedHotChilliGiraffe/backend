import uuid
from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models

from red_hot_chilli_giraffe.accounts.managers import UserManager


# Create your models here.
class User(AbstractUser):
    """
    Custom user model with extra data: phone, company name and nip
    """
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD: str = "username"
    REQUIRED_FIELDS: List[str] = []
    POPULATE_FROM = "default_slug"

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def default_slug(self):
        return uuid.uuid4().hex

    def save(self, *args, **kwargs):
        """
        Set random username based on UUID if is empty.
        """
        super().save(*args, **kwargs)
