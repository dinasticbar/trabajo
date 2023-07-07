from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Producto(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=200)
    oferta = models.BooleanField(default=False)
    
    def tachado(self):
        if self.oferta:
            return "$"+str(round(self.precio * 1.2))
        else:
            return ""
    
    def __str__(self):
        return self.codigo+" - "+self.descripcion