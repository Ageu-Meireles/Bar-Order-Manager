"""
    Este script faz o controle do funcionamento das urls do site
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", include("pages.urls", namespace="pages")),
    path('cozinha/', include('establishment.urls')),  
    path('clientes/', include('customers.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)