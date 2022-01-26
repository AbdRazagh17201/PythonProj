from mysite.settings import TIME_ZONE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.fields import DateField
# Create your models here.
        
class Voiture(models.Model):
    immt = models.CharField(max_length=10)
    Modelle = models.CharField(max_length=15)
    Marque = models.CharField(max_length=25)
    Couleur = models.CharField(max_length=30)
    photo = models.FileField( upload_to = "Photos" )
    disponible = models.BooleanField()

    def __str__(self):
        return self.immt
    
class Client(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    Numero_Permis = models.CharField(max_length=200)
    Adresse = models.CharField(max_length=30)
    Telephon = models.CharField(max_length=25)

    def __str__(self):
        return self.user.first_name

class Location(models.Model):
    NumLocat = models.CharField(max_length=39)
    DateLocat = models.DateField()
    dureeLocat = models.IntegerField()
    Locataire = models.ForeignKey(Client , on_delete = models.CASCADE)
    voiture = models.ForeignKey(Voiture , on_delete = models.CASCADE)

    def __str__(self):
        return self.NumLocat

class Contrat(models.Model):
    NumContr = models.CharField(max_length=39)
    DateContr = models.DateTimeField(default=timezone.now)
    DateDeb =  models.DateTimeField(default=timezone.now)
    DateFin =  models.DateTimeField(default=timezone.now)
    voiture = models.ForeignKey(Voiture , on_delete = models.CASCADE)
    client = models.ForeignKey(Client , on_delete = models.CASCADE)
    Km_Parcours = models.FloatField()
    Tarif_Par_jour = models.FloatField()

    def __str__(self):
        return self.NumContr

