from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from .models import Aluno


def cadastro_aluno(request):
    if request.method == 'GET':
        return render(request, 'cadastro_aluno.html')
    elif request.method == 'POST':
        nome_completo = request.POST['nomeCompleto']
        data_nascimento = request.POST['dataNascimento']
        email = request.POST['email']
        serie_turma = request.POST['serieturma']
        turno = request.POST['turno']
        aluno = Aluno()
        aluno.nomeCompleto = nome_completo
        aluno.dataNascimento = data_nascimento
        aluno.email = email
        aluno.serieturma = serie_turma
        aluno.turno = turno
        aluno.save()
        return HttpResponseRedirect('/lista_aluno')
    else:
        return HttpResponseBadRequest()
    
def cadastro_prof(request):
    return render(request, 'cadastro_prof.html')

def cadastro_livro(request):
    return render(request, 'cadastro_livro.html')

def lista_livro(request):
    return render(request, 'lista_livro.html')

def controle(request):
    return render(request, 'controle.html')

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def lista_aluno(request):
    return render(request, 'lista_aluno.html')

def lista_prof(request):
    return render(request, 'lista_prof.html')