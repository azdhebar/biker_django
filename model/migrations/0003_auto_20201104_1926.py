# Generated by Django 3.1.3 on 2020-11-04 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_models_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='models',
            options={'ordering': ['-created_at'], 'verbose_name': 'Model', 'verbose_name_plural': 'Models'},
        ),
    ]
