# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-29 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index_generator', '0002_load_pool_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flowcell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowcell_id', models.CharField(max_length=50, verbose_name='Flowcell ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6, verbose_name='Name')),
                ('loading_concentration', models.FloatField(blank=True, null=True, verbose_name='Loading Concentration')),
                ('phix', models.FloatField(blank=True, null=True, verbose_name='PhiX %')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index_generator.Pool', verbose_name='Pool')),
            ],
        ),
        migrations.CreateModel(
            name='Sequencer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('lanes', models.PositiveSmallIntegerField(verbose_name='Number of Lanes')),
                ('lane_capacity', models.PositiveSmallIntegerField(verbose_name='Lane Capacity')),
            ],
        ),
        migrations.AddField(
            model_name='flowcell',
            name='lanes',
            field=models.ManyToManyField(blank=True, related_name='flowcell', to='flowcell.Lane'),
        ),
        migrations.AddField(
            model_name='flowcell',
            name='sequencer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowcell.Sequencer', verbose_name='Sequencer'),
        ),
    ]
