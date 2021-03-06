# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_uploads'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploads',
            old_name='url',
            new_name='name',
        ),
        migrations.AddField(
            model_name='uploads',
            name='file',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='uploads',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
