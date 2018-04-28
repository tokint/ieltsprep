from django.urls import path

from . import views

app_name = 'writep2app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/set_answer/', views.set_answer, name='set_answer'),
    path('<int:answer_id>/del_answer/', views.del_answer, name='del_answer'),
    path('<int:answer_id>/upd_answer/', views.upd_answer, name='upd_answer'),
]
