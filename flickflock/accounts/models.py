from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.conf import settings


class Person(AbstractUser):
    group = models.ForeignKey(Site, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.username
