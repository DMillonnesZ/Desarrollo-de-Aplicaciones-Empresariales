from django.contrib import admin
from .models import Dueno, Raza, Veterinario, Mascota, Consulta

admin.site.register([Dueno, Raza, Veterinario, Mascota, Consulta])
