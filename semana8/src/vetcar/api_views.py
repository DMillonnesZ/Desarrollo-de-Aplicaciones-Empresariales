from rest_framework import viewsets

from .models import Medicamento, Consulta
from .serializers import MedicamentoSerializer, ConsultaSerializer


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class ConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        return (
            Consulta.objects
            .select_related('mascota', 'veterinario')
            .prefetch_related('detalles_receta__medicamento')
        )