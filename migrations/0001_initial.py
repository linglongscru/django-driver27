# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('year_of_built', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(blank=True, default=None, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=25)),
                ('year_of_birth', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='driver27.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('full_name', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('competitions', models.ManyToManyField(to='driver27.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='TeamSeasonRel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=75)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver27.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver27.Team')),
            ],
        ),
        migrations.AddField(
            model_name='season',
            name='teams',
            field=models.ManyToManyField(related_name='seasons', through='driver27.TeamSeasonRel', to='driver27.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='driver',
            unique_together=set([('last_name', 'first_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='season',
            unique_together=set([('year', 'competition')]),
        ),
    ]