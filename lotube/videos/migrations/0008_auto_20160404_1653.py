# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20160403_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractthumbnail',
            name='url',
            field=models.CharField(blank=True, default=b'', max_length=255),
        ),
    ]
