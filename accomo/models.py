
from django.db import models
from Djangoecormeceapp.models import CustomUser,AdminUser,CustomerUser,MerchantUser



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
    seo_title =  models.CharField(max_length=200,default="Tradebay property detail")
    seo_description =  models.CharField(max_length=200,default="Tradebay property detail")
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
    liked = models.ManyToManyField(CustomUser, default=None,blank=True,related_name='likes')
    
    
    @property
    def number_of_likes(self):
        return self.liker.all().count()
    

    def __str__(self):
        return self.name


LIKED_CHOICES = (
	('like','like'),
	('Liked','Liked')
)

class Like(models.Model):
	users = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="liking_user")	
	property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name="liked_property")
	value = models.CharField(choices= LIKED_CHOICES , default="Liked",max_length=100)

	def __str__(self):
		return self.property    

class Property_images(models.Model):
    product_id = models.ForeignKey(Property,on_delete=models.CASCADE,related_name="pictures")
    property_img = models.ImageField(upload_to='cars')  


    def __str__(self):
        return self.product_id

class PropertyViewCount(models.Model):
    property = models.ForeignKey(Property,related_name="property_veiw_count", on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100)
    session = models.CharField(max_length=100,)

    def __str__(self):
        return f"{self.ip_address}"






