from django.shortcuts import render
from .models import *
from Website.forms import Loginemail, Loginsenha

# Create your views here.
def index(request):
    form_email = Loginemail,
    form_senha = Loginsenha
    return render(request,"index.html", {"form": form_email,"form": form_senha})
    
def livros(request):
    livros = Livros.objects.all()
    return render(request,"livros.html", {'livros': livros})

def catalogo(request):
    livros = Livros.objects.all()
    return render(request,"catalogo.html", {'livros': livros})

def catalogo2(request):
    livros = Livros.objects.all()
    return render(request,"catalogo-2.html", {'livros': livros})

def FAQs(request):
    return render(request,"FAQs.html")

def funcionario(request):
    usuarios = Usuario.objects.all()
    livros = Livros.objects.all()
    return render(request,"admin.html", {'usuarios': usuarios, 'livros': livros})

def funcionario1(request):
    usuarios = Usuario.objects.all()
    livros = Livros.objects.all()
    return render(request,"admin.html", {'usuarios': usuarios, 'livros': livros})
    
def funcionario2(request):
    usuarios = Usuario.objects.all()
    livros = Livros.objects.all()
    return render(request,"admin.html", {'usuarios': usuarios, 'livros': livros})

def funcionario3(request):
    usuarios = Usuario.objects.all()
    livros = Livros.objects.all()
    return render(request,"admin.html", {'usuarios': usuarios, 'livros': livros})

def descricao(request):
    usuarios = Usuario.objects.all()
    return render(request,"descricao.html", {'usuarios': usuarios})

def cadastro(request):
    usuarios = Usuario.objects.all()
    return render(request,"cadastro.html", {'usuarios': usuarios})

def cadastro_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,"cadastrar_usuario.html", {'usuarios': usuarios})   

def cadastro_book(request):
    usuarios = Usuario.objects.all()
    return render(request,"cadastrar_livros.html", {'usuarios': usuarios})   

def consulta_book(request):
    usuarios = Usuario.objects.all()
    return render(request,"consulta_livros.html", {'usuarios': usuarios}) 
    
def consulta_user(request):
    usuarios = Usuario.objects.all()
    return render(request,"consulta_usuario.html", {'usuarios': usuarios})           

