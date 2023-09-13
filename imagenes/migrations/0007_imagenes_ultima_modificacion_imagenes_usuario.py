# Generated by Django 4.2.3 on 2023-09-06 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imagenes', '0006_alter_imagenes_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenes',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='imagenes',
            name='usuario',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]