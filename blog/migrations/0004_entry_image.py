# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 22:09
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entry_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=blog.models.upload_to_entry),
        ),
    ]
