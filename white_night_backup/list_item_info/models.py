# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models

class ItemInfo(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=6, decimal_places=0) 
    material = models.CharField(max_length=255) 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/catalog/%i/" % self.id
