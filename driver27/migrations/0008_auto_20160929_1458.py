# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver27', '0007_auto_20160929_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivercompetition',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career', to='driver27.Competition'),
        ),
        migrations.AlterField(
            model_name='drivercompetition',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career', to='driver27.Driver'),
        ),
        migrations.AlterField(
            model_name='drivercompetitionteam',
            name='enrolled',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='squad', to='driver27.DriverCompetition'),
        ),
        migrations.AlterField(
            model_name='drivercompetitionteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partners', to='driver27.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='competitions',
            field=models.ManyToManyField(related_name='teams', to='driver27.Competition'),
        ),
    ]