# Generated by Django 4.1.1 on 2022-10-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0006_remove_credito_modificacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credito',
            options={'ordering': ['-fecha']},
        ),
        migrations.RenameField(
            model_name='credito',
            old_name='producto',
            new_name='productos',
        ),
    ]
