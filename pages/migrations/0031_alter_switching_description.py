# Generated by Django 4.2.6 on 2023-10-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_switching_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switching',
            name='description',
            field=models.CharField(blank=True, default='non', max_length=30, null=True),
        ),
    ]