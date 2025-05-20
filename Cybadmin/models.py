from django.db import models

#Création du model Poste
class Poste(models.Model):    
    nom  = models.CharField(max_length=100, unique=True)
    etat = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
