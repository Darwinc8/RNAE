# Generated by Django 4.2.3 on 2023-09-18 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portadores', '0035_alter_portador_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portador',
            name='usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]