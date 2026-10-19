const medicamentos = [
  { id: 1, uuid: "m1", nombre: "Amoxicilina 500mg", descripcion: "Antibiótico", stock: 50, precio_unitario: "12.50" },
  { id: 2, uuid: "m2", nombre: "Ivermectina", descripcion: "Antiparasitario", stock: 30, precio_unitario: "8.90" },
  { id: 3, uuid: "m3", nombre: "Meloxicam", descripcion: "Antiinflamatorio", stock: 40, precio_unitario: "15.00" },
  { id: 4, uuid: "m4", nombre: "Prednisolona 5mg", descripcion: "Corticoide", stock: 0, precio_unitario: "9.80" },
  { id: 5, uuid: "m5", nombre: "Omeprazol 20mg", descripcion: "Protector gástrico", stock: 4, precio_unitario: "11.20" },
];
function App() {
  const nombreApp = "VetCar";
  const igv = 0.18;
  const conIgv = (precio) => (precio * (1 + igv)).toFixed(2);

  return (
    <div>
      <h1>{nombreApp} — Veterinaria</h1>
      <p>Amoxicilina 500mg con IGV: S/ {conIgv(12.5)}</p>
      <h2>Medicamentos</h2>
<ul>
  {medicamentos.map((m) => (
    <li key={m.id}>
      {m.nombre} — S/ {Number(m.precio_unitario).toFixed(2)}
    </li>
  ))}
</ul>
    </div>
  );
}

export default App;