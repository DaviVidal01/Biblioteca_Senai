from django.shortcuts import render
from django import forms

class LoginEmail(forms.Form):
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
    senha_message = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : 'Digite sua Senha'
            }
        )
    )



class Feedback(forms.Form):
    feedback_message = forms.CharField(
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