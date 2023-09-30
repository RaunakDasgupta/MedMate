from django.shortcuts import render, HttpResponse
from .forms import ImageForm

def UploadFile(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = ImageForm()
    context = {'form':form,}
    return render(request, 'upload.html', context)

# Create your views here.
