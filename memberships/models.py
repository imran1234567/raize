from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.forms import TextInput
from django.utils import timezone

# Create your models here.

class Membership(models.Model):
    Marriage = 'marraige'
    Single = 'single'
    VEG = 'Veg'
    NON_VEG = 'Non Veg'
    GOLD = 'gold'
    SILVER = 'silver'
    PLATINUM = 'platinum'
    MAT_STAT = (
        (Marriage, 'Marriage'),
        (Single, 'Single'),
    )

    FOOD_PREF = (
        (VEG, 'Veg'),
        (NON_VEG,'Non Veg' )
    )

    MEMBERSHIP_CARD = (
    (GOLD, 'Gold'),
    (SILVER, 'Silver'),
    (PLATINUM, 'Platinum'),
    )
    name = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=170)
    address = models.CharField(max_length=255)
    dob = models.DateField(max_length=8)
    aniversary_date = models.DateField(max_length=8)
    material_status = models.CharField(max_length=20, choices=MAT_STAT,default=Marriage)
    food_pref = models.CharField(max_length=20, choices=FOOD_PREF, default=VEG)
    membership_card = models.CharField(max_length=20, choices=MEMBERSHIP_CARD, default=SILVER)


    def __str__(self):
        return str(self.email)
