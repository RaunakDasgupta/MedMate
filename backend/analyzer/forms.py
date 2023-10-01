from django import forms
from .models import ImageUploadModel


class ImageForm(forms.ModelForm):

    image = forms.ImageField(
        label='Upload Image',
    )

    class Meta:
        model = ImageUploadModel
        fields = ['image']
