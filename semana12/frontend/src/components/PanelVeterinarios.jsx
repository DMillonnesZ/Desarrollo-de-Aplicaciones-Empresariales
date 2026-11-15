import { useCallback, useEffect, useState } from "react";
import api from "../api";
import { adaptarVeterinario, mensajesDeError } from "../adaptadores";
import BuscadorVeterinarios from "./BuscadorVeterinarios";
import VeterinarioListado from "./VeterinarioListado";
import VeterinarioForm from "./VeterinarioForm";
import ResumenVeterinarios from "./ResumenVeterinarios";
import AvisoPanel from "./AvisoPanel";

// Componente PADRE del panel (Semana 12): guarda los registros que llegan de la API
// y los estados cargando / error. Los hijos solo reciben props y avisan con funciones.
function PanelVeterinarios() {
  const [veterinarios, setVeterinarios] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState("");
  const [recarga, setRecarga] = useState(0); // botón "Reintentar"

  const [buscar, setBuscar] = useState("");
  const [estado, setEstado] = useState("todos");

  const [especialidades, setEspecialidades] = useState([]);
  const [seleccionado, setSeleccionado] = useState(null); // registro que se edita
  const [erroresForm, setErroresForm] = useState([]);
  const [aviso, setAviso] = useState(null);

  const ocultarAviso = useCallback(() => setAviso(null), []);
  const avisar = (tipo, texto) => setAviso({ tipo, texto, momento: Date.now() });

  // Ejercicios 10 y 13: GET del listado. Se vuelve a pedir cuando cambian buscar o estado.
  useEffect(() => {
    const controlador = new AbortController(); // cancela la petición pendiente

    async function cargar() {
      setCargando(true);
      setError("");
      try {
        const params = { search: buscar };
        if (estado !== "todos") params.activo = estado === "activos"; // ?activo=true|false

        const respuesta = await api.get("/veterinarios/", {
          params,
          signal: controlador.signal,
        });
        setVeterinarios(respuesta.data.map(adaptarVeterinario));
      } catch (err) {
        if (err.code === "ERR_CANCELED") return; // la petición se canceló a propósito
        console.error("No se pudo cargar la lista de veterinarios:", err);
        setError("No se pudo cargar la lista de veterinarios.");
      } finally {
        if (!controlador.signal.aborted) setCargando(false);
      }
    }

    cargar();
    return () => controlador.abort();
  }, [buscar, estado, recarga]);

  // Especialidades para el <select> del formulario (una sola vez).
  useEffect(() => {
    async function cargarEspecialidades() {
      try {
        const respuesta = await api.get("/especialidades/");
        setEspecialidades(respuesta.data);
      } catch (err) {
        console.error("No se pudieron cargar las especialidades:", err);
      }
    }
    cargarEspecialidades();
  }, []);

  // Título de la pestaña con la cantidad de registros.
  useEffect(() => {
    document.title = `Veterinarios (${veterinarios.length}) — VetCar`;
  }, [veterinarios.length]);

  // Ejercicio 11: alta (POST, 201) o edición (PATCH, 200). Devuelve true si la API aceptó.
  const guardar = async (datos) => {
    setErroresForm([]);
    try {
      if (seleccionado) {
        const respuesta = await api.patch(`/veterinarios/${seleccionado.id}/`, datos);
        setVeterinarios((actuales) =>
          actuales.map((v) =>
            v.id === seleccionado.id ? adaptarVeterinario(respuesta.data) : v
          )
        );
        setSeleccionado(null);
        avisar("ok", "Veterinario actualizado.");
      } else {
        const respuesta = await api.post("/veterinarios/", datos);
        // Arreglo NUEVO con spread, sin push
        setVeterinarios((actuales) => [...actuales, adaptarVeterinario(respuesta.data)]);
        avisar("ok", `Veterinario agregado: ${respuesta.data.nombre}`);
      }
      return true;
    } catch (err) {
      setErroresForm(mensajesDeError(err)); // 400: mensajes del serializer
      return false;
    }
  };

  // Ejercicio 12: DELETE (204) con filter(); si responde 404 el registro ya no existe.
  const eliminar = async (id) => {
    try {
      await api.delete(`/veterinarios/${id}/`);
      setVeterinarios((actuales) => actuales.filter((v) => v.id !== id));
      if (seleccionado?.id === id) setSeleccionado(null);
      avisar("ok", "Veterinario eliminado.");
    } catch (err) {
      if (err.response?.status === 404) {
        setVeterinarios((actuales) => actuales.filter((v) => v.id !== id));
        avisar("error", "El veterinario ya no existe (404). Se quitó de la lista.");
      } else {
        avisar("error", mensajesDeError(err)[0]); // por ejemplo 409: tiene atenciones
      }
    }
  };

  // Activar / desactivar: PATCH y map().
  const cambiarEstado = async (veterinario) => {
    try {
      const respuesta = await api.patch(`/veterinarios/${veterinario.id}/`, {
        activo: !veterinario.activo,
      });
      setVeterinarios((actuales) =>
        actuales.map((v) =>
          v.id === veterinario.id ? adaptarVeterinario(respuesta.data) : v
        )
      );
    } catch (err) {
      avisar("error", mensajesDeError(err)[0]);
    }
  };

  const editar = (veterinario) => {
    setErroresForm([]);
    setSeleccionado(veterinario);
  };

  const cancelarEdicion = () => {
    setErroresForm([]);
    setSeleccionado(null);
  };

  // id de especialidad -> nombre, para mostrarlo en cada fila
  const nombresEspecialidad = Object.fromEntries(
    especialidades.map((esp) => [esp.id, esp.nombre])
  );

  return (
    <div>
      {aviso && <AvisoPanel aviso={aviso} onTerminar={ocultarAviso} />}

      <BuscadorVeterinarios
        buscar={buscar}
        estado={estado}
        onBuscar={setBuscar}
        onEstado={setEstado}
      />

      <div className="dos-columnas">
        <div>
          {/* Ejercicio 10: tres estados — cargando, error y lista (con mensaje si está vacía) */}
          {cargando && <p className="cargando">Cargando...</p>}

          {error && !cargando && (
            <div>
              <p className="error">{error}</p>
              <button className="boton" onClick={() => setRecarga(recarga + 1)}>
                Reintentar
              </button>
            </div>
          )}

          {!cargando && !error && (
            <VeterinarioListado
              veterinarios={veterinarios}
              nombresEspecialidad={nombresEspecialidad}
              onEditar={editar}
              onEliminar={eliminar}
              onCambiarEstado={cambiarEstado}
            />
          )}

          <VeterinarioForm
            key={seleccionado ? seleccionado.id : "nuevo"}
            seleccionado={seleccionado}
            especialidades={especialidades}
            errores={erroresForm}
            onGuardar={guardar}
            onCancelar={cancelarEdicion}
          />
        </div>

        {/* Ejercicio 13: el resumen se calcula con los datos recibidos de la API */}
        <ResumenVeterinarios veterinarios={veterinarios} />
      </div>
    </div>
  );
}

export default PanelVeterinarios;
