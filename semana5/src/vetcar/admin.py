from django.contrib import admin
from .models import (
    Especie, Especialidad, Persona, Dueno, Veterinario, Raza, Mascota,
    FichaClinica, Medicamento, Atencion, Consulta, Vacunacion, DetalleReceta,
    SeguimientoClinico, AuditoriaAtencion, AuditoriaMascota,
)


class DetalleRecetaInline(admin.TabularInline):
    model = DetalleReceta
    extra = 1


class FichaClinicaInline(admin.StackedInline):
    model = FichaClinica
    can_delete = False
    extra = 1
    max_num = 1


class SeguimientoClinicoInline(admin.TabularInline):
    model = SeguimientoClinico
    extra = 1


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'dueno', 'sexo', 'activo')
    search_fields = ('nombre', 'dueno__nombre', 'dueno__dni')
    list_filter = ('activo', 'sexo', 'raza__especie')
    inlines = [FichaClinicaInline, SeguimientoClinicoInline]


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'colegiatura', 'fecha_ingreso', 'activo')
    list_filter = ('activo',)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'veterinario', 'fecha', 'estado', 'costo')
    list_filter = ('estado',)
    search_fields = ('mascota__nombre', 'motivo')
    inlines = [DetalleRecetaInline]


@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'telefono', 'activo')
    search_fields = ('nombre', 'dni')
    list_filter = ('activo',)


@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie')
    list_filter = ('especie',)
    search_fields = ('nombre',)


@admin.register(Vacunacion)
class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'veterinario', 'nombre_vacuna', 'fecha', 'proxima_dosis')
    list_filter = ('nombre_vacuna',)
    search_fields = ('mascota__nombre', 'nombre_vacuna')


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'stock', 'precio_unitario')
    search_fields = ('nombre',)


@admin.register(AuditoriaAtencion)
class AuditoriaAtencionAdmin(admin.ModelAdmin):
    list_display = ('atencion_id', 'tipo', 'mascota_nombre', 'accion', 'fecha_accion')
    list_filter = ('accion', 'tipo')
    search_fields = ('mascota_nombre', 'dueno_nombre', 'dueno_dni')


admin.site.register(Especie)
admin.site.register(Especialidad)
admin.site.register(Persona)
admin.site.register(FichaClinica)
admin.site.register(Atencion)
admin.site.register(DetalleReceta)
admin.site.register(SeguimientoClinico)
admin.site.register(AuditoriaMascota)