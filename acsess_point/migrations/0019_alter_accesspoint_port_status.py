# Generated by Django 4.2.6 on 2023-12-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acsess_point', '0018_accesspoint_port_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesspoint',
            name='port_status',
            field=models.CharField(default='enable', max_length=10),
        ),
    ]
