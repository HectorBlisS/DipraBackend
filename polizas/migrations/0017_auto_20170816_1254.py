# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polizas', '0016_auto_20170815_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='fecha',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recibo',
            name='numero',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]