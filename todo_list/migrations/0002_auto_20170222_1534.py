# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-22 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='state',
            field=models.CharField(choices=[('todo', 'To Do'), ('doing', 'Doing'), ('done', 'Done')], default='todo', max_length=200),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2, max_length=200),
        ),
    ]
