
from django.contrib import admin
from django.urls import path
from bookcontrol import views

urlpatterns = [
    path('cadastro_aluno', views.cadastro_aluno),
    path('cadastro_prof', views.cadastro_prof),
    path('cadastro_livro', views.cadastro_livro),
    path('lista_livro', views.lista_livro)
]
