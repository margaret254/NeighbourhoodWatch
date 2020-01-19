from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length =30)
    occupants = models.PositiveIntegerField()
    health_contact =  models.CharField(max_length = 30)
    police_contact = models.CharField(max_length = 30)
    hood_pic = models.ImageField(upload_to='images/', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.CharField(max_length = 30)
    post = HTMLField()

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    hood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
