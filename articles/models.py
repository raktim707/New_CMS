from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Articles(models.Model):

    name = models.CharField(max_length=150)
    short_txt = models.TextField()
    body_text = models.TextField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=12, default="00:00")
    picname = models.TextField()
    vidname = models.TextField()
    picurl = models.TextField(default="-")
    vidurl = models.TextField(default="-")
    writer = models.CharField(max_length=50)
    catname = models.CharField(max_length=50, default="-")
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tag = models.TextField(default="")

    def __str__(self):
        return self.name


class Likes(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    likes = models.IntegerField()

    def __str__(self):
        return str(self.likes)


#link = models.CharField(default="-",max_length=30)
#set_name = models.CharField(default="-",max_length=30)
