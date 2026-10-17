from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Medicamento, Consulta
from .serializers import MedicamentoSerializer, ConsultaSerializer


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