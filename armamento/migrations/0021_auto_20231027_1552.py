# Generated by Django 3.2.21 on 2023-10-27 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0020_alter_armamento_municipio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamento',
            name='CUIP_PORTADOR',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='CUIP_RESPONSABLE',
            field=models.TextField(),
        ),
    ]