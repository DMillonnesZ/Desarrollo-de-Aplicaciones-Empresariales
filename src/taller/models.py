from django.db import models

# Datos estáticos en memoria (sin base de datos, según alcance del laboratorio)

citas = [
    {
        "id": 1,
        "cliente": {
            "nombre": "Juan Pérez",
            "telefono": "987654321",
            "vehiculo": {
                "descripcion": "Toyota Yaris 2020",
                "placa": "ABC-123",
                "servicios": [
                    {"tipo": "Cambio de aceite", "precio": 80.00},
                    {"tipo": "Cambio de filtro", "precio": 40.00},
                ],
                "mecanico": "Carlos Ramírez",
                "estado": "En espera",
                "programacion_atencion": "2026-09-02 09:00",
                "fecha_entrega": "2026-09-02",
            }
        }
    },
    {
        "id": 2,
        "cliente": {
            "nombre": "María Gómez",
            "telefono": "912345678",
            "vehiculo": {
                "descripcion": "Hyundai Accent 2019",
                "placa": "XYZ-456",
                "servicios": [
                    {"tipo": "Revisión de frenos", "precio": 60.00},
                ],
                "mecanico": "Luis Fernández",
                "estado": "En proceso",
                "programacion_atencion": "2026-09-02 11:00",
                "fecha_entrega": "2026-09-03",
            }
        }
    },
    {
        "id": 3,
        "cliente": {
            "nombre": "Pedro Ramírez",
            "telefono": "998877665",
            "vehiculo": {
                "descripcion": "Kia Rio 2021",
                "placa": "LMN-789",
                "servicios": [
                    {"tipo": "Alineamiento y balanceo", "precio": 50.00},
                    {"tipo": "Cambio de llantas", "precio": 320.00},
                ],
                "mecanico": "Carlos Ramírez",
                "estado": "Terminado",
                "programacion_atencion": "2026-08-30 14:00",
                "fecha_entrega": "2026-08-31",
            }
        }
    },
    {
        "id": 4,
        "cliente": {
            "nombre": "Ana Torres",
            "telefono": "955443322",
            "vehiculo": {
                "descripcion": "Nissan Sentra 2018",
                "placa": "DEF-321",
                "servicios": [
                    {"tipo": "Diagnóstico de motor", "precio": 45.00},
                ],
                "mecanico": "Luis Fernández",
                "estado": "En espera",
                "programacion_atencion": "2026-09-03 08:30",
                "fecha_entrega": "2026-09-04",
            }
        }
    },
    {
        "id": 5,
        "cliente": {
            "nombre": "Roberto Díaz",
            "telefono": "977665544",
            "vehiculo": {
                "descripcion": "Chevrolet Sail 2020",
                "placa": "GHI-654",
                "servicios": [
                    {"tipo": "Cambio de batería", "precio": 180.00},
                    {"tipo": "Revisión eléctrica", "precio": 70.00},
                ],
                "mecanico": "Carlos Ramírez",
                "estado": "Entregado",
                "programacion_atencion": "2026-08-28 10:00",
                "fecha_entrega": "2026-08-29",
            }
        }
    },
]


def calcular_presupuesto(servicios):
    """Suma el precio de todos los servicios de una cita."""
    return sum(servicio["precio"] for servicio in servicios)


def obtener_siguiente_id():
    """Genera el siguiente ID disponible para una nueva cita."""
    if not citas:
        return 1
    return max(cita["id"] for cita in citas) + 1


def existe_cruce_horario(programacion_atencion, mecanico):
    """
    Verifica si ya existe una cita registrada con el mismo mecánico
    en la misma fecha y hora (evita cruces de citas - Requisito 3/4).
    Retorna True si hay cruce, False si el horario está libre.
    """
    for cita in citas:
        vehiculo = cita["cliente"]["vehiculo"]
        if (
            vehiculo["programacion_atencion"] == programacion_atencion
            and vehiculo["mecanico"] == mecanico
        ):
            return True
    return False

def agregar_cita(datos):
    """
    Agrega una nueva cita a la lista en memoria, a partir de los
    datos limpios (cleaned_data) del formulario.
    """
    nueva_cita = {
        "id": obtener_siguiente_id(),
        "cliente": {
            "nombre": datos["nombre_cliente"],
            "telefono": datos["telefono"],
            "vehiculo": {
                "descripcion": datos["descripcion_vehiculo"],
                "placa": datos["placa"],
                "servicios": [
                    {"tipo": datos["tipo_servicio"], "precio": float(datos["precio_servicio"])},
                ],
                "mecanico": datos["mecanico"],
                "estado": datos["estado"],
                "programacion_atencion": f'{datos["fecha_atencion"]} {datos["hora_atencion"]}',
                "fecha_entrega": str(datos["fecha_entrega"]),
            }
        }
    }
    citas.append(nueva_cita)
    return nueva_cita