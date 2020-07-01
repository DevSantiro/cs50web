from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("meuNome", views.meuNome, name="meuNome"),
    path("<str:name>", views.greet, name="greet")
]