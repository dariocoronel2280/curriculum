# Generated by Django 2.0.2 on 2019-09-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=7, verbose_name='precio'),
        ),
    ]