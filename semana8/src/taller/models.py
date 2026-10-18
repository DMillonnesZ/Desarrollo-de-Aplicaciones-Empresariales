from django.db import models


class Cita(models.Model):
    ESTADO_CHOICES = [
        ("En espera", "En espera"),
        ("En proceso", "En proceso"),
        ("Terminado", "Terminado"),
        ("Entregado", "Entregado"),
    ]

    MECANICO_CHOICES = [
        ("Carlos Ramírez", "Carlos Ramírez"),
        ("Luis Fernández", "Luis Fernández"),
    ]

    # Datos del cliente
    cliente_nombre = models.CharField(max_length=100)
    cliente_telefono = models.CharField(max_length=15)

    # Datos del vehículo
    vehiculo_descripcion = models.CharField(max_length=100)
    vehiculo_placa = models.CharField(max_length=10)

    # Datos de la reparación
    mecanico = models.CharField(max_length=100, choices=MECANICO_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="En espera")

    # Programación
    fecha_atencion = models.DateField()
    hora_atencion = models.TimeField()
    fecha_entrega = models.DateField()

    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_atencion", "-hora_atencion"]

    def __str__(self):
        return f"Cita #{self.id} - {self.cliente_nombre} ({self.vehiculo_placa})"

    def presupuesto(self):
        """Suma el precio de todos los servicios asociados a esta cita."""
        return sum(servicio.precio for servicio in self.servicios.all())


class Servicio(models.Model):
    cita = models.ForeignKey(Cita, related_name="servicios", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - S/ {self.precio}"