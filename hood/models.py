from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length =30)
    occupants = models.PositiveIntegerField()
    health_contact =  models.PositiveIntegerField()
    police_contact = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    
