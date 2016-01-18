from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    createTime = models.DateField

    def __str__(self):
        return self.name
