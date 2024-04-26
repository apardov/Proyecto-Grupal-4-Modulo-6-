# Generated by Django 5.0.4 on 2024-04-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_proveedor', models.CharField(max_length=100)),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('nombre_representante', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
