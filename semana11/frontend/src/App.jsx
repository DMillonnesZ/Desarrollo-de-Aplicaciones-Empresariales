import { useState } from "react";
import "./App.css";
import Practica from "./practica/Practica";
import Tarjeta from "./components/Tarjeta";
import MedicamentoLista from "./components/MedicamentoLista";
import ConsultaLista from "./components/ConsultaLista";
import VeterinarioLista from "./components/VeterinarioLista";
import MascotaLista from "./components/MascotaLista";

function App() {
  const nombreApp = "VetCar";
  const [pantalla, setPantalla] = useState("practica");

  return (
    <>
      <nav className="laboratorio-nav" aria-label="Laboratorios">
        <strong>Desarrollo de Aplicaciones Empresariales</strong>
        <div>
          <button
            type="button"
            aria-pressed={pantalla === "practica"}
            onClick={() => setPantalla("practica")}
          >
            Práctica Semana 11
          </button>
          <button
            type="button"
            aria-pressed={pantalla === "vetcar"}
            onClick={() => setPantalla("vetcar")}
          >
            VetCar Semana 10
          </button>
        </div>
      </nav>
      {pantalla === "practica" ? (
        <Practica />
      ) : (
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
      )}
    </>
  );
}

export default App;
