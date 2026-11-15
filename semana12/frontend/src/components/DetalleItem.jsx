// Un renglón de la receta (elemento anidado de la relación 1:N).
function DetalleItem({ medicamento, cantidad, precio }) {
  const subtotal = cantidad * Number(precio);

  return (
    <li>
      {medicamento} × {cantidad} — S/ {subtotal.toFixed(2)}
    </li>
  );
}

export default DetalleItem;
