from django.shortcuts import render, HttpResponse
from .forms import ImageForm
from .analyzer import colour_analyzer

import asyncio
from django.views.generic.edit import CreateView


def home(request):
    return render(request, './analyzer/home.html')


class UploadFileView(CreateView):
    form_class = ImageForm
    template_name = './analyzer/upload.html'

    def form_valid(self, form):
        instance = form.save()
        image_path = instance.image.path
        res = asyncio.run(colour_analyzer(image_path))

        empty_form = ImageForm()

        context = {
            'res': res,
            'form': empty_form,
            'image': instance.image,
        }

        return render(self.request, 'analyzer/upload.html', context)


upload_file_view = UploadFileView.as_view()
