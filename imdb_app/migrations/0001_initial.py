# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('imdb_score', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('genre', models.ManyToManyField(to='imdb_app.GenreCategory')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('access_type', models.CharField(max_length=50, choices=[(b'Normal', b'Normal'), (b'Admin', b'Admin')])),
            ],
        ),
    ]
