from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from doacoes.views import login_view, home  # Corrigido aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doacoes/', include('doacoes.urls')),
    path('login/', login_view, name='login'),
    path('', home, name='home'),  # Corrigido aqui
]

urlpatterns += [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
