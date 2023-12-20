from django import forms

class LoginForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    telefone = forms.CharField(label='Telefone', max_length=15)
    cpf = forms.CharField(label='CPF', max_length=14)