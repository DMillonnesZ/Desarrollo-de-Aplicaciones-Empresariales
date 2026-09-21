from django.contrib import admin
from .models import (
    Especie, Especialidad, Persona, Dueno, Veterinario, Raza, Mascota,
    FichaClinica, Medicamento, Atencion, Consulta, Vacunacion, DetalleReceta,
    SeguimientoClinico, AuditoriaAtencion, AuditoriaMascota,
)

admin.site.register(Especie)
admin.site.register(Especialidad)
admin.site.register(Persona)
admin.site.register(Dueno)
admin.site.register(Veterinario)
admin.site.register(Raza)
admin.site.register(Mascota)
admin.site.register(FichaClinica)
admin.site.register(Medicamento)
admin.site.register(Atencion)
admin.site.register(Consulta)
admin.site.register(Vacunacion)
admin.site.register(DetalleReceta)
admin.site.register(SeguimientoClinico)
admin.site.register(AuditoriaAtencion)
admin.site.register(AuditoriaMascota)