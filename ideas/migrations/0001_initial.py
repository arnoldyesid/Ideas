# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ideas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('types', models.CharField(max_length=5, choices=[('música', 'Música'), ('arte', 'Arte'), ('tecnologia', 'Tecnología'), ('derecho', 'Derecho'), ('medioAmbiente', 'Medio Ambiente'), ('otro', 'Otros')])),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=10, default='draft', choices=[('draft', 'Draft'), ('published', 'Published')])),
                ('owner', models.ForeignKey(related_name='ideas_created', to=settings.AUTH_USER_MODEL)),
                ('user_likes', models.ManyToManyField(related_name='ideas_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
