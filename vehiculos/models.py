from django.db import models
from django.core.exceptions import ValidationError

class Vehiculo(models.Model):
    marca_modelo = models.CharField(max_length=150)
    vin = models.CharField(max_length=17, unique=True)
    precio_base = models.DecimalField(max_digits=12, decimal_places=2)
    anio = models.IntegerField()
    precio_matriculado = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def clean(self):
        if self.anio < 1990:
            raise ValidationError("El año del modelo no puede ser anterior a 1990.")

    def calcular_precio_matriculado(self):
        """Calcula el precio de matriculación sumando el 8% sobre el valor base."""
        return round(float(self.precio_base) * 1.08, 2)

    def save(self, *args, **kwargs):
        self.full_clean()
        self.precio_matriculado = self.calcular_precio_matriculado()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.marca_modelo} ({self.anio}) - VIN: {self.vin}"