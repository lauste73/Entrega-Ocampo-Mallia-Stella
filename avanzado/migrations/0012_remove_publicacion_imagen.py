# Generated by Django 4.1.2 on 2022-11-06 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0011_publicacion_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='imagen',
        ),
    ]
