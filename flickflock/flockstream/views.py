from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Photo
from .forms import UploadPhotoForm

from accounts.models import CustomUser, Group, Membership

from itertools import chain
from operator import attrgetter


@login_required
def index(request):
    # if not logged in
    # redirect to splash page

    # if current_user not in group
    #   redirect to group/create
    # else get current group of user

    current_user = request.user

    # gets "current group id" of the "group" the current user" is in
    current_group = Group.objects.filter(group_members=current_user).values_list('id', flat=True)
    print(current_group)

    # gets members of "current group" the "current user" is in
    current_group_members = CustomUser.objects.filter(group__in=current_group)
    print(current_group_members)

    # gets photos of the "current group's members" that are "public"
    photos_by_current_group_members = Photo.objects.filter(published_by__in=current_group_members).filter(is_public=True)
    print(photos_by_current_group_members)

    photos = photos_by_current_group_members

    groups = Group.objects.filter(group_members=current_user).values_list('group_name', flat=True)


    # q1 = CustomUser.objects.values_list('username', 'group', 'photo')
    # q2 = Membership.objects.values_list('group_name', 'group_user')
    # q3 = Group.objects.values_list('group_name', 'group_members')

    # print('CustomerUser Query')
    # for q in q1:
    #     print(f'Username: {q[0]} - Group: {q[1]} - Photo: {q[2]}')

    # print('Membership Query')
    # for q in q2:
    #     print(f'group_name: {q[0]} - group_user: {q[1]}')

    # print('Group Query')
    # for q in q3:
    #     print(f'group_name: {q[0]} - group_members: {q[1]}')

    # with the current user's group
    # get all the members of the group
    # where the photos are public

    
    if request.method == "POST":
        photo_form = UploadPhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo = photo_form.cleaned_data.get('photo')
            title = photo_form.cleaned_data.get('title')
            published_by = current_user
            photo = Photo(photo=photo, title=title, published_by=published_by)
            photo.save()
            # add prompt that upload successful
        else:
            # add prompt that upload unsuccesssful
            pass
    else:
        photo_form = UploadPhotoForm()
    # photos = Photo.objects.filter(is_public=True)

    groups
    return render(request, 'flockstream/index.html', {
        'current_user': current_user,
        'form': photo_form,
        'photos': photos,
        'groups': groups,
        })
