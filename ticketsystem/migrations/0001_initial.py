# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('seat_num', models.IntegerField()),
                ('rider_num', models.IntegerField()),
            ],
        ),
    ]