import { useState } from "react";
import SeguimientoItem from "./SeguimientoItem";

// Relación anidada: una mascota tiene varios seguimientos clínicos.
function MascotaCard({ nombre, raza, especie, dueno, peso, seguimientos }) {
  // Estado propio: marcar la mascota como favorita.
  const [favorita, setFavorita] = useState(false);

  const activos = seguimientos.filter((s) => s.activo).length;

  return (
    <div className="tarjeta">
      <h4 style={{ margin: 0 }}>
        {favorita && "★ "}
        {nombre} — {raza} ({especie})
      </h4>
      <p>
        Dueño: {dueno} | Peso: {Number(peso).toFixed(2)} kg
      </p>

      {seguimientos.length === 0 ? (
        <p className="vacio">Sin seguimientos</p>
      ) : (
        <ul>
          {seguimientos.map((s) => (
            <SeguimientoItem
              key={s.uuid}
              veterinario={s.veterinario}
              rol={s.rol}
              desde={s.fecha_asignacion}
              activo={s.activo}
            />
          ))}
        </ul>
      )}

      <p>
        <strong>Seguimientos activos: {activos}</strong>
      </p>

      <button className="boton" onClick={() => setFavorita(!favorita)}>
        {favorita ? "Quitar de favoritas" : "Marcar como favorita"}
      </button>
    </div>
  );
}

export default MascotaCard;
