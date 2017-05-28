# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class ItemInfo(models.Model):
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=50, decimal_places=10)
    material = models.CharField(max_length=1000)
    price = models.IntegerField()
    item_img1 = models.FileField(upload_to='db_img/')
    item_img2  = models.FileField(upload_to='db_img/')
    item_img3  = models.FileField(upload_to='db_img/')
    item_img4  = models.FileField(upload_to='db_img/')  



    def __str__(self):
    	return self.title


    def get_absolute_url(self):
        return "/item/%i/" % self.id


    def get_id(self):
    	return self.id

    def get_chet(self):
        return False if self.id % 2 == 0 else True

 