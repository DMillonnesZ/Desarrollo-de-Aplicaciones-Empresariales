import "./App.css";
import Tarjeta from "./components/Tarjeta";
import MedicamentoLista from "./components/MedicamentoLista";
import ConsultaLista from "./components/ConsultaLista";
import VeterinarioLista from "./components/VeterinarioLista";
import MascotaLista from "./components/MascotaLista";

function App() {
  const nombreApp = "VetCar";

  return (
    <div className="contenedor">
      <h1 style={{ color: "#0b6e4f", textAlign: "center" }}>
        {nombreApp} — Veterinaria
      </h1>
      <p className="subtitulo">Sistema de medicamentos, consultas y recetas</p>

      <h2>Medicamentos</h2>
      <MedicamentoLista />

      <h2>Consultas y recetas</h2>
      <ConsultaLista />

      <section className="seccion">
        <h2 style={{ color: "#0b6e4f" }}>Veterinaria — veterinarios y mascotas</h2>

        <Tarjeta titulo="Veterinarios">
          <VeterinarioLista />
        </Tarjeta>

        <Tarjeta titulo="Mascotas">
          <MascotaLista />
        </Tarjeta>
      </section>
    </div>
  );
}

export default App;
