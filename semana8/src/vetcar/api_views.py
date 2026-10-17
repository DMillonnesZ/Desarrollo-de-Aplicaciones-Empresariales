from rest_framework import generics

from .models import Medicamento
from .serializers import MedicamentoSerializer


class MedicamentoListCreate(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class MedicamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer