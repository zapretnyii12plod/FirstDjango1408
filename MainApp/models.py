from django.db import models

# Create your models here.

class Color(models.Model):
   name = models.CharField(max_length=32)

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   description = models.CharField(max_length=255, default='')
   count = models.PositiveIntegerField(),
   colors = models.ManyToManyField(to=Color)

   def __repr__(self):
      return 'Item('+str(self.name)+','+str(self.brand)+','+str(self.description)+','+str(self.count)+')'