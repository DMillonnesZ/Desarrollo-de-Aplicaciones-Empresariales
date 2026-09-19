import uuid as uuid_lib
from django.db import models
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


validar_dni = RegexValidator(
    r'^\d{8}$', 'El DNI debe tener exactamente 8 dígitos numéricos.')
validar_telefono = RegexValidator(
    r'^9\d{8}$', 'El teléfono debe tener 9 dígitos y empezar con 9.')
validar_colegiatura = RegexValidator(
    r'^[A-Z]{2,4}-\d{4,6}$', 'Formato de colegiatura inválido, ej. "ABC-12345".')
validar_solo_letras = RegexValidator(
    r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', 'Este campo solo admite letras y espacios.')


def validar_fecha_no_futura(valor):
    if valor and valor > timezone.now().date():
        raise ValidationError('La fecha no puede ser futura.')


class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Especies'

    def __str__(self):
        return self.nombre


class Persona(models.Model):

    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    nombre = models.CharField(max_length=100, validators=[validar_solo_letras])
    telefono = models.CharField(
        max_length=9, blank=True, validators=[validar_telefono])
    correo = models.EmailField(blank=True)
    activo = models.BooleanField()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Dueno(Persona):
    dni = models.CharField(max_length=8, unique=True, validators=[validar_dni])
    direccion = models.CharField(max_length=200, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.dni})'

    def dar_de_baja(self):
        self.activo = False
        self.save(update_fields=['activo'])


class Especialidad(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nombre


class Veterinario(Persona):
    colegiatura = models.CharField(
        max_length=20, unique=True, validators=[validar_colegiatura])
    especialidades = models.ManyToManyField(
        Especialidad, related_name='veterinarios')
    fecha_ingreso = models.DateField(
        validators=[validar_fecha_no_futura])  # sin default

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.colegiatura})'


class Raza(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    nombre = models.CharField(max_length=80)
    especie = models.ForeignKey(
        Especie, on_delete=models.PROTECT, related_name='razas')
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['especie__nombre', 'nombre']
        constraints = [
            models.UniqueConstraint(
                fields=['nombre', 'especie'], name='raza_unica_por_especie')
        ]

    def __str__(self):
        return f'{self.nombre} ({self.especie.nombre})'


class Mascota(models.Model):
    SEXOS = [('M', 'Macho'), ('H', 'Hembra')]

    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    nombre = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(
        null=True, blank=True, validators=[validar_fecha_no_futura])
    sexo = models.CharField(max_length=1, choices=SEXOS)
    peso_kg = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True,
        validators=[MinValueValidator(0.01), MaxValueValidator(150)]
    )
    dueno = models.ForeignKey(
        Dueno,
        on_delete=models.PROTECT,
        related_name='mascotas'
    )
    raza = models.ForeignKey(
        Raza, on_delete=models.PROTECT, related_name='mascotas')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField()  # sin default

    veterinarios_seguimiento = models.ManyToManyField(
        Veterinario, through='SeguimientoClinico', related_name='mascotas_seguimiento', blank=True
    )

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.raza.nombre})'

    def dar_de_baja(self):
        self.activo = False
        self.save(update_fields=['activo'])


class FichaClinica(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    mascota = models.OneToOneField(
        Mascota, on_delete=models.CASCADE, related_name='ficha_clinica')
    alergias = models.TextField(blank=True)
    condiciones_cronicas = models.TextField(blank=True)
    seguro_veterinario = models.CharField(max_length=100, blank=True)
    contacto_emergencia = models.CharField(max_length=100, blank=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Ficha clínica'
        verbose_name_plural = 'Fichas clínicas'

    def __str__(self):
        return f'Ficha clínica de {self.mascota.nombre}'


class Medicamento(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField()  # sin default
    precio_unitario = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Atencion(models.Model):
    TIPOS = [('CONSULTA', 'Consulta'), ('VACUNACION', 'Vacunación')]

    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    mascota = models.ForeignKey(
        Mascota, on_delete=models.PROTECT, related_name='atenciones')
    veterinario = models.ForeignKey(
        Veterinario, on_delete=models.PROTECT, related_name='atenciones')
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length=12, choices=TIPOS, editable=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        
        return f'{self.get_tipo_display()} - {self.mascota.nombre} ({self.fecha:%d/%m/%Y %H:%M})'# type: ignore[attr-defined]


class Consulta(Atencion):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    ]
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    estado = models.CharField(max_length=12, choices=ESTADOS)  # sin default
    costo = models.DecimalField(max_digits=8, decimal_places=2, validators=[
                                MinValueValidator(0)])  # sin default

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.mascota.nombre} - {self.fecha:%d/%m/%Y %H:%M}'

    def save(self, *args, **kwargs):
        self.tipo = 'CONSULTA'
        super().save(*args, **kwargs)

    def clean(self):
        if self.estado == 'ATENDIDA' and not self.diagnostico:
            raise ValidationError(
                'Una consulta atendida debe tener diagnóstico.')
        if self.estado == 'ATENDIDA' and self.fecha > timezone.now():
            raise ValidationError(
                'No se puede marcar como atendida una consulta con fecha futura.')

    def anular(self, motivo_anulacion='', usuario=''):
        estado_anterior = self.estado
        self.estado = 'CANCELADA'
        self.save(update_fields=['estado'])
        _registrar_auditoria_atencion(self, accion='ANULACION', usuario=usuario, detalle=motivo_anulacion,
                                    estado_anterior=estado_anterior, estado_nuevo=self.estado)


class Vacunacion(Atencion):
    nombre_vacuna = models.CharField(max_length=100)
    proxima_dosis = models.DateField(null=True, blank=True)
    lote = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Vacunación'
        verbose_name_plural = 'Vacunaciones'

    def __str__(self):
        return f'{self.nombre_vacuna} - {self.mascota.nombre}'

    def save(self, *args, **kwargs):
        self.tipo = 'VACUNACION'
        super().save(*args, **kwargs)

    def clean(self):
        if self.proxima_dosis and self.fecha and self.proxima_dosis <= self.fecha.date():
            raise ValidationError(
                'La próxima dosis debe ser posterior a la fecha de aplicación.')


class DetalleReceta(models.Model):
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    consulta = models.ForeignKey(
        Consulta, on_delete=models.CASCADE, related_name='detalles_receta')
    medicamento = models.ForeignKey(
        Medicamento, on_delete=models.PROTECT, related_name='recetas')
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    dosis = models.CharField(max_length=100)
    indicaciones = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['consulta', 'medicamento'], name='medicamento_unico_por_consulta')
        ]

    def __str__(self):
        return f'{self.medicamento.nombre} x{self.cantidad} ({self.consulta})'

    def clean(self):
        
        if self.medicamento_id and self.cantidad > self.medicamento.stock: # type: ignore[attr-defined]
            raise ValidationError(
                f'Stock insuficiente de {self.medicamento.nombre} (disponible: {self.medicamento.stock}).'
            )


class SeguimientoClinico(models.Model):
    ROLES = [
        ('TITULAR', 'Veterinario titular'),
        ('INTERCONSULTA', 'Interconsulta / especialista'),
    ]
    uuid = models.UUIDField(default=uuid_lib.uuid4,
                            editable=False, unique=True)
    mascota = models.ForeignKey(
        Mascota, on_delete=models.CASCADE, related_name='seguimientos')
    veterinario = models.ForeignKey(
        Veterinario, on_delete=models.CASCADE, related_name='seguimientos')
    fecha_asignacion = models.DateField(
        validators=[validar_fecha_no_futura])  # sin default
    rol = models.CharField(max_length=15, choices=ROLES)
    activo = models.BooleanField()

    class Meta:
        verbose_name = 'Seguimiento clínico'
        verbose_name_plural = 'Seguimientos clínicos'
        constraints = [
            models.UniqueConstraint(
                fields=['mascota', 'veterinario', 'rol'], name='seguimiento_unico')
        ]

    def __str__(self):
        
        return f'{self.veterinario.nombre} sigue a {self.mascota.nombre} ({self.get_rol_display()})' # type: ignore[attr-defined]


class AuditoriaAtencion(models.Model):
    ACCIONES = [
        ('CREACION', 'Creación'),
        ('MODIFICACION', 'Modificación'),
        ('ANULACION', 'Anulación'),
        ('ELIMINACION', 'Eliminación'),
    ]
    atencion_id = models.PositiveIntegerField()
    tipo = models.CharField(max_length=12)
    mascota_nombre = models.CharField(max_length=80)
    dueno_nombre = models.CharField(max_length=100)
    dueno_dni = models.CharField(max_length=8)
    accion = models.CharField(max_length=15, choices=ACCIONES)
    estado_anterior = models.CharField(max_length=12, blank=True)
    estado_nuevo = models.CharField(max_length=12, blank=True)
    usuario = models.CharField(max_length=100, blank=True)
    detalle = models.TextField(blank=True)
    fecha_accion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_accion']
        verbose_name = 'Auditoría de atención'
        verbose_name_plural = 'Auditorías de atenciones'

    def __str__(self):
        return f'Atención #{self.atencion_id} - {self.accion} ({self.fecha_accion:%d/%m/%Y %H:%M})'


class AuditoriaMascota(models.Model):
    ACCIONES = [('ALTA', 'Alta'), ('BAJA', 'Baja')]

    mascota_id = models.PositiveIntegerField()
    mascota_nombre = models.CharField(max_length=80)
    dueno_nombre = models.CharField(max_length=100)
    dueno_dni = models.CharField(max_length=8)
    accion = models.CharField(max_length=4, choices=ACCIONES)
    fecha_accion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_accion']
        verbose_name = 'Auditoría de mascota'
        verbose_name_plural = 'Auditorías de mascotas'

    def __str__(self):
        return f'Mascota #{self.mascota_id} - {self.accion} ({self.fecha_accion:%d/%m/%Y %H:%M})'


def _registrar_auditoria_atencion(atencion, accion, usuario='', detalle='', estado_anterior='', estado_nuevo=''):
    AuditoriaAtencion.objects.create(
        atencion_id=atencion.id,
        tipo=atencion.tipo,
        mascota_nombre=atencion.mascota.nombre,
        dueno_nombre=atencion.mascota.dueno.nombre,
        dueno_dni=atencion.mascota.dueno.dni,
        accion=accion,
        estado_anterior=estado_anterior,
        estado_nuevo=estado_nuevo,
        usuario=usuario,
        detalle=detalle,
    )


@receiver(pre_delete, sender=Atencion)
def auditar_eliminacion_atencion(sender, instance, **kwargs):
    _registrar_auditoria_atencion(
        instance, accion='ELIMINACION',
        detalle=f'Eliminación física de {instance.get_tipo_display()} con fecha {instance.fecha:%d/%m/%Y %H:%M}.'
    )


@receiver(post_save, sender=Consulta)
def auditar_alta_consulta(sender, instance, created, **kwargs):
    if created:
        _registrar_auditoria_atencion(
            instance, accion='CREACION', estado_nuevo=instance.estado)


@receiver(post_save, sender=Vacunacion)
def auditar_alta_vacunacion(sender, instance, created, **kwargs):
    if created:
        _registrar_auditoria_atencion(instance, accion='CREACION')


@receiver(pre_save, sender=Mascota)
def _cachear_estado_previo_mascota(sender, instance, **kwargs):
    if instance.pk:
        instance._activo_anterior = Mascota.objects.filter(pk=instance.pk).values_list(
            'activo', flat=True
        ).first()
    else:
        instance._activo_anterior = None


@receiver(post_save, sender=Mascota)
def auditar_estado_mascota(sender, instance, created, **kwargs):
    anterior = getattr(instance, '_activo_anterior', None)
    if created or (anterior is not None and anterior != instance.activo):
        AuditoriaMascota.objects.create(
            mascota_id=instance.pk,
            mascota_nombre=instance.nombre,
            dueno_nombre=instance.dueno.nombre,
            dueno_dni=instance.dueno.dni,
            accion='ALTA' if instance.activo else 'BAJA',
        )
