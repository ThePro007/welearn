# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20171127_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='foto',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]