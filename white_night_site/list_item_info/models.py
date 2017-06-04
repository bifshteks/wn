# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def set_name_img(count):
    # # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # s = filename.split('.')
    # ext = s[1:]
    # name = instance.id + '_'
    # # res_name = instance.id + '_' +  ext

    # return name, ext
    # # return '{0}'.format(instance.id, filename)
    return item.get_id + '_' + count

class ItemInfo(models.Model):
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=1000)
    price = models.IntegerField()
    # for i in range(1, 5):
    #     exec('img' + i + ' = models.FileField(upload_to=set_name_img()[0] + '1' + set_name_img[1])')

    img1 = models.FileField(upload_to='')
    img2 = models.FileField(upload_to='')
    img3 = models.FileField(upload_to='')
    img4 = models.FileField(upload_to='')
    description = models.TextField() 



    def __str__(self):
    	return self.title


    def get_absolute_url(self):
        return "/item/%i/" % self.id


    def get_id(self):
    	return self.id

    def get_chet(self):
        return False if self.id % 2 == 0 else True

 