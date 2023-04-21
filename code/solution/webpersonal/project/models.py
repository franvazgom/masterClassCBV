from django.db import models
from django.utils import timezone

class ProjectType(models.Model):
    project_type = models.CharField(max_length=100, verbose_name="Tipo de proyecto")
    
    def __str__(self):
        return self.project_type

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del proyecto")
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to='project_images', verbose_name="Imágen")
    created = models.DateField(default=timezone.now, verbose_name="Fecha")

    def __str__(self):
        return self.name