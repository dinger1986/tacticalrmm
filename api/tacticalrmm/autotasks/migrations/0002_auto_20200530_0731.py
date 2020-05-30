# Generated by Django 3.0.6 on 2020-05-30 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0004_check_svc_policy_mode'),
        ('autotasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatedtask',
            name='assigned_check',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignedtask', to='checks.Check'),
        ),
    ]
