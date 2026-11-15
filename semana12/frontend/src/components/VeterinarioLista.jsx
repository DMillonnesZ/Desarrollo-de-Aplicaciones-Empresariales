import { useState } from "react";
import VeterinarioCard from "./VeterinarioCard";
import { veterinarios as veterinariosIniciales } from "../datos";

function VeterinarioLista() {
  const [veterinarios, setVeterinarios] = useState(veterinariosIniciales);
  const [busqueda, setBusqueda] = useState("");

  const [nombre, setNombre] = useState("");
  const [colegiatura, setColegiatura] = useState("");
  const [cupos, setCupos] = useState("");
  const [error, setError] = useState("");

  const filtrados = veterinarios.filter((v) =>
    v.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  const manejarEnvio = (e) => {
    e.preventDefault();

    if (nombre.trim() === "" || colegiatura.trim() === "") {
      setError("El nombre y la colegiatura son obligatorios.");
      return;
    }
    // Regla tomada de la API de la Semana 8: validate_cupos_disponibles
    if (cupos === "" || Number(cupos) < 0 || Number(cupos) > 20) {
      setError("Los cupos disponibles deben estar entre 0 y 20.");
      return;
    }

    const nuevo = {
      id: Math.max(0, ...veterinarios.map((v) => v.id)) + 1,
      uuid: `v${Date.now()}`,
      nombre: nombre.trim(),
      telefono: "",
      correo: "",
      activo: true,
      colegiatura: colegiatura.trim(),
      especialidades: [],
      fecha_ingreso: new Date().toISOString().slice(0, 10),
      cupos_disponibles: Number(cupos),
    };

    setVeterinarios([...veterinarios, nuevo]);
    setNombre("");
    setColegiatura("");
    setCupos("");
    setError("");
  };

  return (
    <div>
      <input
        className="buscador"
        type="text"
        placeholder="Buscar veterinario..."
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
      />

      {filtrados.length === 0 && (
        <p className="vacio">No hay veterinarios que coincidan con la búsqueda.</p>
      )}

      <ul className="lista">
        {filtrados.map((v) => (
          <VeterinarioCard
            key={v.id}
            nombre={v.nombre}
            colegiatura={v.colegiatura}
            ingreso={v.fecha_ingreso}
            cupos={v.cupos_disponibles}
            activo={v.activo}
          />
        ))}
      </ul>

      <form className="formulario" onSubmit={manejarEnvio}>
        <h4>Nuevo veterinario</h4>
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
          type="number"
          placeholder="Cupos disponibles (0 a 20)"
          value={cupos}
          onChange={(e) => setCupos(e.target.value)}
        />
        <button className="boton" type="submit">
          Agregar veterinario
        </button>
        {error && <p className="error">{error}</p>}
      </form>
    </div>
  );
}

export default VeterinarioLista;
