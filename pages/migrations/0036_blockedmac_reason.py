# Generated by Django 4.2.6 on 2023-11-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_blockedmac'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockedmac',
            name='reason',
            field=models.CharField(default='No reason', max_length=100),
        ),
    ]
