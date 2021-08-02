from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Extend default user class of Django"""

    about_us = models.CharField(max_length=300, null=True, blank=True)
    citation = models.CharField(max_length=150, null=True, blank=True)
