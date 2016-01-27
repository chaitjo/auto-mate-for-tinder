from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TinderUser(models.Model):
    user_full_name = models.CharField(max_length=200)
    fb_auth_token = models.CharField(max_length=200)
    fb_id = models.CharField(max_length=200)
    photo_percentage = models.FloatField(default=50)

class Image(models.Model):
    photo_url0 = models.CharField(max_length=200)
    photo_looks0 = models.FloatField(default=50)
    
    photo_url1 = models.CharField(max_length=200)
    photo_looks1 = models.FloatField(default=50)
    
    photo_url2 = models.CharField(max_length=200)
    photo_looks2 = models.FloatField(default=50)
    
#class Image3(models.Model):
#    photo_url0 = models.CharField(max_length=200)
#    photo_looks0 = models.FloatField(default=50)
#
#class Image4(models.Model):
#    photo_url0 = models.CharField(max_length=200)
#    photo_looks0 = models.FloatField(default=50)
#    
#class Image5(models.Model):
#    photo_url0 = models.CharField(max_length=200)
#    photo_looks0 = models.FloatField(default=50)
#    
#class Image6(models.Model):
#    photo_url0 = models.CharField(max_length=200)
#    photo_looks0 = models.FloatField(default=50)
#
#class Image7(models.Model):
#    photo_url0 = models.CharField(max_length=200)
#    photo_looks0 = models.FloatField(default=50)
#    
#class Image8(models.Model):
#    photo_url0 = models.CharField(max_length=200)
#    photo_looks0 = models.FloatField(default=50)