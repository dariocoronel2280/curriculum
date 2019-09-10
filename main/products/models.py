from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=200,verbose_name = "titulo")
    description = models.TextField(verbose_name = "descripcion")
    image  = models.ImageField(verbose_name = "imagen", upload_to="productos")
    price = models.DecimalField(verbose_name="precio", name="precio",max_digits=7, default=00.00, decimal_places=5)
    link = models.URLField(null=True, blank=True, verbose_name="direccion whatsapp")
    created = models.DateField(auto_now_add=True,verbose_name = "fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name = "fecha de actualizacion")
    
    

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["created"]

    def __str__(self):
        return self.title

    