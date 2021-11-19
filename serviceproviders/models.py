from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ServiceProviders(models.Model):

 name = models.CharField(max_length=50)
 occupation = models.TextField()
 organization = models.TextField()
 suburb = models.TextField()
 address = models.CharField(max_length=50)
 sptell = models.CharField(max_length=15)
 spimagename = models.TextField(default="-")
 spimageurl = models.TextField(default="-")
 
 
 def __str__(self):
  return self.name 
  
  
  
  
  
  
  
#link = models.CharField(default="-",max_length=30)
#set_name = models.CharField(default="-",max_length=30)