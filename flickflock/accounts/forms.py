from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from .models import CustomUser, FlockGroup


class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class FlockCreationForm(ModelForm):

    class Meta():
        model = FlockGroup
        fields = ('group_name',)
