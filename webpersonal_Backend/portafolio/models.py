from django.db import models

# Create your models here.
class Portafolio(models.Model):
    title=models.CharField(max_length=200,verbose_name="Título")
    content=models.TextField(max_length=200,verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen",upload_to="portafolio")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de cración")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")
    
    class Meta:
            verbose_name="proyecto"
            verbose_name_plural="portafolio"
            ordering=['-created']

    def __str__(self):
        return self.title
