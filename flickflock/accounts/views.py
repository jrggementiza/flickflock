from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, GroupCreationForm, GroupJoinForm, GroupInviteForm
from .models import Person, Group, Membership, Invite


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
        # TODO: if group already created, prompt group name already taken
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
            # TODO: check if group exists. if not, prompt if they want to create group instead
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


@login_required
def groups_invite(request):
    current_user = request.user
    groups_with_invite_access = Membership.objects.filter(person=current_user).filter(can_invite=True)
    if not groups_with_invite_access:
        # TODO: better prompt that you're not allowed to invite people
        prompt = 'You are not allowed to invite people in the group!'
        return redirect('/')
    if request.method == 'POST':
        form = GroupInviteForm(request.POST, request.FILES)
        if form.is_valid():
            person_to_invite = form.save(commit=False)
            group_name = request.POST['group']
            group_object = Group.objects.get(name=group_name)
            
            person_to_invite.generate_invite_token()
            person_to_invite.group_to_join = group_object
            person_to_invite.invited_by = current_user
            person_to_invite.save()
            person_to_invite.send()
            # TODO: prompt that invite was sent!
            prompt = 'Invite successfully sent to {person_to_invite.email}!'
            return redirect('/')
    else:
        form = GroupInviteForm()
    context = {
        'form': form,
        'groups_with_invite_access': groups_with_invite_access,
    }
    return render(request, 'accounts/groups_invite.html', context)


@login_required
def groups_join_via_email(request, invite_link):
    # TODO: if not logged in or if doesnt have an account, redirects to login / signup. 'next' points back to 'group_join_via_email'
    current_user = request.user
    try:
        invite = Invite.objects.get(invite_link=invite_link, activated_link=False)
    except Invite.DoesNotExist:
        raise Http404("I does not exist")
    invite.activated_link = True
    invite.save()

    group_to_join = invite.group_to_join
    new_member, created = Membership.objects.get_or_create(person=current_user, group=group_to_join)
    if created:
        # TODO: prompt already in the group!, pass the prompt to the index as a popup context
        prompt = '{new_member.person} has ALREADY joined {new_member.group}!'
    else:
        new_member.save()
        # TODO: prompt of successful join
        prompt = '{new_member.person} has joined {new_member.group}!'
    return redirect('/')
