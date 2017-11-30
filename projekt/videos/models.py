# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tutorial(models.Model):
    author = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.author + ' "'+ self.title+'"'


class Movie(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    part_number = models.CharField(max_length=10)