// Recibe un objeto y una función. La tarjeta no modifica el producto:
// comunica la acción al padre mediante onAgregar(producto).
export default function ProductoCard({ producto, onAgregar }) {
  const agotado = producto.stock === 0;

  return (
    <li className="practica-producto">
      <div className="practica-producto-cabecera">
        <span className="practica-producto-numero">
          {String(producto.id).padStart(2, "0")}
        </span>
        <span className={`practica-stock${agotado ? " practica-stock-agotado" : ""}`}>
          {agotado ? "Agotado" : `Stock: ${producto.stock}`}
        </span>
      </div>
      <h3>{producto.nombre}</h3>
      <p className="practica-precio">S/ {Number(producto.precio).toFixed(2)}</p>
      {/* La función flecha espera al clic antes de llamar a onAgregar. */}
      <button
        className="practica-boton"
        type="button"
        disabled={agotado}
        onClick={() => onAgregar(producto)}
        aria-label={`Agregar ${producto.nombre}`}
      >
        Agregar
      </button>
    </li>
  );
}
