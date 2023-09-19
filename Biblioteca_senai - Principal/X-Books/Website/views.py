from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    all_news = NewProdutos.objects.all()
    return render(request,"index.html",  {'news': all_news})
    
def livros(request):
    return render(request,"livros.html")

def catalogo(request):
    return render(request,"catalogo.html")

def catalogo2(request):
    return render(request,"catalogo-2.html")

def FAQs(request):
    return render(request,"FAQs.html")

def admin(request):
    return render(request,"admin.html")

def descricao(request):
    return render(request,"descricao.html")