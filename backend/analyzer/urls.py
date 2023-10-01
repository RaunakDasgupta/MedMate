from django.urls import path
from .views import upload_file_view

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload/', upload_file_view, name='upload'),
]
