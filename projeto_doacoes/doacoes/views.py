# Create your views here.
from django.shortcuts import render, redirect
from .models import Doacao
from .forms import DoacaoForm  # Vamos criar esse formulário já já
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('listar_doacoes')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados informados.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'doacoes/registro.html', {'form': form})


def listar_doacoes(request):
    doacoes = Doacao.objects.all()
    return render(request, 'doacoes/listar.html', {'doacoes': doacoes})


def adicionar_doacao(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doacoes')
    else:
        form = DoacaoForm()
    return render(request, 'doacoes/adicionar.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("listar_doacoes")  # Redireciona para a página principal
        
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            
    return render(request, "doacoes/login.html")

def home(request):
    return render(request, "home.html")

