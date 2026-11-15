import DetalleItem from "./DetalleItem";

// Relación 1:N: una consulta tiene varios detalles de receta.
// Los nombres de la API (detalles_receta, precio_unitario) se convierten a props
// más simples (detalles, precio).
function ConsultaCard({ mascota, motivo, estado, veterinario, costo, detalles }) {
  const total = detalles.reduce(
    (acc, d) => acc + d.cantidad * Number(d.precio_unitario),
    0
  );

  return (
    <div className="tarjeta">
      <h3>
        {mascota} — {motivo}
      </h3>
      <p>
        Estado:{" "}
        <span className={estado === "ATENDIDA" ? "atendida" : "pendiente"}>
          {estado}
        </span>
      </p>
      <p>Veterinario: {veterinario}</p>
      <p>Costo consulta: S/ {Number(costo).toFixed(2)}</p>

      <h4>Receta médica</h4>
      {detalles.length === 0 ? (
        <p className="vacio">Sin receta</p>
      ) : (
        <ul>
          {detalles.map((d) => (
            <DetalleItem
              key={d.uuid}
              medicamento={d.medicamento}
              cantidad={d.cantidad}
              precio={d.precio_unitario}
            />
          ))}
        </ul>
      )}

      <p className="total">Total receta: S/ {total.toFixed(2)}</p>
    </div>
  );
}

export default ConsultaCard;
