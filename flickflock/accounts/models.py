import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.conf import settings


class Person(AbstractUser):
    # TODO: Profile Photo
    bio = models.CharField(max_length=120)

    def __str__(self):
        return self.username


class Group(Site):
    # TODO: Group Logo
    # TODO: Group Password
    group_id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Membership',
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # TODO: Ranks instead of can_invite; Admin, Mod, Member
    can_invite = models.BooleanField(default=False)
    # TODO: Join Date


class Invite(models.Model):
    email = models.EmailField(unique=True, verbose_name='e-mail address')
    invite_date = models.DateTimeField(auto_now_add=True)
    # TODO: Generate Invite Link
