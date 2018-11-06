import datetime
import secrets

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.mail import send_mail


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
    invite_link = models.CharField(max_length=27, primary_key=True)
    email = models.EmailField(unique=True, verbose_name='e-mail address')
    invite_date = models.DateTimeField(auto_now_add=True)
    group_to_join = models.ForeignKey(Group, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activated_link = models.BooleanField(default=False)
    
    def generate_invite_token(self):
        token = secrets.token_urlsafe(20)
        self.invite_link = token
        return self.invite_link

    def send(self):
        pass
        # subject = 'Join us!'
        # message = 'Hey there! {self.invited_by} has invited you to join the group {self.group_to_join}! click the link and lets go! www.flickflock.com/groups/join/{self.invite_link}'
        # from_email = smtp server?
        # recipient = self.email
        

        # link = 'http://%s/friend/accept/%s/' % (settings.SITE_HOST, self.code)
        # template = get_template('invitation_email.txt')
    
        # message = template.render(context)
    
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email])
        # send_email(subject, message, from_email, recipient)
    
        
         
        # Hi {email}!

        # {invited_by} has invited you to join {group_to_join}!
        # Click the link and see you there!
        # http://{{ domain }}/groups/join/{% url 'activate' uidb64=uid invite_link=invite_link %}   

        # [] setup the smtp (test in local dev?)

         


