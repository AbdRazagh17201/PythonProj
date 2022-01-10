from django.urls import path
from . import views 
urlpatterns = [
    path('LesVoitures',views.index),
    path('LesClients',views.index1)
]