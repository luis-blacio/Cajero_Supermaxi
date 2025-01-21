from django.contrib import admin
from .models import Persona, Cliente, Empleado, Cajero, Supermercado, Producto, Caja, Pago, Factura

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')
    filter_horizontal = ('historial_compras',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'salario', 'turno')

@admin.register(Cajero)
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'atiende')

@admin.register(Supermercado)
class SupermercadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'horario_apertura')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'stock')
    actions = ['actualizar_stock']

    def actualizar_stock(self, request, queryset):
        for producto in queryset:
            producto.actualizar_stock(10)  # Ejemplo: Incrementa en 10 unidades

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display = ('id', 'ventas_realizadas')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'monto', 'fecha', 'tipo_pago', 'estado')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'total', 'metodo_pago')
    filter_horizontal = ('detalles_productos',)
