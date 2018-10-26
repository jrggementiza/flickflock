from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.sites.models import Site
from .forms import UserRegistrationForm, GroupCreationForm
from .models import Person


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
                redirect_url = '/'
                return redirect(redirect_url)
            else:
                message.error(request, 'Bad username or password')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def groups(request):
    # create a group?
    # join a group? request invite
    return render(request, 'accounts/groups.html', {})


@login_required
def groups_create(request):
    current_user = request.user
    if request.method == 'POST':
        form = GroupCreationForm(request.POST, request.FILES)
        # if group already created invalid
        if form.is_valid():
            group = form.save(commit=False)
            group.name = form.cleaned_data.get('name')
            group.domain = str(group.name + '.' + 'example.com')
            group.save()
            current_user.group = group
            current_user.save()
            return redirect('/')
    else:
        form = GroupCreationForm()
    context = {
        'form': form,
        'current_user': current_user,
    }
    return render(request, 'accounts/groups_create.html', context)


@login_required
def groups_join(request):
    current_user = request.user
    if request.method == 'POST':
        # add group validation / password so not everyone can join
        form = GroupCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            name = form.cleaned_data.get('name')
            group = Site.objects.get(name=name)
            current_user.group = group
            current_user.save()
            return redirect('/')
    else:
        form = GroupCreationForm()
    context = {
        'form': form,
        'current_user': current_user,
    }
    return render(request, 'accounts/groups_join.html', context)
