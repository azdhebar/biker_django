# Generated by Django 3.1.3 on 2020-11-05 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20201105_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='vehicle_number',
        ),
    ]