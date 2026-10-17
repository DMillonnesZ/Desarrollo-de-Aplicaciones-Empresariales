from rest_framework.routers import DefaultRouter

from .api_views import MedicamentoViewSet, ConsultaViewSet

router = DefaultRouter()
router.register('medicamentos', MedicamentoViewSet, basename='medicamento')
router.register('consultas', ConsultaViewSet, basename='consulta')

urlpatterns = router.urls