# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='tema',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
