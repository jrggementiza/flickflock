from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import CustomUser, Group

from django import forms


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
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
        }))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
        }))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class GroupCreationForm(ModelForm):

    class Meta():
        model = Group
        fields = ('group_name',)


    def clean_group_name(self):
        group_name = self.cleaned_data.get('group_name')
        is_exists = Group.objects.filter(group_name=group_name).exists()
        if is_exists:
            # needs prompt
            print('already exists in db!')
            raise forms.ValidationError("group name already exists!")
        return group_name


    def clean(self):
        data = self.cleaned_data
        # use your logic for non field errors
        return data
