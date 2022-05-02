from statistics import mode
from django.db import models
from django.urls import translate_url

# Create your models here.
class Product(models.Model):
    CHOICES_TYPES = (
        ('1', 'comidas'),
        ('2', 'bebidas'),
        ('3', 'sobremesas')
    )
    name = models.CharField(verbose_name='Nome do produto', max_length=100)
    type = models.CharField(verbose_name='Tipo do produto', choices=CHOICES_TYPES, default=1, max_length=2)
    value = models.CharField(verbose_name='Valor do produto', max_length=8)
    image = models.ImageField(verbose_name='Imagem do produto', upload_to='images/')
    description = models.CharField(verbose_name='Descrição do produto', max_length=500)
    is_active = models.BooleanField(verbose_name='Está ativo?', default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(verbose_name='Número da mesa')
    seaters = models.IntegerField(verbose_name='Número de assentos')
    details = models.CharField(verbose_name='Detalhes da mesa', max_length=500)
    is_active = models.BooleanField(verbose_name='Está ativa?', default=True)
    is_busy = models.BooleanField(verbose_name="Está ocupada?", default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.number)
