from django.contrib import admin
from .models import Client, Contrat, Location, Voiture
# Register your models here.
class VoitureAff(admin.ModelAdmin):
    list_display = ('immt','Modelle','Marque','Couleur','disponible')
class ContratAff(admin.ModelAdmin):
    list_display = ('NumContr','DateContr','DateDeb','DateFin','voiture','client','Km_Parcours','Tarif_Par_jour')

class ClientAff(admin.ModelAdmin):
    list_display = ('user','Numero_Permis','Adresse','Telephon')
class LocatAff(admin.ModelAdmin):
    list_display = ('NumLocat','DateLocat','dureeLocat','Locataire','voiture')
admin.site.register(Voiture,VoitureAff)
admin.site.register(Client,ClientAff)
admin.site.register(Location,LocatAff)
admin.site.register(Contrat,ContratAff)
