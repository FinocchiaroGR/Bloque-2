from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

FILETYPES = [
    ('PDF', 'Archivo PDF'),
    ('IMG', 'Imagen'),
]


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripción = models.CharField(max_length=100)
    fechaCreada = models.DateTimeField(auto_now_add=True)
    subCategoria = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} {self.nombre}"


class Leccion(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    imagen = models.ImageField(upload_to='uploads/lessons/img')
    fecha = models.DateField(
        "Fecha de creación", auto_now=False, auto_now_add=True)
    aprobacion = models.BooleanField("Aprobación")
    category = models.ForeignKey(Categoria, on_delete=CASCADE)


class Archivo(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    path = models.FileField("Archivo", upload_to='uploads/files')
    lipo = models.CharField("Tipo de archivo", choices=FILETYPES, max_length=3)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)


class Video(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=500)
    link = models.CharField(max_length=500)
    leccion = models.ForeignKey(Leccion, on_delete=CASCADE)
