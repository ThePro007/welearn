# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20171029_0522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumnos',
            name='curso',
        ),
        migrations.AddField(
            model_name='alumnos',
            name='curso',
            field=models.ManyToManyField(null=True, to='app.Curso'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Curso'),
        ),
    ]
