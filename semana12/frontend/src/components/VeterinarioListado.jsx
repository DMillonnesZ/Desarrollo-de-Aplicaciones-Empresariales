import VeterinarioFila from "./VeterinarioFila";

// Recibe los registros que llegaron de la API y dibuja una fila por cada uno.
function VeterinarioListado({
  veterinarios,
  nombresEspecialidad,
  onEditar,
  onEliminar,
  onCambiarEstado,
}) {
  // Estado "lista vacía"
  if (veterinarios.length === 0) {
    return <p className="vacio">No hay veterinarios que coincidan con la búsqueda.</p>;
  }

  return (
    <ul className="lista-filas">
      {veterinarios.map((v) => (
        <VeterinarioFila
          key={v.id}
          veterinario={v}
          nombresEspecialidad={nombresEspecialidad}
          onEditar={onEditar}
          onEliminar={onEliminar}
          onCambiarEstado={onCambiarEstado}
        />
      ))}
    </ul>
  );
}

export default VeterinarioListado;
