# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver27', '0005_auto_20160925_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='competitions',
            field=models.ManyToManyField(to='driver27.Competition'),
        ),
    ]
