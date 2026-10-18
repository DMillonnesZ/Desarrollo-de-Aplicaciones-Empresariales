## Semana 7 — ORM avanzado

### Transacciones con `transaction.atomic()` y `F()`
- **Registrar receta** (`/vetcar/consultas/<uuid>/receta/registrar/`): crea el `DetalleReceta`, descuenta `Medicamento.stock` con `F()` y suma al `costo` de la `Consulta`. Si no hay stock suficiente se cancela todo (rollback). Patrón Post/Redirect/Get.
- **Agendar consulta** (`/vetcar/consultas/agendar/`): crea la `Consulta` (la señal registra su `AuditoriaAtencion`) y descuenta un cupo de `Veterinario.cupos_disponibles` con `F()`. Sin cupos, se revierte todo, incluida la auditoría.

### Reportes (`/vetcar/reporte/`)
- `aggregate()`: total de unidades y valor recetado (`DetalleReceta`), total y promedio de cupos (`Veterinario`).
- `annotate()` con `Count`: atenciones por mascota y consultas por veterinario.
- `values().annotate()`: consultas e ingresos agrupados por estado y por veterinario.

### QuerySets personalizados (`as_manager()`)
- `Consulta`: `pendientes()`, `atendidas()`, `del_mes_actual()`, usados en `listar_consultas` y en `reporte`.
- `Veterinario`: `activos()`, `con_cupos()`, usados en `listar_veterinarios` y en `AgendarConsultaForm`.

### Optimización del problema N+1
- Listado de **Dueños**: `prefetch_related('mascotas')` (1+N consultas → 2).
- Listado de **Razas**: `select_related('especie')` + `prefetch_related('mascotas')` (1+N consultas → 2).