# Generated by Django 3.2.21 on 2023-11-28 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibre',
            fields=[
                ('ID_CALIBRE', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('CALIBRE', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('ID_DEPENDENCIA', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('DEPENDENCIA', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Edo_conservacion',
            fields=[
                ('ID_ESTADO', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('DESCRIPCION', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('Id_Emisor', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('ID_ENTIDAD', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('ENTIDAD', models.CharField(max_length=50)),
                ('SIGLAS', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Estatus_Arma',
            fields=[
                ('ID_ESTATUS', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('DESCRIPCION', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LOC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ENTIDAD', models.DecimalField(decimal_places=0, max_digits=10)),
                ('ENTIDAD', models.CharField(max_length=50)),
                ('DEPENDENCIA', models.CharField(max_length=5)),
                ('NO_LICENCIA', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('ID_MARCA', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('MARCA', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('ID_MODELO', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('MODELO', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Propiedad', models.TextField(max_length=20)),
                ('Status', models.IntegerField(choices=[(0, 'Deshabilitado'), (1, 'Habilitado')])),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('ID_TIPO', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('TIPO', models.CharField(max_length=50)),
                ('ID_CLASIFICACION', models.IntegerField(choices=[(0, 'Opción 0'), (1, 'Opción 1'), (2, 'Opción 2')])),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Alta',
            fields=[
                ('ID_ALTA', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('DESCRIPCION', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Dependencia',
            fields=[
                ('ID_TIPO_DEPENEDIENCIA', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('TIPO_DEPENEDENCIA', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Imagen',
            fields=[
                ('ID_IMAGEN', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('DESCRIPCION', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoFuncinamiento',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('TipoFuncionamiento', models.TextField(max_length=20)),
                ('Status', models.IntegerField(choices=[(0, 'Deshabilitado'), (1, 'Habilitado')])),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('ID_INSTITUCION', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=70)),
                ('ID_DEPENDENCIA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.dependencia')),
                ('ID_TIPO_DEPENDENCIA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.tipo_dependencia')),
            ],
        ),
        migrations.AddField(
            model_name='dependencia',
            name='ID_TIPO_DEPENDENCIA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.tipo_dependencia'),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_MUNICIPIO', models.DecimalField(decimal_places=0, max_digits=10)),
                ('MUNICIPIO', models.CharField(max_length=70)),
                ('ID_ENTIDAD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.entidad')),
            ],
            options={
                'unique_together': {('ID_ENTIDAD', 'ID_MUNICIPIO')},
            },
        ),
    ]
