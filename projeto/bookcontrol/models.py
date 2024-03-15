from django.db import models

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nomeCompleto = models.TextField()
    dataNascimento = models.DateField()
    email = models.EmailField()
    serieturma = models.CharField(max_length=200)
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])

class Prof(models.Model):
    id = models.AutoField(primary_key=True)
    nomeCompleto = models.TextField()
    dataNascimento = models.DateField()
    email = models.EmailField()
    disciplina = models.TextField()
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    quantidade = models.IntegerField()
    #image = models.ImageField(upload_to='images/')
    autor = models.TextField()
    editora = models.TextField()
    anoEdicao = models.IntegerField()
    sinopse = models.TextField()

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    nomeCompleto = models.TextField()
    dataEmprestimo = models.DateField()
    dataPrevistaDevolucao = models.DateField()
    serieturma = models.CharField(max_length=200)
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    nomeCompleto = models.TextField()

class Devolucao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    nomeCompleto = models.TextField()
    dataDevolucao = models.DateField()
