from django.test import TestCase
from django.core.exceptions import ValidationError
from vehiculos.models import Vehiculo

class VehiculoModelTest(TestCase):

    def test_calculo_impuesto_matriculacion(self):
        """Verifica que el impuesto de matriculación del 8% se calcule correctamente."""
        vehiculo = Vehiculo(
            marca_modelo="Mazda CX-5",
            vin="3MZKF123456789012",
            precio_base=90000000.00,
            anio=2023
        )
        vehiculo.full_clean()
        vehiculo.save()
        
        # 90,000,000 * 1.08 = 97,200,000.00
        self.assertEqual(float(vehiculo.precio_matriculado), 97200000.00)

    def test_validacion_anio_invalido(self):
        """Verifica que se lance un error si el año es menor a 1990."""
        vehiculo = Vehiculo(
            marca_modelo="Renault 4 Clásico",
            vin="1234567890ABCDEFG",
            precio_base=10000000.00,
            anio=1982
        )
        with self.assertRaises(ValidationError):
            vehiculo.full_clean()