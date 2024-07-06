from django import forms
from .models import Cliente, Contacto
from django import forms
from django.forms import ModelForm
from .models import Genero

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut_cli', 'nombres', 'apellidos', 'email', 'direccion', 'telefono', 'comuna', 'region']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['correo', 'nombre_completo', 'telefono', 'consulta']
        labels = {
            'correo': 'Correo',
            'nombre_completo': 'Nombre Completo',
            'telefono': 'Teléfono',
            'consulta': 'Consulta',
        }

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ["genero",]
        labels = {'genero': 'Género', }