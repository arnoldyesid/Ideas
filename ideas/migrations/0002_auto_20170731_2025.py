# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='types',
            field=models.CharField(max_length=15, choices=[('música', 'Música'), ('arte', 'Arte'), ('tecnologia', 'Tecnología'), ('derecho', 'Derecho'), ('medioAmbiente', 'Medio Ambiente'), ('otro', 'Otros')]),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='user_likes',
            field=models.ManyToManyField(default=0, related_name='ideas_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
