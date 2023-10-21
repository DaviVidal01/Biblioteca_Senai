from django.urls import path
from . import views

urlpatterns =[
# -------- Pages Guests
    path("", index, name="index"),
    path('livros',livros, name="livros"),
    path('catalogo',catalogo, name="catalogo"),
    path('FAQs',FAQs, name="FAQs"),
    path('login',login, name="login"),
    path('feedback',feedback, name="feedback"),

# -------- Pages Admin
    path('funcionario',funcionario, name="funcionario"),
    path('cadastro',cadastro, name="cadastro"),

# -------- Admin User
    path('cadastrarU',cadastrarU, name="cadastrarU"),
    path('cadastro_user',cadastro_usuarios, name="cadastro"),
    path('consulta_user',consulta_user, name="cadastro"),
    path('atualiza_user',atualiza_user, name="atualizacao"),

# -------- Admin Book
    path('cadastro_book',cadastro_book, name="cadastro_book"),
    path('consulta_book',consulta_book, name="cadastro"),
    path('atualiza_book',atualiza_book, name="atualizacao"),
    path('cadastrarL',cadastrarL, name="cadastrarL"),
    path('reserva_livros',status, name="reserva_livros"),

# -------- Auth Login
    path('login',login, name="login"),
    path('logout',logout, name='logout'),
    path('deleteU/<int:id>',deleteU, name="delete"),

# -------- CRUD Usuários
    path('listarU',listarU, name="listarU"),
    path('adicionarU',adicionarU, name="adicionarU"),
    path('deletarU/<int:id>',deleteU, name="deleteU"),
    path('editarU/<int:id>',editarU, name="editarU"),
    path('updateU/<int:id>',updateU, name="updateU"),

# -------- CRUD Livros
    path('listarL', listarL, name="listarL"),
    path('adicionarL',adicionarL, name="adicionarL"),
    path('deletarL/<int:id>',deleteL, name="deleteL"),
    path('editarL/<int:id>',editarL, name="editarL"),
    path('updateL/<int:id>',updateL, name="updateL"),
]