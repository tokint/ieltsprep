from django.urls import path

from . import views

app_name = 'speakp2app'
urlpatterns = [
    path('', views.index, name='index'),
]
