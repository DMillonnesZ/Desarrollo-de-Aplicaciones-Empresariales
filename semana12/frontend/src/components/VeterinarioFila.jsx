// UNA fila del listado. No modifica la lista ni llama a la API: solo avisa al padre.
function VeterinarioFila({
  veterinario,
  nombresEspecialidad,
  onEditar,
  onEliminar,
  onCambiarEstado,
}) {
  const { id, nombre, colegiatura, fecha_ingreso, cupos_disponibles, activo } =
    veterinario;

  const especialidades = veterinario.especialidades
    .map((idEsp) => nombresEspecialidad[idEsp])
    .filter(Boolean)
    .join(", ");

  // Ejercicio 12: confirmación previa antes de avisar al padre.
  const confirmarEliminar = () => {
    if (window.confirm(`¿Eliminar a ${nombre}? Esta acción no se puede deshacer.`)) {
      onEliminar(id);
    }
  };

  return (
    <li className="tarjeta fila-panel">
      <div>
        <strong>{nombre}</strong> ({colegiatura}) — ingreso: {fecha_ingreso}
        <div>
          {especialidades && <span>{especialidades} · </span>}
          {cupos_disponibles === 0 ? (
            <span className="agotado">Sin cupos</span>
          ) : (
            <span>Cupos: {cupos_disponibles}</span>
          )}
          {!activo && <span className="inactivo">Inactivo</span>}
        </div>
      </div>

      <div className="acciones">
        <button className="boton" onClick={() => onEditar(veterinario)}>
          Editar
        </button>
        <button className="boton" onClick={() => onCambiarEstado(veterinario)}>
          {activo ? "Desactivar" : "Activar"}
        </button>
        <button className="boton boton-peligro" onClick={confirmarEliminar}>
          Eliminar
        </button>
      </div>
    </li>
  );
}

export default VeterinarioFila;
