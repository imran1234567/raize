# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-30 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='contact_no',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='email_id',
            field=models.EmailField(default=1, max_length=170),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='membership',
            name='food_pref',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Non Veg', 'Non Veg')], default='Veg', max_length=20),
        ),
        migrations.AddField(
            model_name='membership',
            name='material_status',
            field=models.CharField(choices=[('marraige', 'Marriage'), ('single', 'Single')], default='marraige', max_length=20),
        ),
    ]