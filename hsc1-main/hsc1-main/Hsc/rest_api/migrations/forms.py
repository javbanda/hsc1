from django import forms
from .models import Usuario
from django.core.validators import MinValueValidator
from django.core.validators import EmailValidator
from django.db import models


class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion']

#Validaciones

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(validators=[EmailValidator()])

    def __str__(self):
        return self.nombre



class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.strip():
            raise forms.ValidationError("El nombre no puede estar vacío.")
        return nombre