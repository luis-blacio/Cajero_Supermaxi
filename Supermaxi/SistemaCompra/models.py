# models.py
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=255)

    def caminar(self):
        return "Persona caminando"

    def __str__(self):
        return self.nombre

class Cliente(Persona):
    email = models.EmailField()
    historial_compras = models.ManyToManyField('Factura', blank=True)

    def pagar_productos(self):
        return "Pago realizado"

    def escoger_productos(self):
        return "Productos seleccionados"

    def solicitar_devolucion(self, factura):
        # Lógica para devolución
        return True

class Empleado(Persona):
    salario = models.FloatField()
    turno = models.CharField(max_length=50)

    def recibir_productos(self):
        return "Productos recibidos"

class Cajero(Empleado):
    atiende = models.CharField(max_length=255)

class Supermercado(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    horario_apertura = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    categoria = models.CharField(max_length=255)
    stock = models.IntegerField()

    def actualizar_stock(self, cantidad):
        self.stock += cantidad
        self.save()

    def verificar_stock(self):
        return self.stock > 0

    def __str__(self):
        return self.nombre

class Caja(models.Model):
    ventas_realizadas = models.IntegerField(default=0)

    def procesar_pago(self):
        return "Pago procesado"

    def generar_factura(self):
        return Factura()

    def calcular_monto(self):
        return "Monto calculado"

    def cerrar_caja(self):
        return "Caja cerrada"

class Pago(models.Model):
    monto = models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    id_pago = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    def validar_pago(self):
        return True

    def reembolsar_pago(self):
        return True

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    total = models.FloatField()
    detalles_productos = models.ManyToManyField(Producto)
    metodo_pago = models.CharField(max_length=50)

    def imprimir_recibo(self):
        return "Recibo impreso"

    def enviar_por_email(self, email):
        return f"Factura enviada a {email}"

    def __str__(self):
        return f"Factura {self.id}"
