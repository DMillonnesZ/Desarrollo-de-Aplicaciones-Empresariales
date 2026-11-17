from datetime import date

from vetcar.models import (
    Especie, Raza, Dueno, Mascota, Veterinario,
    Especialidad, FichaClinica, SeguimientoClinico,
)

perro = Especie.objects.get(nombre='Perro')
gato, _ = Especie.objects.get_or_create(nombre='Gato')
raza_lab = Raza.objects.get(nombre='Labrador', especie=perro)
raza_siames, _ = Raza.objects.get_or_create(nombre='Siames', especie=gato)
raza_poodle, _ = Raza.objects.get_or_create(nombre='Poodle', especie=perro)

cirugia, _ = Especialidad.objects.get_or_create(nombre='Cirugia')
dermato, _ = Especialidad.objects.get_or_create(nombre='Dermatologia')

vet1 = Veterinario.objects.get(colegiatura='CMVP-12345')
vet2, _ = Veterinario.objects.get_or_create(
    colegiatura='CMVP-23456',
    defaults=dict(nombre='Luis Mendoza', activo=True,
                  fecha_ingreso=date(2021, 3, 10), cupos_disponibles=0),
)
vet3, _ = Veterinario.objects.get_or_create(
    colegiatura='CMVP-34567',
    defaults=dict(nombre='Rosa Quispe', activo=False,
                  fecha_ingreso=date(2019, 6, 1), cupos_disponibles=5),
)
vet1.especialidades.add(cirugia)
vet2.especialidades.add(dermato)
vet3.especialidades.add(cirugia)

dueno2, _ = Dueno.objects.get_or_create(
    dni='87654321',
    defaults=dict(nombre='Maria Lopez', telefono='912345678', activo=True),
)
dueno3, _ = Dueno.objects.get_or_create(
    dni='11223344',
    defaults=dict(nombre='Jorge Salas', activo=True),
)

for nombre, sexo, d, r in [
    ('Michi', 'H', dueno2, raza_siames),
    ('Rex', 'M', dueno3, raza_lab),
    ('Luna', 'H', dueno2, raza_poodle),
    ('Toby', 'M', dueno3, raza_poodle),
]:
    Mascota.objects.get_or_create(
        nombre=nombre, dueno=d,
        defaults=dict(sexo=sexo, raza=r, activo=True),
    )

for m in Mascota.objects.all():
    FichaClinica.objects.get_or_create(
        mascota=m,
        defaults=dict(alergias='Ninguna', observaciones='Control anual'),
    )
    SeguimientoClinico.objects.get_or_create(
        mascota=m, veterinario=vet1, rol='TITULAR',
        defaults=dict(fecha_asignacion=date(2026, 1, 10), activo=True),
    )
    SeguimientoClinico.objects.get_or_create(
        mascota=m, veterinario=vet2, rol='INTERCONSULTA',
        defaults=dict(fecha_asignacion=date(2026, 2, 5), activo=True),
    )

print('Veterinarios:', Veterinario.objects.count())
print('Razas:', Raza.objects.count())
print('Mascotas:', Mascota.objects.count())
print('Fichas:', FichaClinica.objects.count())
print('Seguimientos:', SeguimientoClinico.objects.count())