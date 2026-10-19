
const medicamentos = [
  { id: 1, uuid: "m1", nombre: "Amoxicilina 500mg", descripcion: "Antibiótico", stock: 50, precio_unitario: "12.50" },
  { id: 2, uuid: "m2", nombre: "Ivermectina", descripcion: "Antiparasitario", stock: 30, precio_unitario: "8.90" },
  { id: 3, uuid: "m3", nombre: "Meloxicam", descripcion: "Antiinflamatorio", stock: 40, precio_unitario: "15.00" },
  { id: 4, uuid: "m4", nombre: "Prednisolona 5mg", descripcion: "Corticoide", stock: 0, precio_unitario: "9.80" },
  { id: 5, uuid: "m5", nombre: "Omeprazol 20mg", descripcion: "Protector gástrico", stock: 4, precio_unitario: "11.20" },
];

const consultas = [
  {
    uuid: "c1",
    fecha: "2026-10-13T10:30:00Z",
    mascota: "Firulais",
    veterinario: "Ana Torres",
    motivo: "Vómitos",
    estado: "ATENDIDA",
    costo: "60.00",
    detalles_receta: [
      { uuid: "d1", medicamento: "Amoxicilina 500mg", cantidad: 2, precio_unitario: "12.50", dosis: "1 cada 12 horas", indicaciones: "" },
      { uuid: "d2", medicamento: "Ivermectina", cantidad: 2, precio_unitario: "8.90", dosis: "1 cada 12 horas", indicaciones: "" },
    ],
  },
  {
    uuid: "c2",
    fecha: "2026-10-10T16:00:00Z",
    mascota: "Rex",
    veterinario: "Luis Mendoza",
    motivo: "Cojera",
    estado: "ATENDIDA",
    costo: "80.00",
    detalles_receta: [
      { uuid: "d3", medicamento: "Meloxicam", cantidad: 3, precio_unitario: "15.00", dosis: "1 al día", indicaciones: "Con alimento" },
    ],
  },
  {
    uuid: "c3",
    fecha: "2026-10-20T09:00:00Z",
    mascota: "Michi",
    veterinario: "Ana Torres",
    motivo: "Control general",
    estado: "PENDIENTE",
    costo: "40.00",
    detalles_receta: [],
  },
];

const totalReceta = (detalles) =>
  detalles.reduce(
    (acc, d) => acc + d.cantidad * Number(d.precio_unitario),
    0
  );

function App() {
  const nombreApp = "VetCar";
  const igv = 0.18;

  const conIgv = (precio) =>
    (precio * (1 + igv)).toFixed(2);

  return (
    <div>
      <h1>{nombreApp} — Veterinaria</h1>

      <p>
        Amoxicilina 500mg con IGV: S/ {conIgv(12.5)}
      </p>

      <h2>Medicamentos</h2>

      {medicamentos.length === 0 && <p>No hay registros</p>}

      <ul>
        {medicamentos.map((m) => (
          <li key={m.id}>
            {m.nombre} — S/ {Number(m.precio_unitario).toFixed(2)}{" "}

            {m.stock === 0 ? (
              <span>Agotado</span>
            ) : (
              <span>Stock: {m.stock}</span>
            )}

            {m.stock > 0 && m.stock <= 5 && (
              <strong> ¡Últimas unidades!</strong>
            )}
          </li>
        ))}
      </ul>

      <h2>Consultas y recetas</h2>

      {consultas.map((c) => (
        <div key={c.uuid}>
          <h3>
            {c.mascota} — {c.motivo} ({c.estado})
          </h3>

          <p>Veterinario: {c.veterinario}</p>

          {c.detalles_receta.length === 0 ? (
            <p>Sin receta</p>
          ) : (
            <ul>
              {c.detalles_receta.map((d) => (
                <li key={d.uuid}>
                  {d.medicamento} × {d.cantidad} — S/{" "}
                  {(d.cantidad * Number(d.precio_unitario)).toFixed(2)}
                </li>
              ))}
            </ul>
          )}

          <p>
            <strong>
              Total receta: S/ {totalReceta(c.detalles_receta).toFixed(2)}
            </strong>
          </p>
        </div>
      ))}
    </div>
  );
}

export default App;
