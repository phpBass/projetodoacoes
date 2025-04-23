from django.urls import path
from .views import login_view, listar_doacoes, adicionar_doacao, registro_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("registro/", registro_view, name="registro"),
    path("", listar_doacoes, name="listar_doacoes"),
    path("adicionar/", adicionar_doacao, name="adicionar_doacao"),
]