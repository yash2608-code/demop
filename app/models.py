from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=25,default="Username")
    email = models.EmailField(max_length=25,default="Email")
    password = models.CharField(max_length=25,default="Password")