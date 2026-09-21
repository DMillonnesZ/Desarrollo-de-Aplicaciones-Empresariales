from django.contrib import admin
from .models import (
    Especie, Especialidad, Persona, Dueno, Veterinario, Raza, Mascota,
    FichaClinica, Medicamento, Atencion, Consulta, Vacunacion, DetalleReceta,
    SeguimientoClinico, AuditoriaAtencion, AuditoriaMascota,
)


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'dueno', 'sexo', 'activo')
    search_fields = ('nombre', 'dueno__nombre', 'dueno__dni')


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'colegiatura', 'fecha_ingreso', 'activo')


admin.site.register(Especie)
admin.site.register(Especialidad)
admin.site.register(Persona)
admin.site.register(Dueno)
admin.site.register(Raza)
admin.site.register(FichaClinica)
admin.site.register(Medicamento)
admin.site.register(Atencion)
admin.site.register(Consulta)
admin.site.register(Vacunacion)
admin.site.register(DetalleReceta)
admin.site.register(SeguimientoClinico)
admin.site.register(AuditoriaAtencion)
admin.site.register(AuditoriaMascota)