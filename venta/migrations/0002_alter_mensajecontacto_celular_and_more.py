# Generated by Django 4.1.3 on 2022-11-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajecontacto',
            name='celular',
            field=models.BigIntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='mensajecontacto',
            name='dni',
            field=models.BigIntegerField(max_length=8),
        ),
    ]
