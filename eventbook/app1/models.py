from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)

    ROLE_CHOICE = (
        ('admin','admin'),
        ('user','user'),
    )
    role = models.CharField(max_length=50,choices=ROLE_CHOICE,default='user')

class event_category(models.Model):
    name = models.CharField(max_length=50)
    c_image = models.ImageField(upload_to='event_cat')

    def __str__(self):
        return self.name
    
class Events(models.Model):
    title = models.CharField(max_length=50)
    event_cat = models.ForeignKey(event_category,on_delete=models.CASCADE)
    location = models.TextField(null=True)
    e_image = models.ImageField(upload_to='events')

    def __str__(self):
        return self.title

