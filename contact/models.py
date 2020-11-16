from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Formation(models.Model):
    titre = models.CharField(max_length=150)
    def __str__(self):
        return self.titre


class Ville(models.Model):
    titre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titre
        

class Contact(AbstractUser):
    username = None
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    email = models.EmailField(max_length = 254, unique=True)
    telephone = models.CharField(max_length=16)
    ville = models.ForeignKey(Ville,on_delete=models.CASCADE)
    societe = models.CharField(max_length=150,blank=True)
    fonction = models.CharField(max_length=150,blank=True)
    formation = models.ForeignKey(Formation,on_delete=models.CASCADE)
    presence = models.CharField(max_length=150)
 
    message = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

   

    def __str__(self):
        return self.email