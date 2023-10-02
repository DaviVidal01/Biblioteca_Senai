from django.shortcuts import render
from django import forms

class Loginemail(forms.Form):
    email_message = forms.CharField(
        label = 'Email',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite seu Email'
            }
        )
    )
class Loginsenha(forms.Form):
        senha_message = forms.CharField(
        label = 'Email',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite sua Senha'
            }
        )
    )