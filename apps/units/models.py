from django.db import models

# Create your models here.

class Unit(models.Model):
    """docstring here"""
    name = models.CharField(max_length=40)
    status = models.BooleanField()
    desc = models.CharField(max_length=200)

    def __str__(self):
        return"{}".format(self.name)