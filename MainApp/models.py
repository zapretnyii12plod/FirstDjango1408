from django.db import models

# Create your models here.

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   description = models.CharField(max_length=255, default='')
   count = models.PositiveIntegerField() 

