from django.urls import path
from . import views

urlpatterns = [
    # Dueño
    path('duenos/', views.listar_duenos, name='listar_duenos'),
    path('duenos/nuevo/', views.crear_dueno, name='crear_dueno'),
    path('duenos/<uuid:uuid>/editar/', views.editar_dueno, name='editar_dueno'),
    path('duenos/<uuid:uuid>/eliminar/', views.eliminar_dueno, name='eliminar_dueno'),

    # Veterinario
    path('veterinarios/', views.listar_veterinarios, name='listar_veterinarios'),
    path('veterinarios/nuevo/', views.crear_veterinario, name='crear_veterinario'),
    path('veterinarios/<uuid:uuid>/', views.veterinario_detalle, name='veterinario_detalle'),
    path('veterinarios/<uuid:uuid>/editar/', views.editar_veterinario, name='editar_veterinario'),
    path('veterinarios/<uuid:uuid>/eliminar/', views.eliminar_veterinario, name='eliminar_veterinario'),

    # Raza
    path('razas/', views.listar_razas, name='listar_razas'),
    path('razas/nueva/', views.crear_raza, name='crear_raza'),
    path('razas/<uuid:uuid>/editar/', views.editar_raza, name='editar_raza'),
    path('razas/<uuid:uuid>/eliminar/', views.eliminar_raza, name='eliminar_raza'),

    # Mascota
    path('mascotas/', views.listar_mascotas, name='listar_mascotas'),
    path('mascotas/nueva/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/<uuid:uuid>/', views.mascota_detalle, name='mascota_detalle'),
    path('mascotas/<uuid:uuid>/editar/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/<uuid:uuid>/eliminar/', views.eliminar_mascota, name='eliminar_mascota'),

    # Consulta
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/nueva/', views.crear_consulta, name='crear_consulta'),
    path('consultas/<uuid:uuid>/editar/', views.editar_consulta, name='editar_consulta'),
    path('consultas/<uuid:uuid>/anular/', views.anular_consulta, name='anular_consulta'),

    # Vacunacion
    path('vacunaciones/', views.listar_vacunaciones, name='listar_vacunaciones'),
    path('vacunaciones/nueva/', views.crear_vacunacion, name='crear_vacunacion'),
    path('vacunaciones/<uuid:uuid>/editar/', views.editar_vacunacion, name='editar_vacunacion'),
    path('vacunaciones/<uuid:uuid>/eliminar/', views.eliminar_vacunacion, name='eliminar_vacunacion'),

    # Ficha clínica (1:1, anidada bajo mascota)
    path('mascotas/<uuid:mascota_uuid>/ficha-clinica/', views.gestionar_ficha_clinica, name='gestionar_ficha_clinica'),

    # Seguimiento clínico (N:M, anidado bajo mascota para crear; propio uuid para editar/eliminar)
    path('mascotas/<uuid:mascota_uuid>/seguimiento/nuevo/', views.crear_seguimiento, name='crear_seguimiento'),
    path('seguimientos/<uuid:uuid>/editar/', views.editar_seguimiento, name='editar_seguimiento'),
    path('seguimientos/<uuid:uuid>/eliminar/', views.eliminar_seguimiento, name='eliminar_seguimiento'),

    # Detalle de receta (N:M, anidado bajo consulta para crear; propio uuid para eliminar)
    path('consultas/<uuid:consulta_uuid>/receta/nueva/', views.crear_detalle_receta, name='crear_detalle_receta'),
    path('recetas/<uuid:uuid>/eliminar/', views.eliminar_detalle_receta, name='eliminar_detalle_receta'),
]