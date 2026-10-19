function App() {
  const nombreApp = "VetCar";
  const igv = 0.18;
  const conIgv = (precio) => (precio * (1 + igv)).toFixed(2);

  return (
    <div>
      <h1>{nombreApp} — Veterinaria</h1>
      <p>Amoxicilina 500mg con IGV: S/ {conIgv(12.5)}</p>
    </div>
  );
}

export default App;