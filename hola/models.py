from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    fecha_mensaje = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre


    