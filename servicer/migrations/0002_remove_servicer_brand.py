# Generated by Django 3.1.3 on 2020-11-04 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicer',
            name='brand',
        ),
    ]
