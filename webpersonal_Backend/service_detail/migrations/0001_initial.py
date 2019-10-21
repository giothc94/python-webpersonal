# Generated by Django 2.2.6 on 2019-10-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Servicio')),
                ('content', models.TextField(verbose_name='Detalle del servicio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de cración')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Detalle de servicio',
                'verbose_name_plural': 'Detalles de servicios',
                'ordering': ['-created'],
            },
        ),
    ]