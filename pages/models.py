from django.db import models
from cozinha.models import Table
class Session(models.Model):
    client_name = models.CharField(verbose_name='Nome do cliente', max_length=200)
    table = models.ForeignKey(Table,verbose_name='Número da mesa do cliente', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(verbose_name='Está ativo?', default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)