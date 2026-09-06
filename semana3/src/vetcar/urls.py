from django.urls import path
from . import views

app_name = 'vetcar'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mascotas/<int:pk>/historial/', views.historial, name='historial'),
    path('<str:entidad>/', views.listar, name='listar'),
    path('<str:entidad>/nuevo/', views.crear, name='crear'),
    path('<str:entidad>/<int:pk>/editar/', views.editar, name='editar'),
    path('<str:entidad>/<int:pk>/eliminar/', views.eliminar, name='eliminar'),
]