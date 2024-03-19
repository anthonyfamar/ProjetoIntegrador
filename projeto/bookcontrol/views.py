from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse
from .models import Aluno, Prof, Livro, Emprestimo, Reserva, Devolucao

def sucesso(resquest):
    return render(resquest, 'sucesso.html')

def index(request):
    return HttpResponseRedirect('/pagina_inicial')


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
    if request.method == 'GET':
        return render(request, 'cadastro_prof.html')
    elif request.method == 'POST':
        nome_completo = request.POST['nomeCompleto']
        data_nascimento = request.POST['dataNascimento']
        email = request.POST['email']
        disciplina = request.POST['disciplina']
        turno = request.POST['turno']
        prof = Prof()
        prof.nomeCompleto = nome_completo
        prof.dataNascimento = data_nascimento
        prof.email = email
        prof.disciplina = disciplina
        prof.turno = turno
        prof.save()
        return HttpResponseRedirect('/lista_prof')
    else:
        return HttpResponseBadRequest()


def cadastro_livro(request):
    if request.method == 'GET':
        return render(request, 'cadastro_livro.html')
    elif request.method == 'POST':
        titulo = request.POST['titulo']
        quantidade = request.POST['quantidade']
        ##imagem = request.FILES['image']
        editora = request.POST['editora']
        ano_edicao = request.POST['anoEdicao']
        sinopse = request.POST['sinopse']
        livro = Livro()
        livro.titulo = titulo
        livro.quantidade = quantidade
        ##livro.image = imagem
        livro.editora = editora
        livro.anoEdicao = ano_edicao
        livro.sinopse = sinopse
        livro.save()
        return HttpResponseRedirect('/lista_livro')
    else:
        return HttpResponseBadRequest()


def lista_livro(request):
    return render(request, 'lista_livro.html', {
        'livros': Livro.objects.all()
    })



def controle(request):
    if request.method == 'GET':
        return render(request, 'controle.html')
    elif request.method == 'POST':
        if 'submit_emprestimo' in request.POST:
            titulo = request.POST['titulo']
            nome_completo = request.POST['nomeCompleto']
            data_emprestimo = request.POST['dataEmprestimo']
            previsao_devolucao = request.POST['dataPrevistaDevolucao']
            serie_turma = request.POST['serieturma']
            turno = request.POST['turno']
            emprestimo = Emprestimo()
            emprestimo.titulo = titulo
            emprestimo.nomeCompleto = nome_completo
            emprestimo.dataEmprestimo = data_emprestimo
            emprestimo.dataPrevistaDevolucao = previsao_devolucao
            emprestimo.serieturma = serie_turma
            emprestimo.turno = turno
            emprestimo.save()
            
        elif 'submit_reserva' in request.POST:
            titulo = request.POST['titulo']
            nome_completo = request.POST['nomeCompleto']
            serie_turma = request.POST['serieturma']
            turno = request.POST['turno']
            reserva = Reserva()
            reserva.titulo = titulo
            reserva.nomeCompleto = nome_completo
            reserva.serieturma = serie_turma
            reserva.turno = turno
            reserva.save()         
            
        elif 'submit_devolucao' in request.POST:
            titulo = request.POST['titulo']
            nome_completo = request.POST['nomeCompleto']
            data_devolucao = request.POST['dataDevolucao']
            devolucao = Devolucao()
            devolucao.titulo = titulo
            devolucao.nomeCompleto = nome_completo
            devolucao.dataDevolucao = data_devolucao
            devolucao.save()
        else:
            return HttpResponse('Fomulário desconhecido')
        return HttpResponseRedirect('/pagina_inicial')
    else:
        return HttpResponseBadRequest()
    



def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def lista_aluno(request):
    return render(request, 'lista_aluno.html', {
        'alunos': Aluno.objects.all()
    })

def lista_prof(request):
    return render(request, 'lista_prof.html', {
        'profs': Prof.objects.all()
    })