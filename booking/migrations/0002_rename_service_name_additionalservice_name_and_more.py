# Generated by Django 4.2.13 on 2024-05-31 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalservice',
            old_name='service_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='additionalservice',
            old_name='service_price',
            new_name='price',
        ),
    ]
