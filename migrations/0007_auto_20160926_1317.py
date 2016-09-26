# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver27', '0006_team_competitions'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver27.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver27.Team')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='teams_aux',
            field=models.ManyToManyField(related_name='_season_teams_aux_+', through='driver27.TeamSeason', to='driver27.Team'),
        ),
    ]
