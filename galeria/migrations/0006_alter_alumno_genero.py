# Generated by Django 5.0.6 on 2024-07-06 03:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_remove_alumno_id_genero_alumno_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='galeria.genero'),
        ),
    ]