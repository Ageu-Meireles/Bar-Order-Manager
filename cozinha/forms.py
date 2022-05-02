from django import forms
from datetime import datetime
from .models import Product, Table

class ProductForm(forms.ModelForm):
    CHOICES_TYPES = (
        ('1', 'comidas'),
        ('2', 'bebidas'),
        ('3', 'sobremesas')
    )
    type = forms.ChoiceField(choices=CHOICES_TYPES, label='tipo do produto')

    class Meta:
        model = Product
        fields = ('image', 'name', 'value', 'description', 'type')
        labels = {'image': 'Imagem do produto', 'name': 'Nome do produto', 'value': 'Preço', 'description': 'Descrição do produto'}

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('number', 'seaters', 'details')
        labels = {'number': 'Número da mesa', 'seaters': 'Número de assentos', 'details': 'Detalhes da mesa e/ou posição'}

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(TableForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'