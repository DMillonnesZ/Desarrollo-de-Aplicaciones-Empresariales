import { useState } from "react";

// Formulario de alta Y de edición (campos controlados).
// NO valida en el navegador: envía los datos y muestra los mensajes 400 del serializer.
// El padre le pone key={...}: al cambiar de "nuevo" a "editar" el formulario se vuelve a crear
// con los datos del registro seleccionado.
function VeterinarioForm({ seleccionado, especialidades, errores, onGuardar, onCancelar }) {
  const [nombre, setNombre] = useState(seleccionado?.nombre ?? "");
  const [colegiatura, setColegiatura] = useState(seleccionado?.colegiatura ?? "");
  const [ingreso, setIngreso] = useState(seleccionado?.fecha_ingreso ?? "");
  const [cupos, setCupos] = useState(seleccionado?.cupos_disponibles ?? "");
  const [especialidad, setEspecialidad] = useState(
    seleccionado?.especialidades[0] ?? ""
  );
  const [activo, setActivo] = useState(seleccionado?.activo ?? true);

  const manejarEnvio = async (e) => {
    e.preventDefault();

    const guardado = await onGuardar({
      nombre,
      colegiatura,
      fecha_ingreso: ingreso,
      cupos_disponibles: cupos === "" ? undefined : Number(cupos),
      especialidades: especialidad === "" ? [] : [Number(especialidad)],
      activo,
    });

    // Solo se vacían los campos si la API aceptó el registro (201 o 200).
    if (guardado && !seleccionado) {
      setNombre("");
      setColegiatura("");
      setIngreso("");
      setCupos("");
      setEspecialidad("");
      setActivo(true);
    }
  };

  return (
    <form className="formulario" onSubmit={manejarEnvio}>
      <h4>{seleccionado ? `Editar a ${seleccionado.nombre}` : "Nuevo veterinario"}</h4>

      <input
        type="text"
        placeholder="Nombre"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
      />
      <input
        type="text"
        placeholder="Colegiatura (ej. CMVP-45678)"
        value={colegiatura}
        onChange={(e) => setColegiatura(e.target.value)}
      />
      <input
        type="date"
        value={ingreso}
        onChange={(e) => setIngreso(e.target.value)}
      />
      <input
        type="number"
        placeholder="Cupos disponibles (0 a 20)"
        value={cupos}
        onChange={(e) => setCupos(e.target.value)}
      />
      <select
        className="selector campo-select"
        value={especialidad}
        onChange={(e) => setEspecialidad(e.target.value)}
      >
        <option value="">— Especialidad —</option>
        {especialidades.map((esp) => (
          <option key={esp.id} value={esp.id}>
            {esp.nombre}
          </option>
        ))}
      </select>
      <label className="campo-check">
        <input
          type="checkbox"
          checked={activo}
          onChange={(e) => setActivo(e.target.checked)}
        />
        Activo
      </label>

      <div className="acciones">
        <button className="boton" type="submit">
          {seleccionado ? "Guardar cambios" : "Agregar veterinario"}
        </button>
        {seleccionado && (
          <button className="boton boton-gris" type="button" onClick={onCancelar}>
            Cancelar
          </button>
        )}
      </div>

      {/* Ejercicio 11: errores 400 de la API, junto al formulario */}
      {errores.map((texto) => (
        <p key={texto} className="error">
          {texto}
        </p>
      ))}
    </form>
  );
}

export default VeterinarioForm;
