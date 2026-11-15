import { useEffect } from "react";

// Ejercicios 4, 5, 6 y 8: hermano de Catalogo. Solo recibe líneas y funciones por props.
function Carrito({ lineas, onQuitar, onVaciar }) {
  // Ejercicio 5: datos derivados. No necesitan useState: se recalculan en cada render.
  const total = lineas.reduce(
    (suma, l) => suma + Number(l.precio) * l.cantidad,
    0
  );
  const unidades = lineas.reduce((suma, l) => suma + l.cantidad, 0);

  // Ejercicio 8: ciclo de vida. Se ejecuta al montar y cada vez que cambia "unidades".
  useEffect(() => {
    console.log("Efecto del carrito: unidades =", unidades);
    document.title = `Carrito (${unidades}) — Cafetería`;
  }, [unidades]);

  return (
    <section className="tarjeta-contenedor">
      <h3 className="tarjeta-titulo">Carrito</h3>

      {lineas.length === 0 && <p className="vacio">El carrito está vacío</p>}

      <ul className="lista-carrito">
        {lineas.map((l) => (
          <li key={l.id} className="linea-carrito">
            <span>
              {l.nombre} x{l.cantidad} — S/{" "}
              {(Number(l.precio) * l.cantidad).toFixed(2)}
            </span>
            <button className="boton boton-peligro" onClick={() => onQuitar(l.id)}>
              Quitar
            </button>
          </li>
        ))}
      </ul>

      <p className="total">
        Total: S/ {total.toFixed(2)} ({unidades} unidades)
      </p>

      <button
        className="boton"
        onClick={onVaciar}
        disabled={lineas.length === 0}
      >
        Vaciar carrito
      </button>
    </section>
  );
}

export default Carrito;
