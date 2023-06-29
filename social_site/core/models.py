from django.db import models

# Create your models here.
    
class Logo (models.Model):
     immagine= models.ImageField(null=True)
