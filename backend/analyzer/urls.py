from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.UploadFile, name='upload'),
]
