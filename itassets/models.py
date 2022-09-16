from pyexpat import model
from django.db import models

class Itasset(models.Model):
    itemnumber = models.CharField(max_length=300)
    assetname = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField(max_length=300)
    quantity = models.FloatField(max_length=300)
    borrowersname = models.CharField(max_length=300)

    def __str__(self):
        return self.itemnumber + ' ' + self.assetname + ' ' + self.description + ' ' + self.borrowersname

