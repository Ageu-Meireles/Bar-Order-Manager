from dataclasses import fields
from pyexpat import model
from django import forms
from datetime import datetime
from .models import Session
from cozinha.models import Table

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('client_name', 'table',)
        labels = {'client_name': 'Nome do cliente', 'table':'Número da mesa'}

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super(SessionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['table'].queryset = Table.objects.filter(is_busy=False)