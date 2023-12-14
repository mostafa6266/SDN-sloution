# Generated by Django 4.2.6 on 2023-12-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_point', '0019_alter_accesspoint_port_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesspoint',
            name='real_port',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='accesspoint',
            name='switch_ip',
            field=models.GenericIPAddressField(default=None),
        ),
    ]