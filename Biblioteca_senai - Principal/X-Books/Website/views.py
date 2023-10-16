from django.shortcuts import render, redirect
from .models import *
from Website.forms import LoginEmail, Feedback, CadastrarLivros, CadastrarUsuario
from django.contrib import messages

# Create your views here.
def index(request):
    form_email = LoginEmail()
    form_feedback = Feedback()
    return render(request,"index.html", {
        "form": form_email, 
        "formF": form_feedback,

        })
    
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
    form_User = CadastrarUsuario()
    return render(request,"cadastrar_usuario.html", {'usuarios':usuarios,"form_User": form_User })

def cadastro_book(request):
    livros = Livros.objects.all()
    form_Livros = CadastrarLivros()
    return render(request,"cadastrar_livros.html", {'usuarios': usuarios})   

def consulta_book(request):
    usuarios = Usuario.objects.all()
    return render(request,"consulta_livros.html", {'usuarios': usuarios}) 
    
def atualiza_user(request):
    usuarios = Usuario.objects.all()
    return render(request,"Atualiza_usuario.html", {'usuarios': usuarios})      

def consulta_user(request):
    usuarios = Usuario.objects.all()
    return render(request,"consulta_usuario.html", {'usuarios': usuarios})           

def faq(request):
    return render(request,"FAQs.html") 

def login(request):
    if request.method == 'POST':
        form = LoginEmail(request.POST)

    if form.is_valid():
        email = form['email_form'].value()
        password = form['senha_form'].value()
        messages.success(request, f'Cadastrar com sucesso!')
        return redirect('index')
    else:
        messages.error(request, f' erro ao realizar o login!')
        return redirect('index')

def feedback(request):
    if request.method == "POST":
        bd = Genero(nome=request.POST['feedback_form'])
        bd.save()
        messages.success(request, f'feedback enviado com sucesso!')
        return redirect('index')

def delete(request, id):
    x = Usuario.objects.get(pk=id)
    x.delete()
    return redirect('listar')

def cadastrarU(request):
    if request.method == 'POST':
        form_User = CadastrarUsuario(request.POST)

    if form_User.is_valid():
        Usuario.objects.create(
        nome = form_User['nome_form'].value(),
        cpf = form_User['cpf_form'].value(),
        endereco = form_User['endereco_form'].value(),
        telefone = form_User['telefone_form'].value(),
        email = form_User['email_form'].value(),
        senha = form_User['senha_form'].value(),
        
        )
        messages.success(request, f'Usuário cadastrado com sucesso!')
        return redirect('funcionario')
    else:
        form_User = CadastrarUsuario
        return render('funcionario',{'form':form})

def cadastrarL(request):
    if request.method == 'POST':
        form = CadastrarLivros(request.POST)

    if form.is_valid():
        titulo = form_Livros['titulo_form'].value()
        autor = form_Livros['autor_form'].value()
        genero = form_Livros['genero_form'].value()
        ano = form_Livros['ano_form'].value()
        capa = form_Livros['capa_form'].value()
        messages.success(request, f'Livro registrado com sucesso!')
        return redirect('cadastrar_livros')
    else:
        form_Livros = CadastrarLivros
        return render('funcionario',{'form':form})

def listar(request):
    usuarios = Usuario.objects.all()
    return render(request,"consulta_usuario.html",{"usuarios":usuarios})

def adicionar(request):
    Usuario.objects.create(nome=request.POST['nome'])
    return redirect('listar')

def editar(request, id):
    usuarios = Usuario.objects.get(pk=id)
    return render(request, "consultar_usuario.html", {"usuarios":usuarios})

def update(request, id):
    usuarios = Usuario.objects.get(pk=id)
    usuarios.nome = request.POST['nome']
    usuarios.endereco = request.POST['endereco']
    usuarios.telefone = request.POST['telefone']
    usuarios.email = request.POST['email']
    usuarios.save()
    return redirect('listar')