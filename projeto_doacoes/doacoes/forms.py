from django import forms
from .models import Doacao
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['nome_doador', 'email_doador', 'descricao', 'quantidade']

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
