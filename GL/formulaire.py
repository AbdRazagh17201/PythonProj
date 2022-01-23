from django.db.models import fields
from django.forms import ModelForm
from .models import *
# Voiture ,Client,Location,Contrat

class VoitureForm(ModelForm):
    class Meta:
        model = Voiture
        # fields = ['immt','Modelle','Marque','Couleur','photo','disponible']
        fields = '__all__'
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['user','Numero_Permis','Adresse','Telephon']
class LocatForm(ModelForm):
    class Meta:
        model = Location
        fields = ['NumLocat','DateLocat','dureeLocat','Locataire','voiture']
class ContraForm(ModelForm):
    class Meta:
        model = Contrat
        fields = ['NumContr','DateContr','DateDeb','DateFin','voiture','client','Km_Parcours','Tarif_Par_jour']