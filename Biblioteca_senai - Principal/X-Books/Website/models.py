from django.db import models
from django.utils import datetime
# Create your models here.
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


class Livros(models.Model):
    titulo = models.CharField(default='', max_length= 30)
    autor = models.CharField(default='', max_length= 30)
    image = models.ImageField(upload_to= './images')
    genero = models.CharField(max_length= 20, choices=,  default ='1') 
    status = models.CharField(max_length = 20, choices = STATUS, default = '1')

class Usuario(models.Model):
    titulo = models.CharField(default='', max_length= 30)
    email = models.EmailField(default='', max_length= 40)
    cpf = models.CharField(default='', max_length= 11)
    telefone = models.IntegerField(default='', max_digits= 14)
    senha = models.CharField(default='', max_length= 40)
    endereco = models.TextField(default='', max_length=255)
    ficha = models.CharField(max_length= 20, choices= FICHA, default='1')

class Categorias(models.Model):
    titulo = models.CharField(default='', max_length= 30)

class Registro(models.Model):
    data_Ret = models.DateTimeField(default=datetime.datetime.now())
    data_Dev = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=20, choices= STATUS2, default= '1')