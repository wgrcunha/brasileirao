# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0003_auto_20170626_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
