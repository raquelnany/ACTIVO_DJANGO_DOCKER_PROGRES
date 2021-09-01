# Generated by Django 3.0.14 on 2021-09-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_inventario_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(max_length=45)),
                ('calle', models.CharField(max_length=45)),
                ('colonia', models.CharField(max_length=45)),
                ('cp', models.BigIntegerField()),
                ('municipio', models.CharField(max_length=45)),
                ('estado', models.CharField(max_length=45)),
                ('pais', models.CharField(max_length=45)),
                ('razon_social', models.CharField(max_length=75)),
                ('rfc', models.CharField(max_length=13)),
                ('telefono', models.BigIntegerField()),
                ('contacto', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('pagina_web', models.CharField(max_length=25)),
                ('id_zona_horaria', models.IntegerField()),
                ('foto_cliente', models.CharField(max_length=50)),
                ('usar_inventario', models.IntegerField()),
                ('alertas_email', models.IntegerField()),
                ('registro', models.IntegerField()),
            ],
        ),
    ]
