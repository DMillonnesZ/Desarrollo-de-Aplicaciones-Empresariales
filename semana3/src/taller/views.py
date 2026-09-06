from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cita
from .forms import CitaForm


def lista_citas(request):
    citas = Cita.objects.all()
    contexto = {"citas": citas}
    return render(request, "taller/lista_citas.html", contexto)


def crear_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)

        if form.is_valid():
            cita = form.save()

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
