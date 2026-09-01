from django.shortcuts import render, redirect
from django.contrib import messages
from .models import citas, calcular_presupuesto, existe_cruce_horario, agregar_cita
from .forms import CitaForm


def lista_citas(request):
    citas_con_presupuesto = []
    for cita in citas:
        vehiculo = cita["cliente"]["vehiculo"]
        presupuesto = calcular_presupuesto(vehiculo["servicios"])
        citas_con_presupuesto.append({
            "id": cita["id"],
            "cliente": cita["cliente"],
            "presupuesto": presupuesto,
        })

    contexto = {"citas": citas_con_presupuesto}
    return render(request, "taller/lista_citas.html", contexto)


def crear_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            programacion = f'{datos["fecha_atencion"]} {datos["hora_atencion"]}'

            # Validación: evitar cruce de citas (mismo mecánico, mismo horario)
            if existe_cruce_horario(programacion, datos["mecanico"]):
                messages.error(
                    request,
                    f'Ya existe una cita programada para {datos["mecanico"]} '
                    f'el {datos["fecha_atencion"]} a las {datos["hora_atencion"]}. '
                    f'Elige otro horario o mecánico.'
                )
            else:
                agregar_cita(datos)
                messages.success(request, "Cita registrada correctamente.")
                return redirect("lista_citas")
    else:
        form = CitaForm()

    return render(request, "taller/crear_cita.html", {"form": form})