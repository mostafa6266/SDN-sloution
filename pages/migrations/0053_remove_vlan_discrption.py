# Generated by Django 4.2.6 on 2023-12-10 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0052_remove_building_ip_range'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vlan',
            name='discrption',
        ),
    ]
