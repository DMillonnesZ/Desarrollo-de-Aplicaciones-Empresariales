// Filtros controlados: el texto y el estado viven en el padre (PanelVeterinarios).
function BuscadorVeterinarios({ buscar, estado, onBuscar, onEstado }) {
  return (
    <div className="filtros">
      <input
        className="buscador"
        type="text"
        placeholder="Buscar por nombre o colegiatura..."
        value={buscar}
        onChange={(e) => onBuscar(e.target.value)}
      />
      <select
        className="selector"
        value={estado}
        onChange={(e) => onEstado(e.target.value)}
      >
        <option value="todos">Todos</option>
        <option value="activos">Solo activos</option>
        <option value="inactivos">Solo inactivos</option>
      </select>
    </div>
  );
}

export default BuscadorVeterinarios;
