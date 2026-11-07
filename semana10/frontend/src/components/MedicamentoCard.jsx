import { useState } from "react";

// Muestra UN medicamento. Los datos llegan por props desestructuradas.
// "descripcion" tiene un valor por defecto.
function MedicamentoCard({ nombre, descripcion = "Sin descripción", precio, stock }) {
  // Estado propio: cada tarjeta tiene su contador de unidades agregadas.
  const [agregados, setAgregados] = useState(0);

  // Se desactiva si no hay stock o si ya se agregó todo el stock disponible.
  const sinStock = stock === 0 || agregados >= stock;

  const agregar = () => setAgregados(agregados + 1);

  return (
    <li className="tarjeta">
      <strong>{nombre}</strong>
      <p>{descripcion}</p>
      <p>Precio: S/ {Number(precio).toFixed(2)}</p>

      {stock === 0 ? (
        <span className="agotado">Agotado</span>
      ) : (
        <span>Stock: {stock}</span>
      )}

      {stock > 0 && stock <= 5 && (
        <span className="ultimas">¡Últimas unidades!</span>
      )}

      <div className="acciones">
        <button className="boton" onClick={agregar} disabled={sinStock}>
          Agregar
        </button>
        {agregados > 0 && <span className="contador">Agregados: {agregados}</span>}
      </div>
    </li>
  );
}

export default MedicamentoCard;
