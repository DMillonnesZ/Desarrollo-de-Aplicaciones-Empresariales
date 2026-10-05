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

            if isinstance(
                widget,
                (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect),
            ):
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
        fields = [
            'nombre', 'telefono', 'correo', 'colegiatura',
            'especialidades', 'fecha_ingreso', 'activo',
        ]
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
        fields = [
            'nombre', 'fecha_nacimiento', 'sexo',
            'peso_kg', 'dueno', 'raza', 'activo',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['raza'].queryset = (
            Raza.objects.order_by('especie__nombre', 'nombre')
        )
        self.fields['dueno'].queryset = Dueno.objects.order_by('nombre')


class ConsultaForm(ClinicaModelForm):
    class Meta:
        model = Consulta
        fields = [
            'mascota', 'veterinario', 'fecha', 'motivo',
            'diagnostico', 'tratamiento', 'estado', 'costo',
        ]
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class VacunacionForm(ClinicaModelForm):
    class Meta:
        model = Vacunacion
        fields = [
            'mascota', 'veterinario', 'fecha',
            'nombre_vacuna', 'proxima_dosis', 'lote',
        ]
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
        fields = [
            'alergias', 'condiciones_cronicas', 'seguro_veterinario',
            'contacto_emergencia', 'observaciones',
        ]


class SeguimientoClinicoForm(ClinicaModelForm):
    class Meta:
        model = SeguimientoClinico
        fields = ['veterinario', 'fecha_asignacion', 'rol', 'activo']
        widgets = {
            'fecha_asignacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['veterinario'].queryset = (
            Veterinario.objects.order_by('nombre')
        )


class DetalleRecetaForm(ClinicaModelForm):
    class Meta:
        model = DetalleReceta
        fields = ['medicamento', 'cantidad', 'dosis', 'indicaciones']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['medicamento'].queryset = (
            Medicamento.objects.order_by('nombre')
        )


# ============================================================
# EJERCICIO 3: FORMULARIO PARA LA OPERACIÓN TRANSACCIONAL
# ============================================================

class RegistrarRecetaForm(forms.Form):
    medicamento = forms.ModelChoiceField(
        queryset=Medicamento.objects.order_by('nombre'),
        label='Medicamento',
        empty_label='Selecciona un medicamento',
    )

    cantidad = forms.IntegerField(
        min_value=1,
        label='Cantidad',
    )

    dosis = forms.CharField(
        max_length=100,
        label='Dosis',
    )

    indicaciones = forms.CharField(
        required=False,
        label='Indicaciones',
        widget=forms.Textarea(attrs={'rows': 2}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs['class'] = (
                'form-select'
                if isinstance(campo.widget, forms.Select)
                else 'form-control'
            )