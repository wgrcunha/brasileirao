# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('rodada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goals_pro', models.IntegerField()),
                ('goals_con', models.IntegerField()),
                ('points', models.IntegerField()),
                ('goals_sal', models.IntegerField()),
                ('cup', models.ForeignKey(to='brasileirao.Cup')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='team',
            field=models.ForeignKey(to='brasileirao.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='away',
            field=models.ForeignKey(related_name='team_away', to='brasileirao.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='cup',
            field=models.ForeignKey(to='brasileirao.Cup'),
        ),
        migrations.AddField(
            model_name='game',
            name='home',
            field=models.ForeignKey(related_name='team_home', to='brasileirao.Team'),
        ),
    ]
