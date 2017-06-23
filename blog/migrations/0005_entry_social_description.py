# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='social_description',
            field=models.CharField(default=django.utils.timezone.now, max_length=140),
            preserve_default=False,
        ),
    ]