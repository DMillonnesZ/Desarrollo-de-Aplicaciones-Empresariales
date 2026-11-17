import { useEffect } from "react";

// Hermano de Catalogo. Lee el mismo estado que modifica Practica.
export default function Carrito({ lineas, onQuitar, onVaciar }) {
  // Ejercicio 5: datos derivados, recalculados en cada render, sin useState.
  const cantidad = lineas.reduce((suma, linea) => suma + linea.cantidad, 0);
  const total = lineas.reduce(
    (suma, linea) => suma + Number(linea.precio) * linea.cantidad,
    0,
  );

  // Ejercicio 8: se ejecuta al montar y cuando cambia la cantidad de unidades.
  useEffect(() => {
    const tituloAnterior = document.title;
    document.title = `Carrito (${cantidad}) — Cafetería`;
    console.log(`Efecto Carrito: ${cantidad} unidades`);

    // Restaura el título al limpiar el efecto, también al salir de la práctica.
    return () => {
      document.title = tituloAnterior;
    };
  }, [cantidad]);

  return (
    <aside className="practica-carrito" aria-labelledby="carrito-titulo">
      <div className="practica-seccion-cabecera">
        <h2 id="carrito-titulo">Tu carrito</h2>
        <span className="practica-unidades">{cantidad} unidades</span>
      </div>

      {/* Ejercicio 6: render condicional con &&. */}
      {lineas.length === 0 && (
        <p className="practica-vacio">El carrito está vacío</p>
      )}

      <ul className="practica-lineas">
        {lineas.map((linea) => (
          <li className="practica-linea" key={linea.id}>
            <div>
              <h3>{linea.nombre}</h3>
              <p>{linea.cantidad} × S/ {Number(linea.precio).toFixed(2)}</p>
              <button
                className="practica-quitar"
                type="button"
                onClick={() => onQuitar(linea.id)}
                aria-label={`Quitar ${linea.nombre}`}
              >
                Quitar
              </button>
            </div>
            <strong>S/ {(Number(linea.precio) * linea.cantidad).toFixed(2)}</strong>
          </li>
        ))}
      </ul>

      <div className="practica-total" aria-live="polite">
        <span>Total</span>
        <strong>S/ {total.toFixed(2)}</strong>
      </div>
      <button
        className="practica-boton practica-boton-secundario"
        type="button"
        onClick={onVaciar}
        disabled={lineas.length === 0}
      >
        Vaciar carrito
      </button>
      <p className="practica-nota">Quitar elimina la línea completa del carrito.</p>
    </aside>
  );
}
