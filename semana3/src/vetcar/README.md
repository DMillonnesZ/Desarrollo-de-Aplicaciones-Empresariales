## Laboratorio 03 — VetCar (Django ORM + SQLite)

### Problemática

Las veterinarias pequeñas registran manualmente las consultas, tratamientos y datos de mascotas
de sus clientes (en cuadernos o mensajes de WhatsApp), lo que genera pérdida de historiales
médicos, dificultad para dar seguimiento a tratamientos en curso y demoras al informar a los
dueños sobre el estado de salud de sus mascotas. Usuarios: el veterinario y los dueños de mascotas.

### Requisitos funcionales

1. Registrar dueños de mascotas.
2. Registrar razas de animales.
3. Registrar veterinarios y su especialidad.
4. Registrar mascotas, asociadas a un dueño y una raza.
5. Listar las mascotas registradas.
6. Agendar una consulta veterinaria para una mascota.
7. Consultar el historial de consultas de una mascota.
8. Actualizar el estado de una consulta.
9. Actualizar los datos de una mascota.
10. Eliminar un registro de mascota, dueño o consulta.

### App creada: `vetcar`

Modelos:

- **Dueno**, **Raza**, **Veterinario** (entidades independientes)
- **Mascota** (ForeignKey → Dueno, ForeignKey → Raza)
- **Consulta** (ForeignKey → Mascota, ForeignKey → Veterinario)

CRUD completo con ModelForms y QuerySets (`all`, `filter`, `order_by`), persistencia en SQLite
mediante Django ORM y migraciones.

### Rutas

| Ruta                               | Función                               |
| ---------------------------------- | ------------------------------------- |
| `/vetcar/`                         | Inicio                                |
| `/vetcar/<entidad>/`               | Listado (READ)                        |
| `/vetcar/<entidad>/nuevo/`         | Crear (CREATE)                        |
| `/vetcar/<entidad>/<id>/editar/`   | Editar (UPDATE)                       |
| `/vetcar/<entidad>/<id>/eliminar/` | Eliminar con confirmación (DELETE)    |
| `/vetcar/mascotas/<id>/historial/` | Historial de consultas de una mascota |

`<entidad>` = `duenos` | `razas` | `veterinarios` | `mascotas` | `consultas`

### Ejecución

![alt text](./screenshots/image.png)
