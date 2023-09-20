from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path('livros/', views.livros, name="livros"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('catalogo2/', views.catalogo2, name="catalogo2"),
    path('funcionario/', views.funcionario, name="funcionario"),
    path('FAQs/', views.FAQs, name="FAQs"),
    path('descricao/', views.descricao, name="descricao")
]