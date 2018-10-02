from django import forms
from .models import Photo


class UploadPhotoForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'form-control-file',
        }))
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'title',
        }))
    # is_public = forms.ChoiceField(widget=forms.CheckboxInput(
    #     attrs={
    #         'type': 'checkbox',
    #         'class': 'custom-control-input',
    #         'id': 'is_public_check',
    #     }))

    class Meta:
        model = Photo
        fields = ('photo', 'title', 'is_public')
