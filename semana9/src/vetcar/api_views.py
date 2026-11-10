from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Medicamento, Consulta, Raza, Veterinario, Mascota
from .serializers import (
    MedicamentoSerializer, ConsultaSerializer,
    RazaSerializer, VeterinarioSerializer, MascotaSerializer,
)


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['nombre', 'stock', 'precio_unitario']


class ConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        qs = (
            Consulta.objects
            .select_related('mascota', 'veterinario')
            .prefetch_related('detalles_receta__medicamento')
        )
        estado = self.request.query_params.get('estado')
        if estado:
            qs = qs.filter(estado=estado.upper())
        return qs

    @action(detail=False, methods=['get'])
    def pendientes(self, request):
        qs = self.get_queryset().pendientes()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.select_related('especie')
    serializer_class = RazaSerializer


class VeterinarioViewSet(viewsets.ModelViewSet):
    serializer_class = VeterinarioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'colegiatura']
    ordering_fields = ['nombre', 'fecha_ingreso', 'cupos_disponibles']

    def get_queryset(self):
        qs = Veterinario.objects.prefetch_related('especialidades')
        activo = self.request.query_params.get('activo')
        if activo is not None:
            qs = qs.filter(activo=activo.lower() in ('true', '1', 'si'))
        return qs

    @action(detail=False, methods=['get'], url_path='con-cupos')
    def con_cupos(self, request):
        qs = self.get_queryset().activos().con_cupos()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class MascotaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MascotaSerializer

    def get_queryset(self):
        return (
            Mascota.objects
            .select_related('dueno', 'raza__especie', 'ficha_clinica')
            .prefetch_related('seguimientos__veterinario')
        )