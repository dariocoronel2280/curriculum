# Generated by Django 2.0.2 on 2019-09-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('description', models.TextField(verbose_name='descripcion')),
                ('image', models.ImageField(upload_to='productos', verbose_name='imagen')),
                ('precio', models.DecimalField(decimal_places=2, default='00.00', max_digits=7, verbose_name='precio')),
                ('link', models.URLField(blank=True, null=True, verbose_name='direccion whatsapp')),
                ('created', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'ordering': ['created'],
            },
        ),
    ]