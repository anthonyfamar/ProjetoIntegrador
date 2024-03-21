from django.db import models

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nomeCompleto = models.CharField(max_length=200)
    dataNascimento = models.DateField()
    email = models.EmailField()
    serieturma = models.CharField(max_length=50)
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])

class Prof(models.Model):
    id = models.AutoField(primary_key=True)
    nomeCompleto = models.CharField(max_length=200)
    dataNascimento = models.DateField()
    email = models.EmailField()
    disciplina = models.CharField(max_length=50)
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])

class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    #image = models.ImageField(upload_to='images/')
    autor = models.CharField(max_length=200)
    editora = models.CharField(max_length=200)
    anoEdicao = models.IntegerField()
    sinopse = models.TextField()

class Emprestimo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    nomeCompleto = models.CharField(max_length=200)
    dataEmprestimo = models.DateField()
    dataPrevistaDevolucao = models.DateField()
    serieturma = models.CharField(max_length=50)
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    nomeCompleto = models.CharField(max_length=200)
    serieturma = models.CharField(max_length=50)
    turno = models.IntegerField(choices=[(1, 'Matutino'), (2, 'Vespertino'), (3, 'Noturno')])   

class Devolucao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    nomeCompleto = models.CharField(max_length=200)
    dataDevolucao = models.DateField()
