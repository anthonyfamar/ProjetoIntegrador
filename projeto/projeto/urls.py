
from django.contrib import admin
from django.urls import path
from bookcontrol import views

urlpatterns = [
    path('', views.index),
    path('cadastro_aluno', views.cadastro_aluno),
    path('cadastro_prof', views.cadastro_prof),
    path('cadastro_livro', views.cadastro_livro),
    path('lista_livro', views.lista_livro),
    path('controle', views.controle),
    path('pagina_inicial', views.pagina_inicial),
    path('lista_aluno', views.lista_aluno),
    path('lista_prof', views.lista_prof)
]
