from django.db import models

# Create your models here.
class Portador(models.Model):
    CUIP = models.CharField(max_length=20, primary_key=True)
    NOMBRE = models.CharField(max_length=30,blank=False)
    APELLIDO_PATERNO = models.CharField(max_length=30,blank=False)
    APELLIDO_MATERNO = models.CharField(max_length=30,blank=False)
    CORREO = models.EmailField(max_length=254,blank=False)
    TELEFONO = models.CharField(max_length=10,blank=False)
    IMAGEN = models.FileField(upload_to='images/portadores/',blank=False)
    
    def __str__(self):
        return f"{self.CUIP} - {self.NOMBRE} {self.APELLIDO_PATERNO} {self.APELLIDO_MATERNO}"

    
    
class LogPortador(models.Model):
    id_registro = models.AutoField(primary_key=True)
    accion = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    # Heredar los campos de Portador
    CUIP = models.CharField(max_length=20)
    NOMBRE = models.CharField(max_length=30,blank=False)
    APELLIDO_PATERNO = models.CharField(max_length=30,blank=False)
    APELLIDO_MATERNO = models.CharField(max_length=30,blank=False)
    CORREO = models.EmailField(max_length=254,blank=False)
    TELEFONO = models.CharField(max_length=10,blank=False)
    IMAGEN = models.FileField(upload_to='images/portadores/',blank=False)   