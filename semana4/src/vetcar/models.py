from django.db import models


class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Dueño'
        verbose_name_plural = 'Dueños'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.dni})'


class Raza(models.Model):
    ESPECIES = [
        ('PERRO', 'Perro'),
        ('GATO', 'Gato'),
        ('AVE', 'Ave'),
        ('OTRO', 'Otro'),
    ]
    nombre = models.CharField(max_length=80)
    especie = models.CharField(max_length=30, choices=ESPECIES)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['especie', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.get_especie_display()})'


class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    colegiatura = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} - {self.especialidad}'


class Mascota(models.Model):
    SEXOS = [('M', 'Macho'), ('H', 'Hembra')]
    nombre = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXOS)
    peso_kg = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    dueno = models.ForeignKey(
        Dueno, on_delete=models.CASCADE, related_name='mascotas')
    raza = models.ForeignKey(
        Raza, on_delete=models.PROTECT, related_name='mascotas')

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.raza.nombre})'


class Consulta(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    ]
    mascota = models.ForeignKey(
        Mascota, on_delete=models.CASCADE, related_name='consultas')
    veterinario = models.ForeignKey(
        Veterinario, on_delete=models.PROTECT, related_name='consultas')
    fecha = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    estado = models.CharField(
        max_length=12, choices=ESTADOS, default='PENDIENTE')

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f'{self.mascota.nombre} - {self.fecha:%d/%m/%Y %H:%M}'
