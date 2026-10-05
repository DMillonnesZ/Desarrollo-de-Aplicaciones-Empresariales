from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.db.models import F, Sum, Count, DecimalField

from .models import (
    Dueno, Veterinario, Raza, Mascota, Consulta, Vacunacion,
    FichaClinica, SeguimientoClinico, DetalleReceta, Medicamento,
)

from .forms import (
    DuenoForm, VeterinarioForm, RazaForm, MascotaForm,
    ConsultaForm, VacunacionForm, FichaClinicaForm,
    SeguimientoClinicoForm, DetalleRecetaForm,
    RegistrarRecetaForm,
)


# ============================================================
# DUEÑO
# ============================================================

def listar_duenos(request):
    duenos = Dueno.objects.all()

    return render(
        request,
        'vetcar/dueno_list.html',
        {'duenos': duenos},
    )


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

    return render(
        request,
        'vetcar/dueno_form.html',
        {'form': form, 'dueno': dueno},
    )


def eliminar_dueno(request, uuid):
    dueno = get_object_or_404(Dueno, uuid=uuid)

    if request.method == 'POST':
        dueno.delete()
        return redirect('listar_duenos')

    return render(
        request,
        'vetcar/dueno_confirmar_eliminar.html',
        {'dueno': dueno},
    )


# ============================================================
# VETERINARIO
# ============================================================

def listar_veterinarios(request):
    veterinarios = Veterinario.objects.prefetch_related(
        'especialidades'
    ).all()

    return render(
        request,
        'vetcar/veterinario_list.html',
        {'veterinarios': veterinarios},
    )


def crear_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_veterinarios')
    else:
        form = VeterinarioForm()

    return render(
        request,
        'vetcar/veterinario_form.html',
        {'form': form},
    )


def editar_veterinario(request, uuid):
    veterinario = get_object_or_404(Veterinario, uuid=uuid)

    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)

        if form.is_valid():
            form.save()
            return redirect('listar_veterinarios')
    else:
        form = VeterinarioForm(instance=veterinario)

    return render(
        request,
        'vetcar/veterinario_form.html',
        {'form': form, 'veterinario': veterinario},
    )


def eliminar_veterinario(request, uuid):
    veterinario = get_object_or_404(Veterinario, uuid=uuid)

    if request.method == 'POST':
        veterinario.delete()
        return redirect('listar_veterinarios')

    return render(
        request,
        'vetcar/veterinario_confirmar_eliminar.html',
        {'veterinario': veterinario},
    )


def veterinario_detalle(request, uuid):
    veterinario = get_object_or_404(
        Veterinario.objects.prefetch_related(
            'seguimientos__mascota',
            'especialidades',
        ),
        uuid=uuid,
    )

    return render(
        request,
        'vetcar/veterinario_detalle.html',
        {'veterinario': veterinario},
    )


# ============================================================
# RAZA
# ============================================================

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

    return render(
        request,
        'vetcar/raza_form.html',
        {'form': form, 'raza': raza},
    )


def eliminar_raza(request, uuid):
    raza = get_object_or_404(Raza, uuid=uuid)

    if request.method == 'POST':
        raza.delete()
        return redirect('listar_razas')

    return render(
        request,
        'vetcar/raza_confirmar_eliminar.html',
        {'raza': raza},
    )


# ============================================================
# MASCOTA
# ============================================================

def listar_mascotas(request):
    mascotas = Mascota.objects.select_related('dueno', 'raza').all()

    return render(
        request,
        'vetcar/mascota_list.html',
        {'mascotas': mascotas},
    )


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

    return render(
        request,
        'vetcar/mascota_form.html',
        {'form': form, 'mascota': mascota},
    )


def eliminar_mascota(request, uuid):
    mascota = get_object_or_404(Mascota, uuid=uuid)

    if request.method == 'POST':
        mascota.dar_de_baja()
        return redirect('listar_mascotas')

    return render(
        request,
        'vetcar/mascota_confirmar_eliminar.html',
        {'mascota': mascota},
    )


def mascota_detalle(request, uuid):
    mascota = get_object_or_404(
        Mascota.objects.select_related(
            'dueno',
            'raza',
            'ficha_clinica',
        ).prefetch_related(
            'atenciones',
            'seguimientos__veterinario',
        ),
        uuid=uuid,
    )

    return render(
        request,
        'vetcar/mascota_detalle.html',
        {'mascota': mascota},
    )


# ============================================================
# CONSULTA
# ============================================================

def listar_consultas(request):
    consultas = Consulta.objects.select_related(
        'mascota',
        'veterinario',
    ).all()

    return render(
        request,
        'vetcar/consulta_list.html',
        {'consultas': consultas},
    )


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

    return render(
        request,
        'vetcar/consulta_form.html',
        {'form': form, 'consulta': consulta},
    )


def anular_consulta(request, uuid):
    consulta = get_object_or_404(Consulta, uuid=uuid)

    if request.method == 'POST':
        consulta.anular(
            motivo_anulacion=request.POST.get('motivo', ''),
            usuario=str(request.user),
        )
        return redirect('listar_consultas')

    return render(
        request,
        'vetcar/consulta_confirmar_anular.html',
        {'consulta': consulta},
    )


# ============================================================
# VACUNACIÓN
# ============================================================

def listar_vacunaciones(request):
    vacunaciones = Vacunacion.objects.select_related(
        'mascota',
        'veterinario',
    ).all()

    return render(
        request,
        'vetcar/vacunacion_list.html',
        {'vacunaciones': vacunaciones},
    )


def crear_vacunacion(request):
    if request.method == 'POST':
        form = VacunacionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_vacunaciones')
    else:
        form = VacunacionForm()

    return render(
        request,
        'vetcar/vacunacion_form.html',
        {'form': form},
    )


def editar_vacunacion(request, uuid):
    vacunacion = get_object_or_404(Vacunacion, uuid=uuid)

    if request.method == 'POST':
        form = VacunacionForm(request.POST, instance=vacunacion)

        if form.is_valid():
            form.save()
            return redirect('listar_vacunaciones')
    else:
        form = VacunacionForm(instance=vacunacion)

    return render(
        request,
        'vetcar/vacunacion_form.html',
        {'form': form, 'vacunacion': vacunacion},
    )


def eliminar_vacunacion(request, uuid):
    vacunacion = get_object_or_404(Vacunacion, uuid=uuid)

    if request.method == 'POST':
        vacunacion.delete()
        return redirect('listar_vacunaciones')

    return render(
        request,
        'vetcar/vacunacion_confirmar_eliminar.html',
        {'vacunacion': vacunacion},
    )


# ============================================================
# FICHA CLÍNICA
# ============================================================

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

    return render(
        request,
        'vetcar/ficha_clinica_form.html',
        {'form': form, 'mascota': mascota},
    )


# ============================================================
# SEGUIMIENTO CLÍNICO
# ============================================================

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

    return render(
        request,
        'vetcar/seguimiento_form.html',
        {'form': form, 'mascota': mascota},
    )


def editar_seguimiento(request, uuid):
    seguimiento = get_object_or_404(SeguimientoClinico, uuid=uuid)

    if request.method == 'POST':
        form = SeguimientoClinicoForm(request.POST, instance=seguimiento)

        if form.is_valid():
            form.save()
            return redirect(
                'mascota_detalle',
                uuid=seguimiento.mascota.uuid,
            )
    else:
        form = SeguimientoClinicoForm(instance=seguimiento)

    return render(
        request,
        'vetcar/seguimiento_form.html',
        {'form': form, 'mascota': seguimiento.mascota},
    )


def eliminar_seguimiento(request, uuid):
    seguimiento = get_object_or_404(SeguimientoClinico, uuid=uuid)
    mascota_uuid = seguimiento.mascota.uuid

    if request.method == 'POST':
        seguimiento.delete()
        return redirect('mascota_detalle', uuid=mascota_uuid)

    return render(
        request,
        'vetcar/seguimiento_confirmar_eliminar.html',
        {'seguimiento': seguimiento},
    )


# ============================================================
# DETALLE DE RECETA — REGISTRO SIMPLE EXISTENTE
# ============================================================

def crear_detalle_receta(request, consulta_uuid):
    consulta = get_object_or_404(Consulta, uuid=consulta_uuid)

    if request.method == 'POST':
        form = DetalleRecetaForm(request.POST)

        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.consulta = consulta

            # Guardamos el precio para los futuros reportes.
            detalle.precio_unitario = detalle.medicamento.precio_unitario

            detalle.save()
            return redirect('editar_consulta', uuid=consulta.uuid)
    else:
        form = DetalleRecetaForm()

    return render(
        request,
        'vetcar/detalle_receta_form.html',
        {'form': form, 'consulta': consulta},
    )


def eliminar_detalle_receta(request, uuid):
    detalle = get_object_or_404(DetalleReceta, uuid=uuid)
    consulta_uuid = detalle.consulta.uuid

    if request.method == 'POST':
        detalle.delete()
        return redirect('editar_consulta', uuid=consulta_uuid)

    return render(
        request,
        'vetcar/detalle_receta_confirmar_eliminar.html',
        {'detalle': detalle},
    )


# ============================================================
# EJERCICIO 3 — TRANSACCIÓN CON ATOMIC Y F
# ============================================================

class StockInsuficienteError(Exception):
    """Permite cancelar toda la operación cuando falta stock."""

    pass


def registrar_receta(request, consulta_uuid):
    consulta = get_object_or_404(Consulta, uuid=consulta_uuid)
    error = None

    if request.method == 'POST':
        form = RegistrarRecetaForm(request.POST)

        if form.is_valid():
            medicamento = form.cleaned_data['medicamento']
            cantidad = form.cleaned_data['cantidad']

            try:
                # Si ocurre un error, se revierten todas las escrituras.
                with transaction.atomic():

                    # 1. Crear el detalle con el precio de esta operación.
                    DetalleReceta.objects.create(
                        consulta=consulta,
                        medicamento=medicamento,
                        cantidad=cantidad,
                        precio_unitario=medicamento.precio_unitario,
                        dosis=form.cleaned_data['dosis'],
                        indicaciones=form.cleaned_data['indicaciones'],
                    )

                    # 2. Descontar stock en la base de datos.
                    # La condición y el descuento forman un mismo UPDATE.
                    actualizados = Medicamento.objects.filter(
                        pk=medicamento.pk,
                        stock__gte=cantidad,
                    ).update(
                        stock=F('stock') - cantidad,
                    )

                    # 3. Si no pudo descontarse, provocar el rollback.
                    if actualizados == 0:
                        raise StockInsuficienteError(
                            f'Stock insuficiente de {medicamento.nombre}. '
                            'Operación cancelada: no se guardó la receta '
                            'ni se modificó el costo.'
                        )

                    # 4. Sumar el importe al costo de la consulta.
                    importe = cantidad * medicamento.precio_unitario

                    Consulta.objects.filter(
                        pk=consulta.pk,
                    ).update(
                        costo=F('costo') + importe,
                    )

            # Se capturan los errores DESPUÉS de salir del atomic.
            except StockInsuficienteError as exc:
                error = str(exc)

            except IntegrityError:
                if DetalleReceta.objects.filter(
                    consulta=consulta,
                    medicamento=medicamento,
                ).exists():
                    error = (
                        'Ese medicamento ya está en la receta '
                        'de esta consulta.'
                    )
                else:
                    error = (
                        'No se pudo registrar la receta por un conflicto '
                        'de integridad. La operación se revirtió.'
                    )

            else:
                messages.success(
                    request,
                    'Receta registrada, stock descontado '
                    'y costo actualizado correctamente.',
                )

                # Post/Redirect/Get: redirigir después de guardar.
                return redirect(
                    'editar_consulta',
                    uuid=consulta.uuid,
                )

    else:
        form = RegistrarRecetaForm()

    return render(
        request,
        'vetcar/registrar_receta.html',
        {
            'form': form,
            'consulta': consulta,
            'error': error,
        },
    )


# ============================================================
# EJERCICIO 6 — REPORTE CON AGGREGATE Y ANNOTATE
# ============================================================

def reporte(request):
    totales = DetalleReceta.objects.aggregate(
        total_unidades=Sum('cantidad'),
        total_valorizado=Sum(
            F('cantidad') * F('medicamento__precio_unitario'),
            output_field=DecimalField(
                max_digits=12,
                decimal_places=2,
            ),
        ),
    )

    por_mascota = Mascota.objects.annotate(
        num_atenciones=Count('atenciones'),
    ).order_by('-num_atenciones')

    por_estado = Consulta.objects.values('estado').annotate(
        total=Count('id'),
        ingresos=Sum('costo'),
    ).order_by('-total')

    return render(
        request,
        'vetcar/reporte.html',
        {
            'totales': totales,
            'por_mascota': por_mascota,
            'por_estado': por_estado,
        },
    )