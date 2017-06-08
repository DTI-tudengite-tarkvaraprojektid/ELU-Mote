# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-08 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20170608_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='register_limit_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]