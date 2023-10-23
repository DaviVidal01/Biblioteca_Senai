from django.shortcuts import render, redirect
from .models import *
from Website.forms import LoginEmail, Feedback, CadastrarLivros, CadastrarUsuario, ReservarLivros
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
# Create your views here.

# ----------- Páginas
def index(request):
    form_feedback = Feedback()
    form_email = LoginEmail()
    usuarios= Usuario.objects.all()
    return render(request,"index.html", {
        "form": form_email, 
        "formF": form_feedback,

        })
    
def livros(request):
    genero = Genero.objects.all()
    livros = Livros.objects.all()
    form_email = LoginEmail()
    usuarios= Usuario.objects.all()
    form_feedback = Feedback
    return render(request,"livros.html", { 'form':form_email ,'livros': livros, "formF": form_feedback, "genero": genero})

def catalogo(request):
    genero = Genero.objects.all()
    livros = Livros.objects.all()
    form_email = LoginEmail()
    usuarios= Usuario.objects.all()
    form_feedback = Feedback
    return render(request,"catalogo.html", {'form': form_email, 'livros': livros, "formF": form_feedback, "genero": genero})

def FAQs(request):
    form_email = LoginEmail()
    form_feedback = Feedback()
    return render(request,"FAQs.html", {
        "form": form_email, 
        "formF": form_feedback,

        })

@login_required
def funcionario(request):
    usuarios = Usuario.objects.all()
    livros = Livros.objects.all()
    return render(request,"admin.html", {'usuarios': usuarios, 'livros': livros, 'logout':logout})

def cadastro(request):
    usuarios = Usuario.objects.all()
    return render(request,"cadastro.html", {'usuarios': usuarios})

def faq(request):
    return render(request,"FAQs.html") 
    
def feedback(request):
    if request.method == "POST":
        bd = Genero(nome=request.POST['feedback_form'])
        bd.save()
        messages.success(request, f'feedback enviado com sucesso!')
        return redirect('index')

# ----------- Cadastro

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

        return render('funcionario',{'formU':form_User})

def cadastro_book(request):
    livros = Livros.objects.all()
    form_Livros = CadastrarLivros()
    return render(request,"cadastrar_livros.html", {'livros': livros, 'form_Livros': form_Livros})   

def status(request):
    form_Reservar = ReservarLivros()
    if request.method == 'POST':
        form= ReservarLivros(request.POST)
        print(form)
        if form.is_valid():
            Registro.objects.create(
            data_Ret = form['data_Ret'].value(),
            data_Dev = form['data_Dev'].value(),
            status = form['status'].value(),
            livro_id = Livros.objects.get(pk=id),
            usuario_id = Usuario.objects.get(pk=id),
            )
            messages.success(request, f'Status alterado com sucesso!')
            return redirect("index")
        else:
            print("erro")
    return render(request,'reserva_livros.html',{'form_Reservar':form_Reservar})

def cadastrarL(request):
    
    form_Livros = CadastrarLivros()
    if request.method == 'POST':
        form_Livros = CadastrarLivros(request.POST, request.FILES)

        if form_Livros.is_valid():
            Livros.objects.create(
            titulo = form_Livros['titulo_form'].value(),
            autor = form_Livros['autor_form'].value(),
            ano = form_Livros['ano_form'].value(),
            image = form_Livros['image_form'].value(),
            genero_id = request.POST.get('genero'),
            )
            messages.success(request, f'Livro registrado com sucesso!')
            
        else:
            print("erro")
    return render(request,'cadastrar_livros.html',{'form_Livros':form_Livros})

# ----------- CRUD Usuário

def deleteU(request, id):
    x = Usuario.objects.get(pk=id)
    x.delete()
    messages.success(request, 'Usuário Deletado com Sucesso')
    return redirect('listarU')

def listarU(request):
    search_query = request.GET.get('search')
    if search_query:
        usuarios = Usuario.objects.filter(nome__icontains=search_query)
    else:
        usuarios = Usuario.objects.all()
    return render(request,"consulta_usuario.html",{"usuarios":usuarios})

def adicionarU(request):
    Usuario.objects.create(nome=request.POST['nome'])
    messages.success(request, 'Usuário adicionado com sucesso')
    return redirect('listarU')

def editarU(request, id):
    usuarios = Usuario.objects.get(pk=id)
    return render(request, "Atualiza_usuario.html", {"usuarios":usuarios})

def updateU(request, id):
    usuarios = Usuario.objects.get(pk=id)
    usuarios.nome = request.POST['nome']
    usuarios.endereco = request.POST['endereco']
    usuarios.telefone = request.POST['telefone']
    usuarios.email = request.POST['email']
    usuarios.save()
    messages.success(request, 'Usuário Editado com Sucesso')
    return redirect('listarU')
    
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
    
def consulta_user(request):
    usuarios = Usuario.objects.all()
    return render(request,"consulta_usuario.html", {'usuarios': usuarios})     

def atualiza_user(request):
    usuarios = Usuario.objects.all()
    return render(request,"atualiza_usuario.html", {'usuarios': usuarios})      
          
# ----------- CRUD Livros
def deleteL(request, id):
    x = Livros.objects.get(pk=id)
    x.delete()
    messages.success(request, 'Livro Deletado com Sucesso')
    return redirect('listarL')

def adicionarL(request):
    Livros.objects.create(nome=request.POST['titulo'])
    messages.success(request, 'Livro Adicionado com Sucesso')
    return redirect('listarL')

def listarL(request):
    search_query = request.GET.get('search')
    if search_query:
        livros = Livros.objects.filter(titulo__icontains=search_query)
    else:
        livros = Livros.objects.all()
    return render(request,"consulta_livro.html",{"livros":livros})

def editarL(request, id):
    livros = Livros.objects.get(pk=id)
    return render(request, "consulta_livro.html",{"livros":livros})

def updateL(request, id):
    livros = Livros.objects.get(pk=id)
    livros.titulo = request.POST['titulo']
    livros.autor = request.POST['autor']
    livros.status = request.POST['status']
    livros.ano = request.POST['ano']
    livros.destaque = request.POST['destaque']
    livros.image = request.POST['image']
    livros.genero = request.POST.get('genero')
    livros.save()
    messages.success(request, 'Livro Editado com Sucesso')
    return redirect('listarL')

def consulta_book(request):
    livros = Livros.objects.all()
    return render(request,"consulta_livro.html", {'livros': livros})

def atualiza_book(request):
    livros = Livros.objects.all()
    return render(request,"atualiza_livro.html", {'livros': livros})  

# ----------- Auth Login

def login(request):
    form = LoginEmail()

    if request.method == 'POST':
        form = LoginEmail(request.POST)

    if form.is_valid():
        email = form['email_form'].value()
        password = form['senha_form'].value()
        user_temp = User.objects.get(email= email)

        usuario = auth.authenticate(
            request,
            username = user_temp,
            password = password
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request, 'Login efetuado com sucesso!')
            if usuario.username == "admin":
                return redirect('funcionario')
            return redirect('index')
    else:
        messages.error(request, f' Erro ao realizar o login!')
        return redirect('index')
    
    return render(request, 'index.html', {'form': form}) 

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('index')

def feedback(request):
    if request.method == "POST":
        bd = Genero(nome=request.POST['feedback_form'])
        bd.save()
        messages.success(request, f'feedback enviado com sucesso!')
        return redirect('index')