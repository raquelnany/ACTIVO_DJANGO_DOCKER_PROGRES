# Generated by Django 3.0.14 on 2021-08-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_usuarioauthtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='', max_length=25),
        ),
    ]