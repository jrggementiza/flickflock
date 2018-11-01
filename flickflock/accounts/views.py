from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, GroupCreationForm, GroupJoinForm, GroupInviteForm
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
            new_member = Membership(person=current_user, group=group, can_invite=True)
            new_member.save()
            return redirect('/')
    else:
        group_form = GroupCreationForm()
    context = {
        'group_form': group_form,
        'current_user': current_user,
    }
    return render(request, 'accounts/groups_create.html', context)


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

# the email of the user you want to invite

# the group (that you can invite in) that you want the person (who owns)
# the email address) to join
# a dropdown of places where you can invite people in?
@login_required
def groups_invite(request):
    current_user = request.user
    groups_with_invite_access = Membership.objects.filter(person=current_user).filter(can_invite=True)
    if not groups_with_invite_access:
        # TODO: prompt that you're not allowed to invite people
        print('you cant seem to invite people into any groups')
        return redirect('/')
    if request.method == 'POST':
        form = GroupInviteForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.save(commit=False)
            # TODO: prompt if this email has already been invited
            print(f'{email} has been invited by {current_user} to join {groups_with_invite_access.group }')
            return redirect('/')
    else:
        form = GroupInviteForm()
    context = {
        'form': form,
        'groups_with_invite_access': groups_with_invite_access,
    }
    return render(request, 'accounts/groups_invite.html', context)
