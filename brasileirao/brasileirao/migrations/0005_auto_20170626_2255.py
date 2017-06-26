# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0004_game_game_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='lost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='percent',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='win',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
