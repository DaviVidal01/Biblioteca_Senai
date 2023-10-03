from django.shortcuts import render
from .models import *
from Website.forms import LoginEmail, Feedback

# Create your views here.
def index(request):
    form_email = LoginEmail()
    form_feedback = Feedback()
    return render(request,"index.html", {"form": form_email, "formF": form_feedback})
    
def livros(request):
    livros = Livros.objects.all()
    form_feedback = Feedback
    return render(request,"livros.html", {'livros': livros, "formF": form_feedback})

def catalogo(request):
    livros = Livros.objects.all()
    form_feedback = Feedback
    return render(request,"catalogo.html", {'livros': livros, "formF": form_feedback})

def catalogo2(request):
    livros = Livros.objects.all()
    form_feedback = Feedback
    return render(request,"catalogo-2.html", {'livros': livros, "formF": form_feedback})

def FAQs(request):
    form_email = LoginEmail,
    form_senha = LoginSenha,
    form_feedback = Feedback
    return render(request,"FAQs.html", {"formE": form_email,"formS": form_senha, "formF": form_feedback})

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

