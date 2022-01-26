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
    path('<int:voiture_id>',views.details,name='details'),
    path('search',views.search,name='search'),
    path('Ajouter',views.Ajouter,name='Ajout'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')


]