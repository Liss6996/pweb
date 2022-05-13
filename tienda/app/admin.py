from django.contrib import admin
from .models import *
# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock']
    search_fields = ['codigo']
    list_per_pages = 5

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductosAdmin)