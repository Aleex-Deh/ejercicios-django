from django.db import models

# Create your models here.

class Biblioteca(models.Model):
    titulo = models.CharField(max_length=255)
    num_paginas = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.titulo} - {self.num_paginas}"