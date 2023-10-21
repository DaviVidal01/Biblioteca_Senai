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

def clean_nome_form(self):
        nome_form = self.cleaned_data.get('Nome')

        if nome_form:
            nome_form = nome_form.strip()
            if ' ' in nome_form:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome_form
            
def clean_senhaconfirmar_form(self):
    senha_form = self.cleaned_data.get('senha_form')
    senhaconfirmar_form = self.cleaned_data.get('senhaconfirmar_form')

    if senha_form and senhaconfirmar_form:
        if senha_form != senhaconfirmar_form:
            raise forms.ValidationError('Senhas não são iguais')
        else:
            return senhaconfirmar_form


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

class ReservarLivros(forms.Form):
    data_Ret = forms.CharField(
            label = 'Data de retirada',
            required = True,
            widget = forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                }
            )
        )
    data_Dev = forms.CharField(
        label='Data de devolução',
        required= True,
        
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    status = forms.CharField(
        label='Status',
        required= True,
        max_length= 45,
        widget= forms.TextInput(
            attrs = {
                'class' : 'form-control'
            }
        )
    )

