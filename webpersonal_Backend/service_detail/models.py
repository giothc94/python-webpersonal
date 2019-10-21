from django.db import models

# Create your models here.

class ServiceDetail(models.Model):
    title=models.CharField(max_length=200,verbose_name="Servicio")
    content=models.TextField(verbose_name="Detalle del servicio")
    image=models.ImageField(verbose_name="Imagen",upload_to="blogs",null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de cración")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="Detalle de servicio"
        verbose_name_plural="Detalles de servicios"
        ordering=['-created']

    def __str__(self):
        return self.title