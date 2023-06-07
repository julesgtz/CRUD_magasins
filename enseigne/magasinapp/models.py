from django.db import models
class Magasin(models.Model):
    nom_magasin = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True) # champs de type text long
    def __str__(self):
        chaine = f"{self.nom_magasin} a bien été ajouté"
        return chaine
    def dico(self):
        return {"nom_magasin": self.nom_magasin, "description": self.description}

class Produit(models.Model):
    magasin = models.ForeignKey("magasin", on_delete=models.CASCADE, default=None)
    nom_produit = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True) # champs de type text long
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        chaine = f"{self.nom_produit} a bien été ajouté au prix de {self.prix}"
        return chaine
    def dico(self):
        return {"nom_produit": self.nom_produit, "description": self.description, "prix": self.prix, "magasin": self.magasin}