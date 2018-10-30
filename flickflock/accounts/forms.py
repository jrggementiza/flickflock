from django import forms
from django.forms import ModelForm

from .models import Person, Group, Membership
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
            'label': 'Password',
            'placeholder': 'password',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
        }))

    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username', 'email', 'password1',)


class GroupCreationForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'group name',
        }))

    class Meta():
        model = Group
        fields = ('name',)


class GroupJoinForm(ModelForm):
    # TODO: group password

    class Meta():
        model = Group
        fields = ('name',)
