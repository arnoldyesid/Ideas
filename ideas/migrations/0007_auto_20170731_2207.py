# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_ideas_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideas',
            old_name='types',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='ideas',
            name='status',
            field=models.CharField(max_length=10, default='published', choices=[('draft', 'Draft'), ('published', 'Published')]),
        ),
    ]
