from django.db import models

# Create your models here.

class Promocion(models.Model):
    PROMOCION_CHOICES =[
        (1,"promocion 1"),
        (2,"Promocion 2"),
        (3,"Promocion 3"),
        (4,"Promocion 4"),
        (5,"Promocion 5")
    ]

    NAME_CHOICES = [
        ('promocion1', 'Promocion 1'),
        ('promocion2', 'Promocion 2'),
        ('promocion3', 'Promocion 3'),
        ('promocion4', 'Promocion 4'),
        ('promocion5', 'Promocion 5'),
    ]


    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='promociones')
    promocion = models.IntegerField(choices=PROMOCION_CHOICES)
    name = models.CharField(choices=NAME_CHOICES, max_length=20)

    def save(self, *args, **kwargs):
        promocion_actual = Promocion.objects.filter(promocion=self.promocion).first()
        if promocion_actual:
            # Eliminar la imagen anterior si existe
            promocion_actual.imagen.delete(save=False)
            promocion_actual.delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre