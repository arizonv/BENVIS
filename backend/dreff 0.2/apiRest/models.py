from distutils.command import upload
from pyexpat import model
from django.db import models


class Developer(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
