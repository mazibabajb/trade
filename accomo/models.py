from operator import mod
from pydoc import describe
from turtle import mode
from unicodedata import category, name
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    description  = models.TextField(max_length=1000)


    def __str__(self):
        return self.name


class Property_type(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name



class Property(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    number_rooms = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    property_images = models.ImageField(upload_to='cars',default='default.png')
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    property_description = models.TextField(max_length=1000)
    demograpy = models.ForeignKey(Property_type, on_delete=models.CASCADE)
    property_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name