from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    real_ip = models.GenericIPAddressField(blank=True, null=True)
