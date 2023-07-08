from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    edad = models.IntegerField()
    numero_telefono = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='core/img')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido
