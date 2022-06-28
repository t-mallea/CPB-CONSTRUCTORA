from django.db import models

# Create your models here.
class Usuario (models.Model):
    nombreCompleto = models.CharField(max_length=50)
    rut = models.models.IntegerField(max_length=20)
    correo = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreCompleto
    
class agendarHora (models.Model):
    fecha = models.IntegerField(max_length=12)    
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    def __str__(self): 
        return self.fecha