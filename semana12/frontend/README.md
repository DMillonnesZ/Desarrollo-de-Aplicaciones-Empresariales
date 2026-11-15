# VetCar — Frontend (React + Vite)

Interfaz de la Semana 10 (Componentes y eventos). Usa datos escritos a mano con la forma de la API REST de la Semana 8 (`src/datos.js`); todavía no consume la API.

## Componentes (`src/components`)

| Componente | Qué hace |
| --- | --- |
| `Tarjeta` | Contenedor reutilizable: recibe `titulo` y `children`. |
| `MedicamentoCard` | Muestra un medicamento (props `nombre`, `descripcion` con valor por defecto, `precio`, `stock`). Botón **Agregar** con contador propio (`useState`). |
| `MedicamentoLista` | Lista con `map()` y `key`, buscador controlado y formulario controlado (`onSubmit`, valida precio > 0). |
| `ConsultaLista` / `ConsultaCard` | Lista de consultas; la tarjeta muestra la receta (relación 1:N) y el total calculado. |
| `DetalleItem` | Un renglón de la receta dentro de `ConsultaCard`. |
| `VeterinarioCard` | Muestra un veterinario; botón **Reservar cupo** con estado. |
| `VeterinarioLista` | Lista, buscador y formulario controlado (valida cupos entre 0 y 20, regla de la API). |
| `MascotaLista` / `MascotaCard` | Lista de mascotas con buscador; botón de favorita con estado. |
| `SeguimientoItem` | Seguimiento clínico dentro de `MascotaCard` (modelo intermedio). |

## Cómo ejecutar

```bash
cd frontend
npm install
npm run dev
```

Abrir http://localhost:5173/

Otros comandos: `npm run lint` y `npm run build`.
