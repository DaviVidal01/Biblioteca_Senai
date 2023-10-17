from django.shortcuts import render
from django import forms

class LoginEmail(forms.Form):
    email_form = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 60,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'email@email.com',
            }
        )
    )
    senha_form = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : '*******',
            }
        )
    )

class Feedback(forms.Form):
    feedback_form = forms.CharField(
        label = 'Feedback',
        required = False,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite suas Sugestões ou Feedbacks'
            }
        )
    )

class CadastrarUsuario(forms.Form):
    nome_form = forms.CharField(
        label='Nome',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'form3Example1c'
            }
        )
    )
    cpf_form = forms.CharField(
        label='CPF',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'form3Example1c'
            }
        )
    )
    endereco_form = forms.CharField(
        label='Endereço',
        required= True,
        max_length= 255,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'form3Example1c'
            }
        )
    )
    telefone_form = forms.CharField(
        label='Telefone',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'form3Example1c'
            }
        )
    )
    email_form = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 60,
        widget = forms.EmailInput(
            attrs = {
                'type' : 'email',
                'class' : 'form-control',
                'id' : 'form3Example3c',
                'placeholder' : 'email@email.com',
            }
        )
    )
    senha_form = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs = {
                'type' : 'password',
                'class' : 'form-control',
                'id' : 'form3Example4c'
            }
        )
    )
    senhaconfirmar_form = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 20,
        widget = forms.PasswordInput(
            attrs = {
                'type' : 'password',
                'class' : 'form-control',
                'id' : 'form3Example4c'
            }
        )
    )

class CadastrarLivros(forms.Form):
    titulo_form = forms.CharField(
        label='Titulo',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    autor_form = forms.CharField(
        label='Autor',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )

    ano_form = forms.CharField(
        label='Ano',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    image_form = forms.CharField(
        label='Image',
        required= True,
        max_length= 45,
        widget= forms.FileInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )