# Generated by Django 3.1.2 on 2020-10-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
