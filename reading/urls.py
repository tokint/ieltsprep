from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:file_name>', views.read_book, name='read_book'),
]
