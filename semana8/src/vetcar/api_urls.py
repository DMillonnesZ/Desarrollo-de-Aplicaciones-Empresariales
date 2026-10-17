from django.urls import path
from . import api_views

urlpatterns = [
    path('medicamentos/', api_views.MedicamentoListCreate.as_view()),
    path('medicamentos/<int:pk>/', api_views.MedicamentoDetail.as_view()),
]