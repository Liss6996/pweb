from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name="index"),
    path('agregar_producto/',agregar_producto, name="agregar"),

]