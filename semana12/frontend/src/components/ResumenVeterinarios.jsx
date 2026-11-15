// Hermano del listado. Todo se CALCULA con los datos que recibe: no usa useState.
function ResumenVeterinarios({ veterinarios }) {
  const total = veterinarios.length;
  const activos = veterinarios.filter((v) => v.activo).length;
  const inactivos = total - activos;
  const cuposTotales = veterinarios.reduce((suma, v) => suma + v.cupos_disponibles, 0);
  const promedio = total === 0 ? 0 : cuposTotales / total;

  return (
    <section className="resumen">
      <h3 className="tarjeta-titulo">Resumen</h3>
      <p>Total de veterinarios: <strong>{total}</strong></p>
      <p>Activos: <strong>{activos}</strong> · Inactivos: <strong>{inactivos}</strong></p>
      <p>Cupos totales: <strong>{cuposTotales}</strong></p>
      <p>Promedio de cupos: <strong>{promedio.toFixed(1)}</strong></p>
    </section>
  );
}

export default ResumenVeterinarios;
