# Generated by Django 4.2.3 on 2023-09-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0016_alter_armamentolog_id_alterna_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamentolog',
            name='id_alterna',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
