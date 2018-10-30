from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, GroupCreationForm, GroupJoinForm
from .models import Person, Group, Membership


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
    return render(request, 'accounts/groups.html', {})


@login_required
def groups_create(request):
    current_user = request.user
    if request.method == 'POST':
        group_form = GroupCreationForm(request.POST, request.FILES)
        # TODO: if group already created invalid
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.name = group_form.cleaned_data.get('name')
            group.domain = str(group.name + '.' + 'example.com')
            group.save()
            new_member = Membership(person=current_user, group=group)
            new_member.save()
            return redirect('/')
    else:
        group_form = GroupCreationForm()
    context = {
        'group_form': group_form,
        'current_user': current_user,
    }
    return render(request, 'accounts/groups_create.html', context)


# if it exists, get the group instance of the group name
# get the model instance of the current_user
# assign the current_user to group via membership
@login_required
def groups_join(request):
    current_user = request.user
    if request.method == 'POST':
        membership_form = GroupJoinForm(request.POST, request.FILES)
        if membership_form.is_valid():
            group = membership_form.save(commit=False)
            # TODO: check if group exists. if not, create group instead?
            # TODO: add group password
            group_to_join = Group.objects.get(name=group.name)
            new_member = Membership(person=current_user, group=group_to_join)
            new_member.save()
            return redirect('/')
    else:
        membership_form = GroupJoinForm()
    context = {
        'membership_form': membership_form,
        'current_user': current_user,
    }
    return render(request, 'accounts/groups_join.html', context)


# TODO: def group_invite
# invite model
# group admin can invite
# email of person to invite
# invite code, so some form of hash link
# on click, reroutes to sign up page
# auto joins to group invited