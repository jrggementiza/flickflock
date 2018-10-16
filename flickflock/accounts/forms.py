from django import forms
from django.forms import ModelForm

from .models import Person #, Group
from django.contrib.sites.models import Site
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
        }))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username@example.com',
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
        }))

    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username', 'email', 'password1', 'password2')


class GroupCreationForm(ModelForm):

    class Meta():
        model = Site
        fields = ('name',)
