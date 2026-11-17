from datetime import date, timedelta
from decimal import Decimal

from django.utils import timezone

from vetcar.models import (
    Especie, Raza, Dueno, Mascota, Veterinario,
    Medicamento, Consulta, DetalleReceta,
)

especie, _ = Especie.objects.get_or_create(nombre='Perro')
raza, _ = Raza.objects.get_or_create(nombre='Labrador', especie=especie)

dueno, _ = Dueno.objects.get_or_create(
    dni='12345678',
    defaults=dict(nombre='Carlos Ramirez', telefono='987654321', activo=True),
)
mascota, _ = Mascota.objects.get_or_create(
    nombre='Firulais',
    dueno=dueno,
    defaults=dict(raza=raza, sexo='M', activo=True),
)
vet, _ = Veterinario.objects.get_or_create(
    colegiatura='CMVP-12345',
    defaults=dict(
        nombre='Ana Torres', activo=True,
        fecha_ingreso=date(2020, 1, 15),
    ),
)

for nombre, stock, precio in [
    ('Amoxicilina 500mg', 50, '12.50'),
    ('Ivermectina', 30, '8.90'),
    ('Meloxicam', 40, '15.00'),
]:
    Medicamento.objects.get_or_create(
        nombre=nombre,
        defaults=dict(stock=stock, precio_unitario=Decimal(precio)),
    )

if not Consulta.objects.exists():
    ahora = timezone.now()
    meds = list(Medicamento.objects.all()[:2])
    datos = [
        ('Control general', 'PENDIENTE', '', '40', 1),
        ('Vomitos', 'ATENDIDA', 'Gastritis leve', '60', -2),
        ('Cojera', 'ATENDIDA', 'Esguince leve', '80', -5),
        ('Vacuna de refuerzo', 'PENDIENTE', '', '50', 3),
        ('Alergia en piel', 'CANCELADA', '', '0', -1),
    ]
    for motivo, estado, diag, costo, dias in datos:
        c = Consulta.objects.create(
            mascota=mascota, veterinario=vet,
            fecha=ahora + timedelta(days=dias),
            motivo=motivo, estado=estado,
            diagnostico=diag, costo=Decimal(costo),
        )
        if estado == 'ATENDIDA':
            for m in meds:
                DetalleReceta.objects.create(
                    consulta=c, medicamento=m, cantidad=2,
                    precio_unitario=m.precio_unitario,
                    dosis='1 cada 12 horas',
                )

print('Medicamentos:', Medicamento.objects.count())
print('Consultas:', Consulta.objects.count())
print('Recetas:', DetalleReceta.objects.count())