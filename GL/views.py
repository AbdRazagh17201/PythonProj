from multiprocessing import context
from django import template
from django.core.checks import messages
from django.db.models.base import Model
from django.db.models import Q
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Client, Voiture
from .formulaire import *

@login_required
def AjoutVoi(request):
    if request.method == "POST":
        form = VoitureForm(request.POST, request.FILES)
        # msg =''
        if form.is_valid():
            form.save()
        return redirect('GL:index1')
            # msg = "Ok"
    else:
        form = VoitureForm()
    
    voitures = Voiture.objects.filter(disponible = True) 
    return render(request , 'AjouterVoiture.html' , {'form' : form , 'voitures':voitures })

# def index(request):
#     Voitures =  Voiture.objects.all()
#     #output = ','.join([m.Modelle for m in Voitures])
#     #SELECT * FROM movies_movie
#     #Movie.objects.filter(release_year = 1984)
#     # SELECT * FROM Voitures_Voiture WHERE
#     #output = Voiture.objects.get(id=1) 
#     #return HttpResponse(output)
#     return render(request , 'gl\index.html',{'voitures': Voitures})

@login_required
def AjoutClient(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm()
    return render(request , 'AjoutClient.html' , {'form' : form , 'dataclients':Client.objects.all()})

@login_required
def AjoutLocat(request):
    if request.method == "POST":
        form = LocatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = LocatForm()
    return render(request , 'AjoutLocat.html' , {'form' : form , 'datalocate':Location.objects.all()})

@login_required
def AjoutContra(request):
    if request.method == "POST":
        form1 = ContraForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
    else:
        form1 = ContraForm()
    return render(request , 'AjoutContra.html' , {'form1' : form1 , 'datacontra':Contrat.objects.all()})

@login_required
def Affiche(request):
    voitures = Voiture.objects.all()
    clients = Client.objects.all()
    locations = Location.objects.all()
    contras = Contrat.objects.all()
    voitures_number = voitures.count()
    message = f'Il y a {voitures_number} Voitures :'
    Client_number = clients.count()
    message1 = f'Il y a {Client_number} Clients :'
    Location_number = locations.count()
    message2 = f'Il y a {Location_number} Locations :'
    Contra_number = contras.count()
    message3 = f'Il y a {Contra_number} Contras :'
    context = { 
        'voitures': voitures,
        'dataclients':clients,
        'message': message,
        'datalocate':locations,
        'datacontra':contras,
        'message1':message1,
        'message2':message2,
        'message3':message3,
    }
    return render(request , 'Afficher.html' ,context)
    
# def inscrire(request):
#     return render(request , 'home.html',{'dataadmin':Client.objects.filter(user_id = 1) })

@login_required
def login(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request , 'home.html',{})
        else:
                return render(request , 'home.html',{})
    else:
        return redirect('index')

@login_required
def index(request):
    voitures = Voiture.objects.all()
    voitures_number = voitures.count()
    message = f'Il y a {voitures_number} Voitures :'
    context = { 
        'voitures': voitures,
        'message': message,

    }
    return render(request , 'index.html',context)

@login_required
def details(request,id):
    voitures = Voiture.objects.get(pk=id)
    # clients = Client.objects.get(pk=id)
    # contras = Contrat.objects.get(pk=id)
    # locations = Location.objects.get(pk=id)
    # #msg = "Les donnees est ici :immt {}. Modelle {}. Marque {} .Couleur {}. Disponible {}".format( voitures.immt,voitures.Modelle,voitures.Marque,voitures.Couleur,voitures.disponible )
    # # Context = {
    # #     'voitures_immt' : voitures.immt,
    # #     'voitures_Modelle' : voitures.Modelle,
    # #     'voitures_Marque' : voitures.Marque,
    # #     'voitures_Couleur' : voitures.Couleur,
    # #     'voitures_disponible' : voitures.disponible,
    # #     'voitures_photo' : voitures.photo
    # # }
    # # return HttpResponse(Context)
    # context = { 
    #     'voitures': voitures,
    #     'clients': clients,
    #     'contras': contras,
    #     'locations': locations

    # }
    return render(request , 'details.html', {'voitures':voitures})


def detailsClient(request,id):
    clients = Client.objects.get(id=id)
    return render(request , 'detailsClient.html', {'clients':clients})

def detailsLocation(request,id):
    location = Location.objects.get(pk=id)
    return render(request , 'detailsLocation.html', {'location':location})

def detailsContra(request,id):
    contra = Contrat.objects.get(pk=id)
    return render(request , 'detailsContra.html', {'contra':contra})



@login_required  
def search(request):
    search = request.GET.get('search')
    voitures = Voiture.objects.filter(Q(immt__icontains=search) |
                                     Q(Modelle__icontains =search) |
                                     Q(Marque__icontains =search)  |
                                     Q(Couleur__icontains =search))
    # clients = Client.objects.filter(Q(user=search) |
    #                                  Q(Numero_Permis =search) |
    #                                  Q(Adresse =search))
    voitures_number = voitures.count()
    message = f'Il y a {voitures_number} Voitures :'
    context = { 
        'voitures': voitures,
        'message': message,
        # 'clients': clients

    }
    return render(request , 'search.html',context)

@login_required
def Ajouter(request):
    return render(request , 'Ajouter.html')

def update(request,id):
    voiture = Voiture.objects.get(id=id)
    if request.method == "POST":
        form = VoitureForm(request.POST, request.FILES, instance=voiture)
        if form.is_valid():
            form.save()
            return redirect('GL:index1')
    else:
        form = VoitureForm(instance=voiture)
    context = {
        'form': form,
        'voiture': voiture,
    }
    return render(request , 'Update.html' , context)

def updateClient(request,id):
    client = Client.objects.get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('GL:index1')
    else:
        form = ClientForm(instance=client)
    context = {
        'form': form,
        'client': client,
    }
    return render(request , 'UpdateClient.html' , context)

def updateLoc(request,id):
    location = Location.objects.get(id=id)
    if request.method == "POST":
        form = LocatForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            return redirect('GL:index1')
    else:
        form = LocatForm(instance=location)
    context = {
        'form': form,
        'location': location,
    }
    return render(request , 'UpdateLocation.html' , context)


def updateCont(request,id):
    contra = Contrat.objects.get(id=id)
    if request.method == "POST":
        form = ContraForm(request.POST, request.FILES, instance=contra)
        if form.is_valid():
            form.save()
            return redirect('GL:index1')
    else:
        form = ContraForm(instance=contra)
    context = {
        'form': form,
        'contra': contra,
    }
    return render(request , 'UpdateContra.html' , context)

def delete(request,id):
    voiture = Voiture.objects.get(id=id)
    voiture.delete()
    return redirect('GL:index1')
    return render(request , 'Delete.html')

def deleteClient(request,id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('GL:index1')
   
def deleteLoc(request,id):
    location = Location.objects.get(id=id)
    location.delete()
    return redirect('GL:index1')
   

def deleteContra(request,id):
    contra = Contrat.objects.get(id=id)
    contra.delete()
    return redirect('GL:index1')
