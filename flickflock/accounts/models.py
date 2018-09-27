from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class FlockGroup(models.Model):
    group_name = models.CharField(max_length=100, blank=True, null=True, default='New Group')
    group_admin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE) # this creates a dropdown of all users in db

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')
    def __str__(self):
        return self.group_name


class FlockGroupMember(models.Model):
    flock_group_member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='membership')
    flock_group = models.ForeignKey(FlockGroup, on_delete=models.CASCADE, related_name='membership')

    def __str__(self):
        return f'{flock_group_member} is in {flock_group}'
