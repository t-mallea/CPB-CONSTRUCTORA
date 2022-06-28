from typing_extensions import runtime
from django.db import models

# Create your models here.
class Usuario (models.Model):
    nombreCompleto = models.CharField(max_length=50)
    rut = models.IntegerField(max_length=20)
    correo = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=20)