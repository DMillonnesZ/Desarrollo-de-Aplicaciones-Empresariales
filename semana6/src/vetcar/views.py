from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Dueno, Veterinario, Raza, Mascota, Consulta, Vacunacion,
    FichaClinica, SeguimientoClinico, DetalleReceta,
)
from .forms import (
    DuenoForm, VeterinarioForm, RazaForm, MascotaForm, ConsultaForm, VacunacionForm,
    FichaClinicaForm, SeguimientoClinicoForm, DetalleRecetaForm,
)


# ---------------------------------------------------------------------------
# DUENO
# ---------------------------------------------------------------------------
def listar_duenos(request):
    duenos = Dueno.objects.all()
    return render(request, 'vetcar/dueno_list.html', {'duenos': duenos})


def crear_dueno(request):
    if request.method == 'POST':
        form = DuenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_duenos')
    else:
        form = DuenoForm()
    return render(request, 'vetcar/dueno_form.html', {'form': form})


def editar_dueno(request, uuid):
    dueno = get_object_or_404(Dueno, uuid=uuid)
    if request.method == 'POST':
        form = DuenoForm(request.POST, instance=dueno)
        if form.is_valid():
            form.save()
            return redirect('listar_duenos')
    else:
        form = DuenoForm(instance=dueno)
    return render(request, 'vetcar/dueno_form.html', {'form': form, 'dueno': dueno})


def eliminar_dueno(request, uuid):
    dueno = get_object_or_404(Dueno, uuid=uuid)
    if request.method == 'POST':
        dueno.delete()
        return redirect('listar_duenos')
    return render(request, 'vetcar/dueno_confirmar_eliminar.html', {'dueno': dueno})


# ---------------------------------------------------------------------------
# VETERINARIO
# ---------------------------------------------------------------------------
def listar_veterinarios(request):
    veterinarios = Veterinario.objects.prefetch_related('especialidades').all()
    return render(request, 'vetcar/veterinario_list.html', {'veterinarios': veterinarios})


def crear_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'vetcar/veterinario_form.html', {'form': form})


def editar_veterinario(request, uuid):
    veterinario = get_object_or_404(Veterinario, uuid=uuid)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('listar_veterinarios')
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, 'vetcar/veterinario_form.html', {'form': form, 'veterinario': veterinario})


def eliminar_veterinario(request, uuid):
    veterinario = get_object_or_404(Veterinario, uuid=uuid)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('listar_veterinarios')
    return render(request, 'vetcar/veterinario_confirmar_eliminar.html', {'veterinario': veterinario})


def veterinario_detalle(request, uuid):
    """Vista de detalle: usa prefetch_related para el M2M con Mascota
    (Ejercicio 12: recorrido del modelo intermedio SeguimientoClinico)."""
    veterinario = get_object_or_404(
        Veterinario.objects.prefetch_related('seguimientos__mascota', 'especialidades'),
        uuid=uuid
    )
    return render(request, 'vetcar/veterinario_detalle.html', {'veterinario': veterinario})


# ---------------------------------------------------------------------------
# RAZA
# ---------------------------------------------------------------------------
def listar_razas(request):
    razas = Raza.objects.select_related('especie').all()
    return render(request, 'vetcar/raza_list.html', {'razas': razas})


def crear_raza(request):
    if request.method == 'POST':
        form = RazaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_razas')
    else:
        form = RazaForm()
    return render(request, 'vetcar/raza_form.html', {'form': form})


def editar_raza(request, uuid):
    raza = get_object_or_404(Raza, uuid=uuid)
    if request.method == 'POST':
        form = RazaForm(request.POST, instance=raza)
        if form.is_valid():
            form.save()
            return redirect('listar_razas')
    else:
        form = RazaForm(instance=raza)
    return render(request, 'vetcar/raza_form.html', {'form': form, 'raza': raza})


def eliminar_raza(request, uuid):
    raza = get_object_or_404(Raza, uuid=uuid)
    if request.method == 'POST':
        raza.delete()
        return redirect('listar_razas')
    return render(request, 'vetcar/raza_confirmar_eliminar.html', {'raza': raza})


# ---------------------------------------------------------------------------
# MASCOTA
# ---------------------------------------------------------------------------
def listar_mascotas(request):
    mascotas = Mascota.objects.select_related('dueno', 'raza').all()
    return render(request, 'vetcar/mascota_list.html', {'mascotas': mascotas})


def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'vetcar/mascota_form.html', {'form': form})


def editar_mascota(request, uuid):
    mascota = get_object_or_404(Mascota, uuid=uuid)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'vetcar/mascota_form.html', {'form': form, 'mascota': mascota})


def eliminar_mascota(request, uuid):
    mascota = get_object_or_404(Mascota, uuid=uuid)
    if request.method == 'POST':
        mascota.dar_de_baja()
        return redirect('listar_mascotas')
    return render(request, 'vetcar/mascota_confirmar_eliminar.html', {'mascota': mascota})


def mascota_detalle(request, uuid):
    mascota = get_object_or_404(
        Mascota.objects.select_related('dueno', 'raza', 'ficha_clinica')
                    .prefetch_related('atenciones', 'seguimientos__veterinario'),
        uuid=uuid
    )
    return render(request, 'vetcar/mascota_detalle.html', {'mascota': mascota})


# ---------------------------------------------------------------------------
# CONSULTA
# ---------------------------------------------------------------------------
def listar_consultas(request):
    consultas = Consulta.objects.select_related('mascota', 'veterinario').all()
    return render(request, 'vetcar/consulta_list.html', {'consultas': consultas})


def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'vetcar/consulta_form.html', {'form': form})


def editar_consulta(request, uuid):
    consulta = get_object_or_404(Consulta, uuid=uuid)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'vetcar/consulta_form.html', {'form': form, 'consulta': consulta})


def anular_consulta(request, uuid):
    consulta = get_object_or_404(Consulta, uuid=uuid)
    if request.method == 'POST':
        consulta.anular(motivo_anulacion=request.POST.get('motivo', ''), usuario=str(request.user))
        return redirect('listar_consultas')
    return render(request, 'vetcar/consulta_confirmar_anular.html', {'consulta': consulta})


# ---------------------------------------------------------------------------
# VACUNACION
# ---------------------------------------------------------------------------
def listar_vacunaciones(request):
    vacunaciones = Vacunacion.objects.select_related('mascota', 'veterinario').all()
    return render(request, 'vetcar/vacunacion_list.html', {'vacunaciones': vacunaciones})


def crear_vacunacion(request):
    if request.method == 'POST':
        form = VacunacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vacunaciones')
    else:
        form = VacunacionForm()
    return render(request, 'vetcar/vacunacion_form.html', {'form': form})


def editar_vacunacion(request, uuid):
    vacunacion = get_object_or_404(Vacunacion, uuid=uuid)
    if request.method == 'POST':
        form = VacunacionForm(request.POST, instance=vacunacion)
        if form.is_valid():
            form.save()
            return redirect('listar_vacunaciones')
    else:
        form = VacunacionForm(instance=vacunacion)
    return render(request, 'vetcar/vacunacion_form.html', {'form': form, 'vacunacion': vacunacion})


def eliminar_vacunacion(request, uuid):
    vacunacion = get_object_or_404(Vacunacion, uuid=uuid)
    if request.method == 'POST':
        vacunacion.delete()
        return redirect('listar_vacunaciones')
    return render(request, 'vetcar/vacunacion_confirmar_eliminar.html', {'vacunacion': vacunacion})


# ---------------------------------------------------------------------------
# FICHA CLINICA (relación 1:1 con Mascota)
# Al ser 1:1, no hay "listar" ni "crear varias": una sola vista maneja
# crear-o-editar según si la mascota ya tiene ficha o no.
# ---------------------------------------------------------------------------
def gestionar_ficha_clinica(request, mascota_uuid):
    mascota = get_object_or_404(Mascota, uuid=mascota_uuid)
    ficha = getattr(mascota, 'ficha_clinica', None)

    if request.method == 'POST':
        form = FichaClinicaForm(request.POST, instance=ficha)
        if form.is_valid():
            nueva_ficha = form.save(commit=False)
            nueva_ficha.mascota = mascota
            nueva_ficha.save()
            return redirect('mascota_detalle', uuid=mascota.uuid)
    else:
        form = FichaClinicaForm(instance=ficha)
    return render(request, 'vetcar/ficha_clinica_form.html', {'form': form, 'mascota': mascota})


# ---------------------------------------------------------------------------
# SEGUIMIENTO CLINICO (modelo intermedio N:M Mascota <-> Veterinario)
# Siempre se crea/elimina desde el detalle de una mascota concreta.
# ---------------------------------------------------------------------------
def crear_seguimiento(request, mascota_uuid):
    mascota = get_object_or_404(Mascota, uuid=mascota_uuid)
    if request.method == 'POST':
        form = SeguimientoClinicoForm(request.POST)
        if form.is_valid():
            seguimiento = form.save(commit=False)
            seguimiento.mascota = mascota
            seguimiento.save()
            return redirect('mascota_detalle', uuid=mascota.uuid)
    else:
        form = SeguimientoClinicoForm()
    return render(request, 'vetcar/seguimiento_form.html', {'form': form, 'mascota': mascota})


def editar_seguimiento(request, uuid):
    seguimiento = get_object_or_404(SeguimientoClinico, uuid=uuid)
    if request.method == 'POST':
        form = SeguimientoClinicoForm(request.POST, instance=seguimiento)
        if form.is_valid():
            form.save()
            return redirect('mascota_detalle', uuid=seguimiento.mascota.uuid)
    else:
        form = SeguimientoClinicoForm(instance=seguimiento)
    return render(request, 'vetcar/seguimiento_form.html', {'form': form, 'mascota': seguimiento.mascota})


def eliminar_seguimiento(request, uuid):
    seguimiento = get_object_or_404(SeguimientoClinico, uuid=uuid)
    mascota_uuid = seguimiento.mascota.uuid
    if request.method == 'POST':
        seguimiento.delete()
        return redirect('mascota_detalle', uuid=mascota_uuid)
    return render(request, 'vetcar/seguimiento_confirmar_eliminar.html', {'seguimiento': seguimiento})


# ---------------------------------------------------------------------------
# DETALLE RECETA (modelo intermedio N:M Consulta <-> Medicamento)
# Siempre se crea/elimina desde el detalle de una consulta concreta.
# ---------------------------------------------------------------------------
def crear_detalle_receta(request, consulta_uuid):
    consulta = get_object_or_404(Consulta, uuid=consulta_uuid)
    if request.method == 'POST':
        form = DetalleRecetaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.consulta = consulta
            detalle.save()
            return redirect('editar_consulta', uuid=consulta.uuid)
    else:
        form = DetalleRecetaForm()
    return render(request, 'vetcar/detalle_receta_form.html', {'form': form, 'consulta': consulta})


def eliminar_detalle_receta(request, uuid):
    detalle = get_object_or_404(DetalleReceta, uuid=uuid)
    consulta_uuid = detalle.consulta.uuid
    if request.method == 'POST':
        detalle.delete()
        return redirect('editar_consulta', uuid=consulta_uuid)
    return render(request, 'vetcar/detalle_receta_confirmar_eliminar.html', {'detalle': detalle})