from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import MagasinForm,ProduitForm
from . import models
from .models import Magasin


def ajout_magasin(request):
        form = MagasinForm()
        return render(request,"magasinapp/ajout_magasin.html",{"form" : form, "id": id})

def traitement_magasin(request):
    mform = MagasinForm(request.POST)
    if mform.is_valid():
        mag = mform.save()
        return HttpResponseRedirect("/magasin/")
    else:
        return render(request,"magasinapp/ajout_magasin.html",{"form": mform})

def affiche_magasin(request, id):
    mag = models.Magasin.objects.get(pk=id)
    return render(request,"magasinapp/affiche_magasin.html",{"magasin": mag, "id": id})

def update_traitement_magasin(request, id):
    mform = MagasinForm(request.POST)
    if mform.is_valid():
        mag = mform.save(commit=False)
        mag.id = id
        mag.save()
        return HttpResponseRedirect("/magasin/")
    else:
        return render(request, "magasinapp/update_magasin.html", {"form": mform, "id": id})

def update_magasin(request, id):
    magasin = models.Magasin.objects.get(pk=id)
    form = MagasinForm(magasin.dico())
    return render(request,"magasinapp/ajout_magasin.html",{"form":form, "id": id})

def index(request):
    liste = list(models.Magasin.objects.all())
    return render(request,"magasinapp/index.html", {"liste" : liste})

def delete_magasin(request, id):
    magasin = models.Magasin.objects.get(pk=id)
    magasin.delete()
    return HttpResponseRedirect("/magasin/")






def ajout_produit(request, id):
    form = ProduitForm()
    return render(request, "magasinapp/ajout_produit.html", {"form": form, "id": id})


def traitement_produit(request):
    pform = ProduitForm(request.POST)
    if pform.is_valid():
        produit = pform.save()
        return HttpResponseRedirect("/magasin/")
    else:
        return render(request, "magasinapp/ajout_magasin.html", {"form": mform})


def affiche_produit(request, id):
    produit = models.Produit.objects.get(pk=id)
    return render(request, "magasinapp/affiche_magasin.html", {"magasin": produit})


def update_traitement_produit(request, id):
    pform = ProduitForm(request.POST)
    if pform.is_valid():
        produit = pform.save(commit=False)
        produit.id = id
        produit.save()
        return HttpResponseRedirect("/magasin/")
    else:
        return render(request, "magasinapp/update_magasin.html", {"form": produit, "id": id})


def update_produit(request, id):
    produit = models.Produit.objects.get(pk=id)
    form = ProduitForm(produit.dico())
    return render(request, "magasinapp/ajout_magasin.html", {"form": form, "id": id})



def delete_produit(request, id):
    produit = models.Produit.objects.get(pk=id)
    produit.delete()
    return HttpResponseRedirect("/magasin/")

