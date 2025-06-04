from django.db import models

#Création du model Poste
class Poste(models.Model):    
    nom  = models.CharField(max_length=100, unique=True)
    ip = models.CharField(max_length=100,unique=True)
    etat = models.CharField(max_length=20,default="hors_ligne")

    def __str__(self):
        return self.nom
