# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-19 05:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0007_auto_20200118_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='post',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
