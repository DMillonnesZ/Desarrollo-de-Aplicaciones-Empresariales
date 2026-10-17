from rest_framework.routers import DefaultRouter

from .api_views import MedicamentoViewSet

router = DefaultRouter()
router.register('medicamentos', MedicamentoViewSet, basename='medicamento')

urlpatterns = router.urls