# Generated by Django 3.1.3 on 2020-11-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='accept',
            field=models.BooleanField(default=False),
        ),
    ]
