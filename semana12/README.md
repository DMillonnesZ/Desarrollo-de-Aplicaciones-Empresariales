## Frontend (React + Vite)

Interfaz de React del proyecto VetCar.

cd frontend
npm install
npm run dev   # http://localhost:5173/

Muestra: medicamentos y consultas con sus recetas (Parte 1) y veterinarios y mascotas con sus seguimientos clínicos (Parte 2).

### Semana 11 — Comunicación entre componentes

- `src/practica/`: mini catálogo con carrito (props, funciones por props, estado elevado, estado derivado, buscador compartido y `useEffect`).
- Panel de veterinarios (`src/components/PanelVeterinarios.jsx`): el padre guarda el estado y reparte los datos por props a `BuscadorVeterinarios`, `VeterinarioListado` (con `VeterinarioFila`), `VeterinarioForm` y `ResumenVeterinarios`. Los hijos avisan con `onEliminar`, `onCambiarEstado`, `onGuardar`, `onBuscar` y `onEstado`. Incluye un `useEffect` para el título de la pestaña y un aviso temporal con limpieza.

### Semana 12 — React consume la API de Django (Ajax)

El panel de veterinarios y la práctica de medicamentos ya no usan datos escritos a mano: piden los datos a la API REST de la Semana 8 con Axios.

**Cómo ejecutar Django y React a la vez (dos terminales)**

```
# Terminal 1 - Django (puerto 8000)
pip install -r requirements.txt
cd src
python manage.py migrate
python manage.py runserver

# Terminal 2 - React (puerto 5173)
cd frontend
npm install
npm install axios
npm run dev
```

Abrir http://localhost:5173/

**Configuración de CORS (`src/config/settings.py`)**

- `corsheaders` en `INSTALLED_APPS`.
- `corsheaders.middleware.CorsMiddleware` en la parte alta de `MIDDLEWARE`.
- `CORS_ALLOWED_ORIGINS = ['http://localhost:5173', 'http://127.0.0.1:5173']`.

**Endpoints que usa el panel (base `http://127.0.0.1:8000/api`)**

| Operación | Método | URL | Código |
|---|---|---|---|
| Listar / buscar / filtrar | GET | `/veterinarios/?search=ana&activo=true` | 200 |
| Crear | POST | `/veterinarios/` | 201 (400 si no valida) |
| Editar | PATCH | `/veterinarios/<id>/` | 200 |
| Eliminar | DELETE | `/veterinarios/<id>/` | 204 (404 si no existe, 409 si tiene atenciones) |
| Especialidades del formulario | GET | `/especialidades/` | 200 |
| Práctica: medicamentos | GET, POST, PATCH, DELETE | `/medicamentos/` | 200, 201, 200, 204 |

La API todavía no tiene autenticación ni permisos: cualquier persona puede listar, crear, modificar y eliminar registros.
