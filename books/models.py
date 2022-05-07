from django.db import models
from django.urls import reverse
from Djangoecormeceapp.models import MerchantUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    seo_title =  models.CharField(max_length=200,default="Tradebay book detail")
    seo_description =  models.CharField(max_length=200,default="Tradebay book detail")
    url_slug = models.SlugField(blank=True)
    title = models.CharField(max_length=200)
    auther = models.CharField(max_length=200)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    book_file = models.FileField(upload_to='cars')
    book_summary = models.TextField(max_length=500,default="book summury")
    book_thumbnail = models.ImageField(upload_to='cars',default='default.PNG')
    merchant = models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail",args=[self.id])        

class Author(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='cars',default='default.png') 
    dob = models.DateField(auto_created=False) 
    background = models.TextField()

    def __str__(self):
        return self.name