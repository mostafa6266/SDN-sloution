# Generated by Django 4.2.6 on 2023-11-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocked_mac', '0003_rename_bloced_mac_address_blocked_mac_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocked_mac_address',
            name='mac_address',
            field=models.CharField(max_length=25),
        ),
    ]
