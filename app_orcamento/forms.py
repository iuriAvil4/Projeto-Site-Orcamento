from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError
import re

class ClienteForm(forms.ModelForm):
	
    nome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome", "class":"form-control"}), label="")
    sobrenome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sobrenome", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    telefone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefone com DDD", "class":"form-control"}), label="")
    descricao = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Descrição", "class":"form-control", "style":"height: 250px; resize: none;"}), label="")
    

    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'descricao']

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        # Validar telefone no formato (11 dígitos)
        if not re.match(r'^\d{11}$', telefone):
            raise ValidationError('Número de telefone inválido. Utilize o formato com DDD.')

        return telefone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Validar e-mail usando uma abordagem mais ampla
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValidationError("Formato de e-mail inválido")

        return email