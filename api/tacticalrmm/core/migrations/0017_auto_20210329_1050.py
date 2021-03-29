# Generated by Django 3.1.7 on 2021-03-29 10:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210319_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfield',
            name='checkbox_value',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customfield',
            name='default_values_multiple',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), blank=True, default=list, null=True, size=None),
        ),
    ]
