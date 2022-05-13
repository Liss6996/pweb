from django import forms
from django.forms import ModelForm
from .models import *



#template formulario
class ProductoForm(ModelForm):

     class Meta:
         model = Producto
         fields = ['codigo','nombre','marca','precio','stock','descripcion','tipo']