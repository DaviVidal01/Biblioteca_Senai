from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path('livros/', views.livros, name="livros"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('catalogo2/', views.catalogo2, name="catalogo2"),
    path('funcionario/', views.funcionario, name="funcionario"),
    path('funcionario1/', views.funcionario1, name="funcionario1"),
    path('funcionario2/', views.funcionario2, name="funcionario2"),
    path('funcionario3/', views.funcionario3, name="funcionario3"),
    path('FAQs/', views.FAQs, name="FAQs"),
    path('descricao/', views.descricao, name="descricao"),
    path('cadastro/', views.cadastro, name="cadastro")
]