# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-05-30 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_membership_aniversary_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='membership_card',
            field=models.CharField(choices=[('gold', 'Gold'), ('silver', 'Silver'), ('platinum', 'Platinum')], default='silver', max_length=20),
        ),
    ]