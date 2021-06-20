# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Twitter_Streams(models.Model):
    created_at = models.DateTimeField()
    text = models.CharField(max_length= 800)
    compound_score = models.DecimalField(max_digits= 4, decimal_places= 2) 