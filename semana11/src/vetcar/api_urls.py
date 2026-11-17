from rest_framework.routers import DefaultRouter

from .api_views import (
    MedicamentoViewSet, ConsultaViewSet, RazaViewSet,
    VeterinarioViewSet, MascotaViewSet,
)

router = DefaultRouter()
router.register('medicamentos', MedicamentoViewSet, basename='medicamento')
router.register('consultas', ConsultaViewSet, basename='consulta')
router.register('razas', RazaViewSet, basename='raza')
router.register('veterinarios', VeterinarioViewSet, basename='veterinario')
router.register('mascotas', MascotaViewSet, basename='mascota')

urlpatterns = router.urls