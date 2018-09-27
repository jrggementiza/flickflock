from django.shortcuts import render

from .models import Photo
from .forms import UploadPhotoForm

#login required
def index(request):
    # get the current group of the user
    # display photos of the users group that is public
    current_user = request.user

    if request.method == "POST":
        photo_form = UploadPhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():          
            photo_form.save()
            # add prompt that upload successful
        else:
            # add prompt that upload unsuccesssful
            pass
    else:
        photo_form = UploadPhotoForm()
    photos = Photo.objects.all()


    return render(request, 'flockstream/index.html', {
        'current_user': current_user,
        'form': photo_form,
        'photos': photos
        })
