from rest_framework import serializers
from .models import Medicamento


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['id', 'uuid', 'nombre', 'descripcion', 'stock', 'precio_unitario']
        read_only_fields = ['uuid']
        
        def validate_precio_unitario(self, value):
         if value <= 0:
            raise serializers.ValidationError(
                'El precio unitario debe ser mayor que cero.'
            )
         return value