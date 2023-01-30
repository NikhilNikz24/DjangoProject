from django.db import models

class Signup(models.Model):
    Name=models.CharField( max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Image(models.Model):
    Name=models.CharField(max_length=10)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Price=models.IntegerField()