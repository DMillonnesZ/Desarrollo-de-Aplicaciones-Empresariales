from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cita, Servicio
from .forms import CitaForm


def lista_citas(request):
    citas = Cita.objects.all()

    contexto = {
        "citas": citas
    }

    return render(
        request,
        "taller/lista_citas.html",
        contexto
    )


def crear_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # Validación: evitar cruce de citas
            # (mismo mecánico, misma fecha y hora)
            cruce = Cita.objects.filter(
                mecanico=datos["mecanico"],
                fecha_atencion=datos["fecha_atencion"],
                hora_atencion=datos["hora_atencion"],
            ).exists()

            if cruce:
                messages.error(
                    request,
                    f'Ya existe una cita programada para '
                    f'{datos["mecanico"]} el '
                    f'{datos["fecha_atencion"]} a las '
                    f'{datos["hora_atencion"]}. '
                    f'Elige otro horario o mecánico.'
                )

            else:
                # Guarda la Cita
                cita = form.save(commit=False)
                cita.save()

                # Crea el Servicio asociado
                Servicio.objects.create(
                    cita=cita,
                    tipo=datos["tipo_servicio"],
                    precio=datos["precio_servicio"],
                )

                messages.success(
                    request,
                    "Cita registrada correctamente."
                )

                return redirect("lista_citas")

    else:
        form = CitaForm()

    return render(
        request,
        "taller/crear_cita.html",
        {"form": form}
    )
