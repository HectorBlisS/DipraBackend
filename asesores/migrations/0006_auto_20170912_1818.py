# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asesores', '0005_clave_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='fechaF',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='fechaI',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
