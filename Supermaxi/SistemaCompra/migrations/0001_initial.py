# Generated by Django 5.1.5 on 2025-01-20 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventas_realizadas', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('monto', models.FloatField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_pago', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.FloatField()),
                ('categoria', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('horario_apertura', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaCompra.persona')),
                ('salario', models.FloatField()),
                ('turno', models.CharField(max_length=50)),
            ],
            bases=('SistemaCompra.persona',),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('metodo_pago', models.CharField(max_length=50)),
                ('detalles_productos', models.ManyToManyField(to='SistemaCompra.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaCompra.persona')),
                ('email', models.EmailField(max_length=254)),
                ('historial_compras', models.ManyToManyField(blank=True, to='SistemaCompra.factura')),
            ],
            bases=('SistemaCompra.persona',),
        ),
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='SistemaCompra.empleado')),
                ('atiende', models.CharField(max_length=255)),
            ],
            bases=('SistemaCompra.empleado',),
        ),
    ]
