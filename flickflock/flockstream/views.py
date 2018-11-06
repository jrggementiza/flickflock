from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from accounts.models import Person, Group, Membership
from accounts.forms import UserRegistrationForm
from .models import Photo
from .forms import UploadPhotoForm


def index(request, prompt):
    print(prompt)
    current_user = request.user
    if not request.user.is_authenticated:
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
            form = UserRegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'flockstream/splash.html', context)
    else:
        # TODO: render memberships in a toggle to view / not view
        memberships = Membership.objects.all().filter(person=current_user)
        if not memberships:
            redirect_url = 'groups/'
            return redirect(redirect_url)
        # TODO: publish on which groups? ManyToMany Field
        photos = Photo.objects.filter(published_by=current_user).filter(is_public=True).order_by('-published_on')
        if request.method == "POST":
            photo_form = UploadPhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                published_by = current_user
                photo.published_by = published_by
                photo.save()
        else:
            photo_form = UploadPhotoForm()
        context = {
            'current_user': current_user,
            'form': photo_form,
            'memberships': memberships,
            'photos': photos,
        }
        return render(request, 'flockstream/index.html', context)
