# Generated by Django 4.1.7 on 2023-04-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre y Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('contact_type', models.IntegerField(choices=[[0, 'Pedido de información'], [1, 'Queja por un producto'], [2, 'Felicitaciones']], verbose_name='Tipo de contacto')),
                ('subscription', models.BooleanField(default=False, verbose_name='Suscribirme a correos informativos')),
                ('created_at', models.DateTimeField(verbose_name='Fecha de envió')),
            ],
        ),
    ]