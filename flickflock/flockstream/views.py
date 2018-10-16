from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import Person
from .models import Photo
from .forms import UploadPhotoForm


@login_required(login_url='accounts/login/')
def index(request):
    current_user = request.user
    if current_user.group is None:
        redirect_url = 'accounts/groups'
        return redirect(redirect_url)
    photos = Photo.objects.filter(published_by__group=current_user.group).filter(is_public=True)    
    if request.method == "POST":
        photo_form = UploadPhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            # save directly to model form
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
    return render(request, 'flockstream/index.html', {
        'current_user': current_user,
        'form': photo_form,
        'photos': photos,
        })
