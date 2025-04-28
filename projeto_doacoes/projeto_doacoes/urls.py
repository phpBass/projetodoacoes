"""
URL configuration for projeto_doacoes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from doacoes.views import login_view  # importa a view diretamente
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doacoes/', include('doacoes.urls')),  # Inclui as URLs do app "doacoes"
    path('login/', login_view, name='login'),  # <-- isso faz /login/ funcionar
    path('', home, name='home'),
]

urlpatterns += [
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]

def home(request):
    return HttpResponse("Projeto Doações: página inicial funcionando!")
