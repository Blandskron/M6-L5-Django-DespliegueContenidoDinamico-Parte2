from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion = models.PositiveIntegerField(help_text="Duración en horas")

    def __str__(self):
        return self.nombre
