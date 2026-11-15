// Ejercicio 1: recibe UN producto por props y lo dibuja.
// Ejercicio 3: avisa al padre con la función onAgregar recibida por props.
function ProductoCard({ producto, onAgregar }) {
  const agotado = producto.stock === 0;

  return (
    <li className="tarjeta">
      <strong>{producto.nombre}</strong>
      <p>Precio: S/ {Number(producto.precio).toFixed(2)}</p>

      {agotado ? (
        <span className="agotado">Agotado</span>
      ) : (
        <span>Stock: {producto.stock}</span>
      )}

      <div className="acciones">
        {/* Se pasa una función (no su resultado): () => onAgregar(producto) */}
        <button
          className="boton"
          disabled={agotado}
          onClick={() => onAgregar(producto)}
        >
          Agregar
        </button>
      </div>
    </li>
  );
}

export default ProductoCard;
