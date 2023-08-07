from django.db import models

# Create your models here.
class Portador(models.Model):
    CUIP = models.CharField(max_length=20, primary_key=True)
    NOMBRE = models.CharField(max_length=30,blank=False)
    APELLIDO_PATERNO = models.CharField(max_length=30,blank=False)
    APELLIDO_MATERNO = models.CharField(max_length=30,blank=False)
    CORREO = models.EmailField(max_length=254,blank=False)
    TELEFONO = models.CharField(max_length=10,blank=False)
    IMAGEN = models.FileField(upload_to='portadores/imagenes/',blank=False)
    
    def __str__(self):
        return f"{self.CUIP} - {self.NOMBRE} {self.APELLIDO_PATERNO} {self.APELLIDO_MATERNO}"
    
    def delete(self, using=None, Keep_parents=False):
        self.IMAGEN.storage.delete(self.IMAGEN.name)
        super().delete()
    