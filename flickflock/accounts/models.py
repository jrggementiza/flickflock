from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

import datetime


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class Group(models.Model):
    group_name = models.CharField(max_length=128)
    group_members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    def __str__(self):
        return self.group_name


class Membership(models.Model):
    group_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return f'{self.group_user} is in {self.group_name}'
