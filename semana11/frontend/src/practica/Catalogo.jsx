import ProductoCard from "./ProductoCard";

// Practica entrega el arreglo ya filtrado; Catalogo lo distribuye a sus hijos.
export default function Catalogo({ productos, onAgregar }) {
  return (
    <section className="practica-catalogo" aria-labelledby="catalogo-titulo">
      <div className="practica-seccion-cabecera">
        <h2 id="catalogo-titulo">Catálogo</h2>
        <span>{productos.length} productos</span>
      </div>
      {productos.length === 0 && (
        <p className="practica-vacio" role="status">
          No hay productos que coincidan
        </p>
      )}
      <ul className="practica-productos">
        {productos.map((producto) => (
          <ProductoCard
            key={producto.id}
            producto={producto}
            onAgregar={onAgregar}
          />
        ))}
      </ul>
    </section>
  );
}
