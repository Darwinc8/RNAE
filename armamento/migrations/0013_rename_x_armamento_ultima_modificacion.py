# Generated by Django 4.2.3 on 2023-09-08 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0012_rename_ultima_modificacion_armamento_x'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armamento',
            old_name='x',
            new_name='ultima_modificacion',
        ),
    ]