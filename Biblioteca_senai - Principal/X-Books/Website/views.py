from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,"index.html")
    
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

def admin(request):
    return render(request,"admin.html")

def descricao(request):
    usuarios = Usuario.objects.all()
    return render(request,"descricao.html", {'usuarios': usuarios})