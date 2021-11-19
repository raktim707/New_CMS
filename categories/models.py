from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categories(models.Model):

 name = models.CharField(max_length=50)
 count = models.IntegerField(default=0)
 
 
 def __str__(self):
  return self.name 
  
  
  
  
  
  
  
#link = models.CharField(default="-",max_length=30)
#set_name = models.CharField(default="-",max_length=30)