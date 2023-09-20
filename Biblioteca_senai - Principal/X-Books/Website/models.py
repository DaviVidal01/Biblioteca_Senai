from django.db import models
from datetime import datetime

# Create your models here.
CATEGORIAS = (
    ('1','Aventura'),
    ('2','Terror'),
    ('3','Romance'),
    ('4','Poesia'),
    ('5','Fantasia'),
    ('6','Biografia'),
    ('7','Autobiografia'),
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


class Livros(models.Model):
    titulo = models.CharField(default='', max_length= 30)
    autor = models.CharField(default='', max_length= 30)
    image = models.ImageField(upload_to= './images')
    genero = models.CharField(max_length= 20, choices=CATEGORIAS,  default ='1') 
    status = models.CharField(max_length = 20, choices = STATUS, default = '1')

class Usuario(models.Model):
    titulo = models.CharField(default='', max_length= 30)
    email = models.EmailField(default='', max_length= 40)
    cpf = models.CharField(default='', max_length= 11)
    telefone = models.CharField(default='4002-8922', max_length=14)
    senha = models.CharField(default='', max_length= 40)
    endereco = models.TextField(default='', max_length=255)
    ficha = models.CharField(max_length= 20, choices= FICHA, default='1')

class Registro(models.Model):
    data_Ret = models.DateTimeField(default=datetime.now())
    data_Dev = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=20, choices= STATUS2, default= '1')