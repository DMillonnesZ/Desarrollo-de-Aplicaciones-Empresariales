from django import forms
from .models import Cita, Servicio


class CitaForm(forms.ModelForm):

    tipo_servicio = forms.CharField(
        label="Tipo de servicio",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        )
    )

    precio_servicio = forms.DecimalField(
        label="Precio del servicio (S/)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01"
            }
        )
    )

    class Meta:
        model = Cita
        fields = [
            "cliente_nombre",
            "cliente_telefono",
            "vehiculo_descripcion",
            "vehiculo_placa",
            "mecanico",
            "estado",
            "fecha_atencion",
            "hora_atencion",
            "fecha_entrega",
        ]

        widgets = {
            "cliente_nombre": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "cliente_telefono": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "vehiculo_descripcion": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "vehiculo_placa": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "mecanico": forms.Select(
                attrs={"class": "form-select"}
            ),
            "estado": forms.Select(
                attrs={"class": "form-select"}
            ),
            "fecha_atencion": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "hora_atencion": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),
            "fecha_entrega": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
        }
