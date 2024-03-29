# Generated by Django 3.0.14 on 2021-08-24 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_centrocosto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('proveedor', models.CharField(default='', max_length=25)),
                ('calle', models.CharField(default='', max_length=25)),
                ('colonia', models.CharField(default='', max_length=25)),
                ('cp', models.BigIntegerField()),
                ('municipio', models.CharField(default='', max_length=25)),
                ('estado', models.CharField(default='', max_length=25)),
                ('pais', models.CharField(default='', max_length=25)),
                ('razon_social', models.CharField(default='', max_length=25)),
                ('rfc', models.BigIntegerField()),
                ('pagina_web', models.CharField(default='', max_length=25)),
                ('foto_proveedor', models.CharField(max_length=50)),
                ('numero_proveedor', models.BigIntegerField()),
                ('moneda', models.CharField(default='', max_length=25)),
                ('id_estatus_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.EstatusUsuario')),
            ],
        ),
    ]
