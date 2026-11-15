// Ejercicio 7: campo controlado. El texto NO se guarda aquí: vive en Practica.
function Buscador({ valor, onCambiar }) {
  return (
    <input
      className="buscador"
      type="text"
      placeholder="Buscar producto..."
      value={valor}
      onChange={(e) => onCambiar(e.target.value)}
    />
  );
}

export default Buscador;
