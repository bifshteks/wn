# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_item_info', '0009_auto_20170528_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteminfo',
            name='item_img1',
        ),
        migrations.RemoveField(
            model_name='iteminfo',
            name='item_img2',
        ),
        migrations.RemoveField(
            model_name='iteminfo',
            name='item_img3',
        ),
        migrations.RemoveField(
            model_name='iteminfo',
            name='item_img4',
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='ext_img1',
            field=models.CharField(default='jpg', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='ext_img2',
            field=models.CharField(default='jpg', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='ext_img3',
            field=models.CharField(default='jpg', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='ext_img4',
            field=models.CharField(default='jpg', max_length=10),
            preserve_default=False,
        ),
    ]
