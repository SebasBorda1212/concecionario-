from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'marca_modelo', 'vin', 'precio_base', 'anio', 'precio_matriculado']
        read_only_fields = ['precio_matriculado']

    def validate_anio(self, value):
        if value < 1990:
            raise serializers.ValidationError("El año del modelo no puede ser anterior a 1990.")
        return value