from django.shortcuts import render

def cadastro_aluno(request):
    return render(request, 'cadastro_aluno.html')

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