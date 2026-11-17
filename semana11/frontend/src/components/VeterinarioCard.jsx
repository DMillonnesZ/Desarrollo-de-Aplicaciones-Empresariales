import { useState } from "react";

// Muestra UN veterinario. "cupos" tiene valor por defecto 0.
function VeterinarioCard({ nombre, colegiatura, ingreso, cupos = 0, activo }) {
  // Estado propio: cuántos cupos se reservaron desde esta tarjeta.
  const [reservados, setReservados] = useState(0);

  const disponibles = cupos - reservados;

  return (
    <li className="tarjeta">
      <strong>{nombre}</strong> ({colegiatura}) — ingreso: {ingreso}{" "}
      {disponibles === 0 ? (
        <span className="agotado">Sin cupos</span>
      ) : (
        <span>Cupos: {disponibles}</span>
      )}
      {!activo && <span className="inactivo">Inactivo</span>}

      <div className="acciones">
        <button
          className="boton"
          onClick={() => setReservados(reservados + 1)}
          disabled={disponibles === 0 || !activo}
        >
          Reservar cupo
        </button>
        {reservados > 0 && (
          <span className="contador">Reservados: {reservados}</span>
        )}
      </div>
    </li>
  );
}

export default VeterinarioCard;
