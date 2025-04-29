from django.urls import path
from .views import login_view, listar_doacoes, adicionar_doacao, registro_view, home

urlpatterns = [
    path("login/", login_view, name="login"),
    path("registro/", registro_view, name="registro"),
    path("", listar_doacoes, name="listar_doacoes"),  # mantém como principal
    path("adicionar/", adicionar_doacao, name="adicionar_doacao"),
    path("home/", home, name="home"),  # muda home para /doacoes/home/
]
