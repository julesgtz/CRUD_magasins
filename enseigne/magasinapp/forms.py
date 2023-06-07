from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class MagasinForm(ModelForm):
    class Meta:
        model = models.Magasin
        fields = ('nom_magasin', 'description')
        labels = {
        'nom_magasin' : _('Nom Magasin'),
        'description' : _('Description') ,
        }

class ProduitForm(ModelForm):
    class Meta:
        model = models.Produit
        fields = ('nom_produit', 'description','prix','magasin')
        labels = {
        'nom_produit' : _('Nom Produit'),
        'description' : _('Description') ,
        'prix' : _('Prix'),
        'magasin' : _('Magasin'),
        }