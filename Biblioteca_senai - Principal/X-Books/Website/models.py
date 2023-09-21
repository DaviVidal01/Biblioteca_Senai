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
    ('7','Drama'),
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
<<<<<<< HEAD
    genero = models.CharField(max_length= 20, choices='',  default ='1') 
=======
    genero = models.CharField(max_length= 20, choices=CATEGORIAS,  default ='1') 
>>>>>>> 388d188160f87d5a80f8a45af1f9c3f184a097c1
    status = models.CharField(max_length = 20, choices = STATUS, default = '1')
    ano = models.IntegerField(default=0)

class Usuario(models.Model):
    nome = models.CharField(default='', max_length= 30)
    email = models.EmailField(default='', max_length= 40)
    cpf = models.CharField(default='', max_length= 11)
<<<<<<< HEAD
    telefone = models.CharField(default='', max_digits= 14)
=======
    telefone = models.CharField(default='4002-8922', max_length=14)
>>>>>>> 388d188160f87d5a80f8a45af1f9c3f184a097c1
    senha = models.CharField(default='', max_length= 40)
    endereco = models.TextField(default='', max_length=255)
    ficha = models.CharField(max_length= 20, choices= FICHA, default='1')

class Registro(models.Model):
    data_Ret = models.DateTimeField(default=datetime.now())
    data_Dev = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=20, choices= STATUS2, default= '1')