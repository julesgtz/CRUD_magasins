from django.urls import path
from . import views

urlpatterns = [
path('ajout_magasin/', views.ajout_magasin),
path('traitement_magasin/', views.traitement_magasin),
path('affiche_magasin/<int:id>/',views.affiche_magasin),
path('update_magasin/<int:id>/',views.update_magasin),
path('update_traitement_magasin/<int:id>/',views.update_traitement_magasin),
path('delete_magasin/<int:id>/',views.delete_magasin),

path('ajout_produit/<int:id>/', views.ajout_produit),
path('traitement_produit/<int:id>/', views.traitement_produit),
path('affiche_produit/<int:id>/',views.affiche_produit),
path('update_produit/<int:id>/',views.update_produit),
path('update_traitement_produit/<int:id>/',views.update_traitement_produit),
path('delete_produit/<int:id>/',views.delete_produit),

path('',views.index),
]