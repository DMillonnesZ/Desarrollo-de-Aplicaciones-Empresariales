import ProductoCard from "./ProductoCard";

// Ejercicio 1: recibe el arreglo de productos y entrega cada uno a ProductoCard.
// Ejercicio 7: muestra un mensaje cuando el filtro no deja ningún producto.
function Catalogo({ productos, onAgregar }) {
  return (
    <div>
      {productos.length === 0 && (
        <p className="vacio">No hay productos que coincidan</p>
      )}

      <ul className="lista">
        {productos.map((p) => (
          <ProductoCard key={p.id} producto={p} onAgregar={onAgregar} />
        ))}
      </ul>
    </div>
  );
}

export default Catalogo;
