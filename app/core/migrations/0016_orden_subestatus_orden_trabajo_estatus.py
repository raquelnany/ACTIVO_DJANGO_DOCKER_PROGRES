# Generated by Django 3.0.14 on 2021-12-02 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20211202_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_Subestatus',
            fields=[
                ('id_orden_subestatus', models.AutoField(primary_key=True, serialize=False)),
                ('orden_subestatus_es', models.CharField(max_length=120)),
                ('orden_subestatus_en', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Orden_Trabajo_Estatus',
            fields=[
                ('id_orden_trabajo_estatus', models.AutoField(primary_key=True, serialize=False)),
                ('orden_trabajo_estatus_es', models.CharField(max_length=120)),
                ('orden_trabajo_estatus_en', models.CharField(max_length=120)),
            ],
        ),
    ]
