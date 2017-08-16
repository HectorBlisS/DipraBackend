# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 20:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polizas', '0007_auto_20170716_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcliente', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha_poliza', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('tpersona', models.CharField(blank=True, max_length=150, null=True)),
                ('ecivil', models.CharField(blank=True, max_length=150, null=True)),
                ('genero', models.CharField(blank=True, max_length=150, null=True)),
                ('rsocial', models.CharField(blank=True, max_length=150, null=True)),
                ('apaterno', models.CharField(blank=True, max_length=150, null=True)),
                ('amaterno', models.CharField(blank=True, max_length=150, null=True)),
                ('pnombre', models.CharField(blank=True, max_length=150, null=True)),
                ('snombre', models.CharField(blank=True, max_length=150, null=True)),
                ('rfc', models.CharField(blank=True, max_length=150, null=True)),
                ('curp', models.CharField(blank=True, max_length=150, null=True)),
                ('edad', models.CharField(blank=True, max_length=150, null=True)),
                ('tipoid', models.CharField(blank=True, max_length=150, null=True)),
                ('numid', models.CharField(blank=True, max_length=150, null=True)),
                ('fnacimiento', models.CharField(blank=True, max_length=150, null=True)),
                ('fiel', models.CharField(blank=True, max_length=150, null=True)),
                ('pais', models.CharField(blank=True, max_length=150, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=150, null=True)),
                ('calle', models.CharField(blank=True, max_length=150, null=True)),
                ('edificio', models.CharField(blank=True, max_length=150, null=True)),
                ('noext', models.CharField(blank=True, max_length=150, null=True)),
                ('noint', models.CharField(blank=True, max_length=150, null=True)),
                ('otroext', models.CharField(blank=True, max_length=150, null=True)),
                ('cp', models.CharField(blank=True, max_length=150, null=True)),
                ('colonia', models.CharField(blank=True, max_length=150, null=True)),
                ('municipio', models.CharField(blank=True, max_length=150, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=150, null=True)),
                ('estado', models.CharField(blank=True, max_length=150, null=True)),
                ('telefono', models.CharField(blank=True, max_length=150, null=True)),
                ('correo', models.CharField(blank=True, max_length=150, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=150, null=True)),
                ('otraoc', models.CharField(blank=True, max_length=150, null=True)),
                ('fmercantil', models.CharField(blank=True, max_length=150, null=True)),
                ('honorarios', models.CharField(blank=True, max_length=150, null=True)),
                ('institucion', models.CharField(blank=True, max_length=150, null=True)),
                ('aempresarial', models.CharField(blank=True, max_length=150, null=True)),
                ('actempresarial', models.CharField(blank=True, max_length=150, null=True)),
                ('rtemp', models.CharField(blank=True, max_length=150, null=True)),
                ('rperm', models.CharField(blank=True, max_length=150, null=True)),
                ('resotro', models.CharField(blank=True, max_length=150, null=True)),
                ('fpublico', models.CharField(blank=True, max_length=150, null=True)),
                ('parpublico', models.CharField(blank=True, max_length=150, null=True)),
                ('asalariado', models.CharField(blank=True, max_length=150, null=True)),
                ('bhonorarios', models.CharField(blank=True, max_length=150, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('asesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asesor_poliza', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='actempresarial',
            new_name='addaddress',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='aempresarial',
            new_name='agrupacion',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='amaterno',
            new_name='apertura',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='apaterno',
            new_name='cis',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='asalariado',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='bhonorarios',
            new_name='daños',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='calle',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='ciudad',
            new_name='financiamiento',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='colonia',
            new_name='idpoliza',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='correo',
            new_name='importe',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='cp',
            new_name='newaddress',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='curp',
            new_name='next',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='ecivil',
            new_name='pago',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='edad',
            new_name='prima',
        ),
        migrations.RenameField(
            model_name='poliza',
            old_name='edificio',
            new_name='sector',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='asesor',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='familiar',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fcargo',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fecha_poliza',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fiel',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fmercantil',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fnacimiento',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fpublico',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='fsucargo',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='honorarios',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='micargo',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='nacionalidad',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='noext',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='noint',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='numid',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='otroext',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='parentesco',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='parpublico',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='pnombre',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='resotro',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='rfc',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='rperm',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='rsocial',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='rtemp',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='snombre',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='sucargo',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='tipoid',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='tpersona',
        ),
    ]