from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=200,verbose_name = "titulo")
    description = models.TextField(verbose_name = "descripcion")
    image  = models.ImageField(verbose_name = "imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="direccion web")
    created = models.DateField(auto_now_add=True,verbose_name = "fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name = "fecha de actualizacion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["created"]

    def __str__(self):
        return self.title      