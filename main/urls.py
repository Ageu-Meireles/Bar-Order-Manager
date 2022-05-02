"""
    Este script faz o controle do funcionamento das urls do site
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # administração do django
    path('admin/', admin.site.urls),
    # autenticação de usuários
    path('accounts/', include('allauth.urls')),
    path("", include("pages.urls", namespace="pages")),
    # aplicativo da cozinha
    path('cozinha/', include('cozinha.urls')),  
    # aplicativo dos clientes    # o método include() busca n
    path('clientes/', include('clientes.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)