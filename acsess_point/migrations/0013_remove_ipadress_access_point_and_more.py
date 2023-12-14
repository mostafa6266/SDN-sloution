# Generated by Django 4.2.6 on 2023-12-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_point', '0012_ipadress_access_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipadress',
            name='access_point',
        ),
        migrations.AlterField(
            model_name='accesspoint',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, unique=True),
        ),
    ]
