from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, GroupCreationForm
from .models import Group, Membership


def accounts(request):
    # sign up
    # login
    # do splash.html
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
                redirect_url = request.GET.get('/')
                return redirect(redirect_url)
            else:
                message.error(request, 'Bad username or password')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def groups(request):
    # create a group?
    # join a group? request invite
    pass


@login_required
def group_create(request):
    current_user = request.user
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)

        # if group already created invalid
        if form.is_valid():
            print(form.cleaned_data)
            # get the pieces for membership
            group_member = current_user
            group_name = form.cleaned_data.get('group_name')

            # create a group
            group = Group.objects.create(group_name=group_name)

            # create + save membership
            membership = Membership(group_user=current_user, group_name=group)
            membership.save()

            return redirect('/')
    else:
        form = GroupCreationForm()
    return render(request, 'accounts/groupcreate.html', {'form': form, 'current_user': current_user})


@login_required
def group_join(request):
    pass
