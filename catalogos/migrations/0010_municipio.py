# Generated by Django 4.2.3 on 2023-07-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0009_delete_municipio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ENTIDAD', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ID_MUNICIPIO', models.DecimalField(decimal_places=0, max_digits=10)),
                ('MUNICIPIO', models.CharField(max_length=70)),
            ],
            options={
                'unique_together': {('ID_ENTIDAD', 'ID_MUNICIPIO')},
            },
        ),
    ]
