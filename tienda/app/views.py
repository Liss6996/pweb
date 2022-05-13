import re
from django.shortcuts import render
from .models import *
from .forms import *

def index (request):
    return render(request,'app/index.html')

def agregar_producto (request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto guardado correctamente!'
    return render (request,'app/agregar_producto.html',datos)

def modificar_producto (request):
    datos = {
        'form' :ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= '¡Producto modificado con exito!'
    return render (request,'app/modificar_producto.html')        

def listarproductos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    return render(request, 'app/productos/listar_producto.html', datos)



def index (request):
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll
    }

    return render(request, 'app/home.html',datos)
 
          