# Generated by Django 4.2.6 on 2023-11-01 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_remove_switching_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedMAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(max_length=17, unique=True)),
                ('blocked_at', models.DateTimeField(auto_now_add=True)),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.switching')),
            ],
        ),
    ]
