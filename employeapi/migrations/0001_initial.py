# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-21 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=125)),
                ('prenom', models.CharField(max_length=125)),
                ('date_naissance', models.CharField(max_length=100)),
                ('salaire', models.IntegerField()),
                ('genre', models.CharField(max_length=1)),
            ],
        ),
    ]
