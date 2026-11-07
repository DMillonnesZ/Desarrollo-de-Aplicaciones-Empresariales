import { useState } from "react";
import MascotaCard from "./MascotaCard";
import { mascotas } from "../datos";

function MascotaLista() {
  const [busqueda, setBusqueda] = useState("");

  const filtradas = mascotas.filter((m) =>
    m.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  return (
    <div>
      <input
        className="buscador"
        type="text"
        placeholder="Buscar mascota..."
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
      />

      {filtradas.length === 0 && (
        <p className="vacio">No hay mascotas que coincidan con la búsqueda.</p>
      )}

      {filtradas.map((m) => (
        <MascotaCard
          key={m.uuid}
          nombre={m.nombre}
          raza={m.raza}
          especie={m.especie}
          dueno={m.dueno}
          peso={m.peso_kg}
          seguimientos={m.seguimientos}
        />
      ))}
    </div>
  );
}

export default MascotaLista;
