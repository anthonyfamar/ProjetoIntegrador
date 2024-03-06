from django.shortcuts import render

def cadastro_aluno(request):
    return render(request, 'cadastro_aluno.html')

def cadastro_prof(request):
    return render(request, 'cadastro_prof.html')

def cadastro_livro(request):
    return render(request, 'cadastro_livro.html')