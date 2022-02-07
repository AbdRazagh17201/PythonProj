from django.urls import path
from . import views

app_name = 'GL'
urlpatterns = [
    path('log',views.login),
    path('index',views.index,name='index1'),
    path('AV',views.AjoutVoi),
    path('AC',views.AjoutClient),
    path('Afficher',views.Affiche),
    path('AL',views.AjoutLocat),
    path('ACon',views.AjoutContra),
    path('<int:id>',views.details,name='details'),
    path('DetailCli<int:id>',views.detailsClient,name='details1'),
    path('DetailLoc<int:id>',views.detailsLocation,name='details2'),
    path('DetailCon<int:id>',views.detailsContra,name='details3'),
    path('search',views.search,name='search'),
    path('Ajouter',views.Ajouter,name='Ajout'),
    path('update/<int:id>',views.update,name='update'),
    path('updateClient/<int:id>',views.updateClient,name='update1'),
    path('updateLocation/<int:id>',views.updateLoc,name='update2'),
    path('updateContra/<int:id>',views.updateCont,name='update3'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('deleteClient/<int:id>',views.deleteClient,name='delete1'),
    path('deleteLocation/<int:id>',views.deleteLoc,name='delete2'),
    path('deleteContra/<int:id>',views.deleteContra,name='delete3')


]