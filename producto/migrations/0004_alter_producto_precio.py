# Generated by Django 4.1.1 on 2022-10-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(),
        ),
    ]
