# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-29 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disk',
            name='capacity',
            field=models.CharField(max_length=32, verbose_name='磁盘容量GB'),
        ),
    ]
