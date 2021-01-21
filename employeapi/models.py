# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employer(models.Model):
    nom=models.CharField(max_length=125)
    prenom=models.CharField(max_length=125)
    date_naissance=models.CharField(max_length=100)
    salaire=models.IntegerField()
    genre=models.CharField(max_length=1)
