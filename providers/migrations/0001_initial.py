# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('language', models.CharField(max_length=3)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
    ]