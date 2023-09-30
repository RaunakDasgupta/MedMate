from django import forms
from .models import ImageUploadModel


class ImageForm(forms.ModelForm):

    image = forms.ImageField(
        label='Upload Image',
        help_text='max. 42 megabytes'
    )

    class Meta:
        model = ImageUploadModel
        fields = ['image']
