from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

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


class Match(models.Model):
    remite = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_enviados')
    destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_recibidos')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.remite.username} -> {self.destino.username}'

class Mensaje(models.Model):
    remite = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    id_mensaje = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.remite.username} -> {self.destino.username}'