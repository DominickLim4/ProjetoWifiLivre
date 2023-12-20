from django.shortcuts import render, redirect
from .models import Usuario, RegistroConexao
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Extrair os dados do formulário
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            cpf = form.cleaned_data['cpf']
            
            # Salvar no banco de dados
            Usuario.objects.create(nome=nome, email=email, telefone=telefone, cpf=cpf)

            # Redirecionar para a página de sucesso
            return redirect('sucesso')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')
