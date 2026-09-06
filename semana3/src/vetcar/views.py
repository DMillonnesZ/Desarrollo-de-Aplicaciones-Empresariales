from django.shortcuts import render, redirect, get_object_or_404
from .models import Dueno, Raza, Veterinario, Mascota, Consulta
from .forms import DuenoForm, RazaForm, VeterinarioForm, MascotaForm, ConsultaForm

ENTIDADES = {
    'duenos': {
        'model': Dueno, 'form': DuenoForm, 'titulo': 'Dueños',
        'columnas': ['nombre', 'dni', 'telefono', 'correo'],
    },
    'razas': {
        'model': Raza, 'form': RazaForm, 'titulo': 'Razas',
        'columnas': ['nombre', 'especie', 'descripcion'],
    },
    'veterinarios': {
        'model': Veterinario, 'form': VeterinarioForm, 'titulo': 'Veterinarios',
        'columnas': ['nombre', 'colegiatura', 'especialidad', 'telefono'],
    },
    'mascotas': {
        'model': Mascota, 'form': MascotaForm, 'titulo': 'Mascotas',
        'columnas': ['nombre', 'raza', 'sexo', 'peso_kg', 'dueno'],
    },
    'consultas': {
        'model': Consulta, 'form': ConsultaForm, 'titulo': 'Consultas',
        'columnas': ['fecha', 'mascota', 'veterinario', 'motivo', 'estado'],
    },
}


def inicio(request):
    contexto = {
        'total_duenos': Dueno.objects.count(),
        'total_mascotas': Mascota.objects.count(),
        'pendientes': Consulta.objects.filter(estado='PENDIENTE').count(),
    }
    return render(request, 'vetcar/inicio.html', contexto)


def listar(request, entidad):
    cfg = ENTIDADES[entidad]
    objetos = cfg['model'].objects.all()
    filas = []
    for obj in objetos:
        valores = []
        for col in cfg['columnas']:
            metodo = getattr(obj, f'get_{col}_display', None)
            valores.append(metodo() if metodo else getattr(obj, col))
        filas.append({'obj': obj, 'valores': valores})
    contexto = {
        'entidad': entidad,
        'titulo': cfg['titulo'],
        'columnas': [c.replace('_', ' ').title() for c in cfg['columnas']],
        'filas': filas,
    }
    return render(request, 'vetcar/lista.html', contexto)


def crear(request, entidad):
    cfg = ENTIDADES[entidad]
    if request.method == 'POST':
        form = cfg['form'](request.POST)
        if form.is_valid():
            form.save()
            return redirect('vetcar:listar', entidad=entidad)
    else:
        form = cfg['form']()
    contexto = {'form': form, 'entidad': entidad,
                'titulo': f"Nuevo registro - {cfg['titulo']}"}
    return render(request, 'vetcar/formulario.html', contexto)


def editar(request, entidad, pk):
    cfg = ENTIDADES[entidad]
    obj = get_object_or_404(cfg['model'], pk=pk)
    if request.method == 'POST':
        form = cfg['form'](request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('vetcar:listar', entidad=entidad)
    else:
        form = cfg['form'](instance=obj)
    contexto = {'form': form, 'entidad': entidad,
                'titulo': f"Editar - {cfg['titulo']}"}
    return render(request, 'vetcar/formulario.html', contexto)


def eliminar(request, entidad, pk):
    cfg = ENTIDADES[entidad]
    obj = get_object_or_404(cfg['model'], pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('vetcar:listar', entidad=entidad)
    contexto = {'obj': obj, 'entidad': entidad, 'titulo': cfg['titulo']}
    return render(request, 'vetcar/confirmar_eliminar.html', contexto)


def historial(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    consultas = Consulta.objects.filter(mascota=mascota).order_by('-fecha')
    return render(request, 'vetcar/historial.html',
                  {'mascota': mascota, 'consultas': consultas})