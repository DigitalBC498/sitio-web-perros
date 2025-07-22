from django.db import models

# Create your models here.


ESTADO_CHOICES = [
    ('perdido', 'Perdido'),
    ('encontrado', 'Encontrado'),
]

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    foto = models.ImageField(upload_to='fotos_perros/', blank=True, null=True)  # <- CAMPO OPCIONAL
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

