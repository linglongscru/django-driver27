# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 08:46
from __future__ import unicode_literals

from django.db import migrations
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('driver27', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='fastest_lap',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(default=False, on=('race',)),
        ),
        migrations.AlterField(
            model_name='seat',
            name='current',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(default=False, on=('contender',)),
        ),
    ]