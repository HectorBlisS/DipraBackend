# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 21:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('documento', 'documento'), ('buzon', 'buzon'), ('carta', 'carta')], default='documento', max_length=100)),
                ('archivo', models.FileField(upload_to='asesores/documentos')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('asesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archivos_asesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_asesor', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_reclutamieto', models.CharField(blank=True, max_length=100, null=True)),
                ('candidato', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('tarjetas', models.IntegerField(blank=True, null=True)),
                ('oficina', models.CharField(blank=True, max_length=100, null=True)),
                ('reclutador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reclutador_asesor', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asesor_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(blank=True, max_length=100, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('asesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cita_asesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(blank=True, max_length=100, null=True)),
                ('clave_stat', models.BooleanField(default=True)),
                ('fecha_inicio', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_final', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('asesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clave_asesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('asesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curso_asesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
