from django.urls import path
from . import views

#Define um nome para evitar namespace C.
app_name = 'tasks'

urlpatterns = [
    path("", views.index, name="index"),
    path("addTask", views.addTask, name="addTask")
]