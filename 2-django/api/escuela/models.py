from django.db import models
	# Create your models here.

class Escuela(models.Model):
    dni = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.nombre} - {self.dni}"