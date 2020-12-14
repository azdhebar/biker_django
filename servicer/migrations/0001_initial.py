# Generated by Django 3.1.2 on 2020-10-29 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
        ('brand', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_servicer', to='brand.brand')),
                ('model_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_servicer', to='model.models')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_servicer', to='account.account')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]