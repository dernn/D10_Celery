# Generated by Django 4.0.5 on 2024-03-26 18:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc_donalds', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pseudonyms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), null=True, size=8),
        ),
    ]
