// Campo controlado: el texto vive en Practica, no en este componente.
export default function Buscador({ valor, onCambiar }) {
  return (
    <div className="practica-buscador">
      <label htmlFor="buscar-producto">Buscar producto</label>
      <input
        id="buscar-producto"
        type="search"
        placeholder="Escribe un nombre, por ejemplo: ca"
        value={valor}
        onChange={(evento) => onCambiar(evento.target.value)}
      />
    </div>
  );
}
