# Generated by Django 4.1.2 on 2022-11-02 23:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0004_alter_publicacion_linea_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publicacion',
            name='subtitulo',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ExtensionMoto',
        ),
    ]
