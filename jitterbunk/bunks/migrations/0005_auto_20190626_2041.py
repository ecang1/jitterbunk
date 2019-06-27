# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-26 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bunks', '0004_auto_20190626_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunks_from_user', to='bunks.UserProfile'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunks_to_user', to='bunks.UserProfile'),
        ),
    ]
