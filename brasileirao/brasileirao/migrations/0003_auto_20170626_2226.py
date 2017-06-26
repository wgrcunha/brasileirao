# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0002_auto_20170626_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_score',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_score',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
