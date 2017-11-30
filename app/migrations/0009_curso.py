# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20171026_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dificultad', models.CharField(choices=[('1', 'Principiante'), ('2', 'Basico'), ('3', 'Intermedio'), ('4', 'Avanzado')], max_length=30)),
                ('foto', models.ImageField(upload_to='images')),
                ('descripcion', models.TextField(max_length=270)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Alumnos')),
                ('maestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Maestros')),
            ],
        ),
    ]
