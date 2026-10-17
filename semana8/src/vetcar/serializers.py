from rest_framework import serializers
from .models import Medicamento, Consulta, DetalleReceta


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


class DetalleRecetaSerializer(serializers.ModelSerializer):
    medicamento = serializers.CharField(source='medicamento.nombre', read_only=True)

    class Meta:
        model = DetalleReceta
        fields = ['uuid', 'medicamento', 'cantidad', 'precio_unitario', 'dosis', 'indicaciones']


class ConsultaSerializer(serializers.ModelSerializer):
    mascota = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario = serializers.CharField(source='veterinario.nombre', read_only=True)
    detalles_receta = DetalleRecetaSerializer(many=True, read_only=True)

    class Meta:
        model = Consulta
        fields = ['uuid', 'fecha', 'mascota', 'veterinario', 'motivo',
                  'estado', 'costo', 'detalles_receta']