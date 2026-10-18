from rest_framework import serializers
from .models import (
    Medicamento, Consulta, DetalleReceta,
    Especialidad, Raza, Veterinario,
    Mascota, FichaClinica, SeguimientoClinico,
)


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


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['id', 'nombre', 'descripcion']


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ['id', 'uuid', 'nombre', 'especie', 'descripcion']
        read_only_fields = ['uuid']


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = [
            'id', 'uuid', 'nombre', 'telefono', 'correo', 'activo',
            'colegiatura', 'especialidades', 'fecha_ingreso',
            'cupos_disponibles',
        ]
        read_only_fields = ['uuid']

    def validate_cupos_disponibles(self, value):
        if value > 20:
            raise serializers.ValidationError(
                'Los cupos disponibles no pueden superar 20.'
            )
        return value


class FichaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaClinica
        fields = ['alergias', 'condiciones_cronicas', 'seguro_veterinario',
                  'contacto_emergencia', 'observaciones']


class SeguimientoSerializer(serializers.ModelSerializer):
    veterinario = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = SeguimientoClinico
        fields = ['uuid', 'veterinario', 'rol', 'fecha_asignacion', 'activo']


class MascotaSerializer(serializers.ModelSerializer):
    dueno = serializers.CharField(source='dueno.nombre', read_only=True)
    raza = serializers.CharField(source='raza.nombre', read_only=True)
    especie = serializers.CharField(source='raza.especie.nombre', read_only=True)
    ficha_clinica = FichaClinicaSerializer(read_only=True)
    seguimientos = SeguimientoSerializer(many=True, read_only=True)

    class Meta:
        model = Mascota
        fields = ['uuid', 'nombre', 'sexo', 'peso_kg', 'activo', 'dueno',
                  'raza', 'especie', 'ficha_clinica', 'seguimientos']