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
    path('cadastro/', views.cadastro, name="cadastro"),
    path('cadastro_user/', views.cadastro_usuarios, name="cadastro"),
    path('cadastro_book/', views.cadastro_book, name="cadastro_book"),
    path('consulta_book/', views.consulta_book, name="cadastro"),
    path('consulta_user/', views.consulta_user, name="cadastro"),
    path('atualiza_user/', views.atualiza_user, name="atualizacao"),
    path('atualiza_book/', views.atualiza_book, name="atualizacao"),
    path('login/', views.login, name="login"),
    path('feedback/', views.feedback, name="feedback"),
    path('cadastrarL', views.cadastrarL, name="cadastrarL"),
    path('cadastrarU/', views.cadastrarU, name="cadastrarU"),

# -------- Auth Login
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('deleteU/<int:id>', views.deleteU, name="delete"),

# -------- CRUD Usuários
    path('listarU', views.listarU, name="listarU"),
    path('adicionarU/', views.adicionarU, name="adicionarU"),
    path('deletarU/<int:id>', views.deleteU, name="deleteU"),
    path('editarU/<int:id>', views.editarU, name="editarU"),
    path('updateU/<int:id>', views.updateU, name="updateU"),

# -------- CRUD Livros
    path('listarL', views.listarL, name="listarL"),
    path('adicionarL/', views.adicionarL, name="adicionarL"),
    path('deletarL/<int:id>', views.deleteL, name="deleteL"),
    path('editarL/<int:id>', views.editarL, name="editarL"),
    path('updateL/<int:id>', views.updateL, name="updateL"),
]