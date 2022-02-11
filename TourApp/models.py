from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DurationField, EmailField
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from sqlalchemy import null

# Create your models here.

class users (models.Model):
    userId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    nationality = models.CharField(max_length=100)
    languages = models.CharField(max_length=250)
    photo = models.ImageField(null=True,upload_to='static')
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

class admin (models.Model):
    adminId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    photo = models.ImageField(null=True,upload_to='static')
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

class category(models.Model):
    categories = models.CharField(primary_key=True,max_length=150)

# def __str__(    self): 
#         return category.categories

class destinations (models.Model):
    destinationId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500,default='')
    name= models.CharField(max_length=150)
    longitude = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    categori = models.ForeignKey(category, related_name="category",on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    imageurl = models.URLField()
    url = models.CharField(max_length=100,default='')
    rating = models.IntegerField(default=3)

class hotels (models.Model):
    hotelId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500,default='')
    name= models.CharField(max_length=150)
    location = models.CharField(max_length=250, default= null)
    city = models.CharField(max_length=250, default= null)
    rating = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    imageurl = models.URLField()
    url = models.CharField(max_length=100,default='')
    rating = models.IntegerField(default=3)

class status(models.Model):
    state = models.CharField(primary_key=True,max_length=150)

    # def __str__(self): 
    #     return status.state

class tourguide (models.Model):
    userId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    languages = models.CharField(max_length=250)
    photo = models.ImageField(null=True,upload_to='static')
    email = models.EmailField()
    speciality = models.ForeignKey(category, related_name="speciality",on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    status = models.ForeignKey(status, related_name="status",on_delete=models.CASCADE)

class bookings(models.Model):
    bookingId = models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    tourguide = models.CharField(max_length=100)
    date= models.DateField()
    Duration= DurationField()  
    destination= models.CharField(max_length=100)
    bill = models.PositiveIntegerField() 