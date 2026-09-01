from django import forms


ESTADOS = [
    ("En espera", "En espera"),
    ("En proceso", "En proceso"),
    ("Terminado", "Terminado"),
    ("Entregado", "Entregado"),
]

MECANICOS = [
    ("Carlos Ramírez", "Carlos Ramírez"),
    ("Luis Fernández", "Luis Fernández"),
]


class CitaForm(forms.Form):
    # Datos del cliente
    nombre_cliente = forms.CharField(
        label="Nombre del cliente",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    telefono = forms.CharField(
        label="Teléfono",
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # Datos del vehículo
    descripcion_vehiculo = forms.CharField(
        label="Vehículo (marca, modelo, año)",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    placa = forms.CharField(
        label="Placa",
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # Servicio (uno por formulario, según alcance definido)
    tipo_servicio = forms.CharField(
        label="Tipo de servicio",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    precio_servicio = forms.DecimalField(
        label="Precio del servicio (S/)",
        min_value=0,
        decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
    )

    mecanico = forms.ChoiceField(
        label="Mecánico asignado",
        choices=MECANICOS,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    estado = forms.ChoiceField(
        label="Estado",
        choices=ESTADOS,
        initial="En espera",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    # Fecha y hora con selector tipo calendario/reloj (widgets nativos HTML5)
    fecha_atencion = forms.DateField(
        label="Fecha de atención",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    hora_atencion = forms.TimeField(
        label="Hora de atención",
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time"})
    )
    fecha_entrega = forms.DateField(
        label="Fecha estimada de entrega",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )