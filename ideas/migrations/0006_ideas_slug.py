# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_auto_20170731_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideas',
            name='slug',
            field=models.SlugField(max_length=200, blank=True),
        ),
    ]
