# Generated by Django 3.1.3 on 2020-11-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20201105_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='mobile',
            field=models.CharField(default='', max_length=12),
        ),
    ]