# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-12 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
        ('flowcell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowcell',
            name='requests',
            field=models.ManyToManyField(blank=True, related_name='flowcell', to='request.Request'),
        ),
    ]
