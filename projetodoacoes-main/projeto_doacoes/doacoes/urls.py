from django.urls import path
from .views import login_view, listar_doacoes, adicionar_doacao, registro_view #home

urlpatterns = [
    path("login/", login_view, name="login"),  # /doacoes/login/
    path("registro/", registro_view, name="registro"),
    path("", listar_doacoes, name="listar_doacoes"),  # /doacoes/
    path("adicionar/", adicionar_doacao, name="adicionar_doacao"),
#    path("home/", home, name="home"),  # /doacoes/home/
]
