from django.db import models

# Create your models here.
class User(models.Model):
    
    first_name = models.CharField(max_length=30) 
    last_name= models.CharField(max_length=30)
    username= models.CharField(max_length=30,default="")
    email = models.EmailField(max_length=50) 
    password = models.CharField(max_length=32) 
    repassword = models.CharField(max_length=32) 