# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-18 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_auto_20200118_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='admin',
        ),
    ]