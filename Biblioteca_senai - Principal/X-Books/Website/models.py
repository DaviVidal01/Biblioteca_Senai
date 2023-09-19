from django.db import models

# Create your models here.
NEWES = (
    ('1', 'None'),
    ('2', 'New')
)
DESC = (
    ('1', 'None'),
    ('2', '-10%'),
    ('3', '-30%'),
)

class NewProdutos(models.Model):
    title = models.CharField(default='', max_length= 30)
    image = models.ImageField(upload_to= './images')
    precoD = models.DecimalField(default=000.00, max_digits=5, decimal_places=2)
    precoA = models.DecimalField(default=000.00, max_digits=5, decimal_places=2)
    new = models.CharField(max_length = 20, choices = NEWES, default = '1')
    desconto = models.CharField(max_length = 20, choices = DESC, default = '1')

class Categorias(models.Model):
    nome = models.CharField(default='', max_length= 30)