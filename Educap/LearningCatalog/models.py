from django.db import models

# Create your models here.


class Categoria(models.Model):
    Nombre = models.CharField(max_length=30)
    Descripción = models.CharField(max_length=100)
    FechaCreada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Nombre}"
