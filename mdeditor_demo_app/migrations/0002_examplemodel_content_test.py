# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdeditor_demo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='content_test',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]