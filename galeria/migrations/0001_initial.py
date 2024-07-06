# Generated by Django 5.0.6 on 2024-07-05 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPolera',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cat', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_comuna', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_region', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cli', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=20)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.region')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_detalle', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('categoria_polera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.categoriapolera')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('total_pedi', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.cliente')),
                ('detalle_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.detallepedido')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_productos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(max_length=30)),
                ('descrip_produc', models.CharField(max_length=40)),
                ('precio_produc', models.DecimalField(decimal_places=2, max_digits=20)),
                ('stock_produc', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.categoriapolera')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.region'),
        ),
    ]