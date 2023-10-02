from django.db import models
from datetime import datetime

# Create your models here.
#CATEGORIAS = (
#    ('1','Aventura'),
#    ('2','Terror'),
#    ('3','Romance'),
#    ('4','Poesia'),
#    ('5','Fantasia'),
#    ('6','Biografia'),
#    ('7','Drama'),
#)
DESTAQUE= (
    ('1','None'),
    ('2','Sim')
)
STATUS = (
    ('1', 'Disponível'),
    ('2', 'Alugado')
)
FICHA = (
    ('1','Limpa'),
    ('2','Punição')
)
STATUS2 = (
    ('1','Pendente'),
    ('2','Atrasado'),
    ('3','Entregue')
)

class Genero(models.Model):
    nome = models.CharField(max_length = 30)

    def __str__(self):
        return self.nome


class Livros(models.Model):
    titulo = models.CharField(max_length= 30)
    autor = models.CharField(max_length= 30)
    image = models.ImageField(upload_to= './images')
    genero = models.ForeignKey(Genero, on_delete= models.CASCADE) 
    status = models.CharField(max_length = 20, choices = STATUS, default = '1')
    destaque = models.CharField(max_length = 20, choices = DESTAQUE, default = '1')
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length= 40)
    email = models.EmailField(max_length= 40)
    cpf = models.CharField(max_length= 11)
    telefone = models.CharField(default='4002-8922', max_length=14)
    senha = models.CharField(max_length= 40)
    endereco = models.TextField(max_length=255)
    ficha = models.CharField(max_length= 20, choices= FICHA, default='1')

    def __str__(self):
        return self.nome

class Registro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete= models.CASCADE)
    data_Ret = models.DateTimeField(default=datetime.now())
    data_Dev = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=20, choices= STATUS2, default= '1')