# Generated by Django 4.2.13 on 2024-05-23 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_rooms', '0003_alter_hotelroom_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotelroom',
            options={'verbose_name': 'Гостиничные номера', 'verbose_name_plural': 'Гостиничные номера'},
        ),
    ]
