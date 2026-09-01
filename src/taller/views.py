from django.shortcuts import render
from .models import citas, calcular_presupuesto


def lista_citas(request):
    """
    Recorre la lista de citas (en memoria) y calcula el presupuesto
    de cada una antes de enviarlas al template.
    """
    citas_con_presupuesto = []
    for cita in citas:
        vehiculo = cita["cliente"]["vehiculo"]
        presupuesto = calcular_presupuesto(vehiculo["servicios"])
        citas_con_presupuesto.append({
            "id": cita["id"],
            "cliente": cita["cliente"],
            "presupuesto": presupuesto,
        })

    contexto = {
        "citas": citas_con_presupuesto,
    }
    return render(request, "taller/lista_citas.html", contexto)