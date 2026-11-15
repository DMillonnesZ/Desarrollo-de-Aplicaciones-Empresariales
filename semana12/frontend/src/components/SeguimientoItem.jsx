// Elemento anidado: un seguimiento clínico de una mascota (modelo intermedio).
function SeguimientoItem({ veterinario, rol, desde, activo }) {
  return (
    <li>
      {veterinario} — {rol} (desde {desde}) · {activo ? "activo" : "inactivo"}
    </li>
  );
}

export default SeguimientoItem;
