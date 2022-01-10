from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from .models import Client, Voiture


# Create your views here.
'''
def index(request):
    template = loader.get_template('index.html')
    data = {'matrielInfo' : ['Laptop','Ipad']}
    return HttpResponse(template.render(data))
'''
def index(request):
    Voitures =  Voiture.objects.all()
    #output = ','.join([m.Modelle for m in Voitures])
    #SELECT * FROM movies_movie
    #Movie.objects.filter(release_year = 1984)
    # SELECT * FROM Voitures_Voiture WHERE
    #output = Voiture.objects.get(id=1) 
    #return HttpResponse(output)
    return render(request , 'gl\index.html',{'voitures': Voitures})


def index1(request):
    Clients =  Client.objects.all()
    return render(request , 'gl\index1.html',{'clients': Clients})
