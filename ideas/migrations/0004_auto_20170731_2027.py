# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_auto_20170731_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
