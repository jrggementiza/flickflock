from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .forms import UserRegistrationForm, FlockCreationForm
from .models import FlockGroup


def accounts(request):
    # sign up
    # login
    pass


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', '/')
                return redirect(redirect_url)
            else:
                message.error(request, 'Bad username or password')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def flock_register(request):
    # create a group?
    # join a group? request invite
    pass


def flock_create(request):
    # if user is not logged in if request.user.is_authenticated():
        # redirect_url = request.GET.get('accounts/login')
        # return redirect(redirect_url)
    if request.method == 'POST':
        form = FlockCreationForm(request.POST)
        if form.is_valid():
            form.save()
            group_name = form.cleaned_data.get('group_name')
            current_user = request.user
            flock_group = FlockGroup(group_name=group_name, group_admin=current_user)
            flock_group.save()
            redirect_url = request.GET.get('next', '/')
            return redirect(redirect_url)
    else:
        form = FlockCreationForm()
    return render(request, 'accounts/flockcreate.html', {'form': form})
