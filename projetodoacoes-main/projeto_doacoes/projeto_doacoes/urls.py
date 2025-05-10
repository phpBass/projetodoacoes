from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from doacoes.views import home  # Apenas home aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doacoes/', include('doacoes.urls')),  # Inclui rotas específicas do app
    path('', home, name='home'),  # Página principal
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
