# Generated by Django 3.1.3 on 2020-11-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='remarks',
            field=models.TextField(blank=True, default=''),
        ),
    ]
