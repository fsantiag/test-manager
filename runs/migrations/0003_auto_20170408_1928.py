# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0002_auto_20170408_1922'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='environment',
            table='environment',
        ),
        migrations.AlterModelTable(
            name='run',
            table='run',
        ),
        migrations.AlterModelTable(
            name='status',
            table='status',
        ),
        migrations.AlterModelTable(
            name='test',
            table='test',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
