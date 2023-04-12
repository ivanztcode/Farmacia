from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    correo_electronico = models.EmailField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class Medicamento(models.Model):
    codigo_barras = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='medicamentos', null=True, blank=True)
    fecha_caducidad = models.DateField(default=timezone.now)


    def __str__(self):
        return f'{self.nombre} - Precio: {self.precio} - Stock: {self.stock}'