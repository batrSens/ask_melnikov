# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0006_auto_20171114_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ask.User'),
        ),
    ]