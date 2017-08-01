# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0002_auto_20170731_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='user_likes',
            field=models.ManyToManyField(related_name='ideas_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
