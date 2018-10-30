from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.conf import settings

# class Photo
# FK Person


class Person(AbstractUser):
    # profile photo
    bio = models.CharField(max_length=120)
    
    def __str__(self):
        return self.username


class Group(Site):
    # name = 'alpha'
    # domain = 'alpha.example.com'
    # group photo / banner = star
    # temporarily add group password = 'qwerty'
    # group owner = current.user
    group_id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Membership',
    )

    def __str__(self):
        return self.name


## model is Entry.blog fk Blog
# Entry object
# Blog object
# Entry.blog = Blog object

## model is Membership.person fk Person, Membership.group fk Group
# Membership object
# Person Object - get current user from Person model
# Group Object - get group name from the input if it exists
# Membership.person = Person Object
# Membership.group = Group Object

# prevent membership duplication

class Membership(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # has been invited
    # invite date
    # join date
