from django import forms
from .models import (
    Dueno, Veterinario, Raza, Mascota, Consulta, Vacunacion,
    FichaClinica, SeguimientoClinico, DetalleReceta, Medicamento,
)


class ClinicaModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            widget = campo.widget
            clases_previas = widget.attrs.get('class', '')
            if isinstance(widget, (forms.CheckboxInput,)):
                nueva_clase = 'form-check-input'
            elif isinstance(widget, (forms.CheckboxSelectMultiple, forms.RadioSelect)):
                nueva_clase = 'form-check-input'
            elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
                nueva_clase = 'form-select'
            else:
                nueva_clase = 'form-control'
            widget.attrs['class'] = f'{clases_previas} {nueva_clase}'.strip()


class DuenoForm(ClinicaModelForm):
    class Meta:
        model = Dueno
        fields = ['nombre', 'telefono', 'correo', 'dni', 'direccion', 'activo']


class VeterinarioForm(ClinicaModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'telefono', 'correo', 'colegiatura', 'especialidades', 'fecha_ingreso', 'activo']
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'especialidades': forms.CheckboxSelectMultiple(),
        }


class RazaForm(ClinicaModelForm):
    class Meta:
        model = Raza
        fields = ['nombre', 'especie', 'descripcion']


class MascotaForm(ClinicaModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'fecha_nacimiento', 'sexo', 'peso_kg', 'dueno', 'raza', 'activo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['raza'].queryset = self.fields['raza'].queryset.order_by('especie__nombre', 'nombre') # type: ignore[attr-defined]
        self.fields['dueno'].queryset = self.fields['dueno'].queryset.order_by('nombre') # type: ignore[attr-defined]


class ConsultaForm(ClinicaModelForm):
    class Meta:
        model = Consulta
        fields = ['mascota', 'veterinario', 'fecha', 'motivo', 'diagnostico', 'tratamiento', 'estado', 'costo']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class VacunacionForm(ClinicaModelForm):
    class Meta:
        model = Vacunacion
        fields = ['mascota', 'veterinario', 'fecha', 'nombre_vacuna', 'proxima_dosis', 'lote']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'proxima_dosis': forms.DateInput(attrs={'type': 'date'}),
        }


class MedicamentoForm(ClinicaModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'stock', 'precio_unitario']


class FichaClinicaForm(ClinicaModelForm):
    class Meta:
        model = FichaClinica
        fields = ['alergias', 'condiciones_cronicas', 'seguro_veterinario', 'contacto_emergencia', 'observaciones']

class SeguimientoClinicoForm(ClinicaModelForm):
    class Meta:
        model = SeguimientoClinico
        fields = ['veterinario', 'fecha_asignacion', 'rol', 'activo']
        widgets = {
            'fecha_asignacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['veterinario'].queryset = self.fields['veterinario'].queryset.order_by('nombre') # type: ignore[attr-defined]


class DetalleRecetaForm(ClinicaModelForm):
    class Meta:
        model = DetalleReceta
        fields = ['medicamento', 'cantidad', 'dosis', 'indicaciones']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicamento'].queryset = self.fields['medicamento'].queryset.order_by('nombre') # type: ignore[attr-defined]