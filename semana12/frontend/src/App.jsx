import { useState } from "react";
import "./App.css";
import Tarjeta from "./components/Tarjeta";
import MedicamentoLista from "./components/MedicamentoLista";
import ConsultaLista from "./components/ConsultaLista";
import VeterinarioLista from "./components/VeterinarioLista";
import MascotaLista from "./components/MascotaLista";
import Practica from "./practica/Practica";
import ListaPractica from "./practica/ListaPractica";
import PanelVeterinarios from "./components/PanelVeterinarios";

function App() {
  const nombreApp = "VetCar";
  const [vista, setVista] = useState("panel");

  const opciones = [
    { id: "panel", texto: "Panel de veterinarios (API)" },
    { id: "api", texto: "Práctica Ajax: medicamentos (Parte 1)" },
    { id: "practica", texto: "Semana 11: catálogo y carrito" },
    { id: "semana10", texto: "Semana 10" },
  ];

  return (
    <div className="contenedor">
      <h1 style={{ color: "#0b6e4f", textAlign: "center" }}>
        {nombreApp} — Veterinaria
      </h1>
      <p className="subtitulo">Panel administrativo — Semana 12 (React + API de Django)</p>

      <nav className="pestanas">
        {opciones.map((o) => (
          <button
            key={o.id}
            className={vista === o.id ? "boton pestana-activa" : "boton"}
            onClick={() => setVista(o.id)}
          >
            {o.texto}
          </button>
        ))}
      </nav>

      {vista === "panel" && (
        <>
          <h2>Panel de veterinarios</h2>
          <PanelVeterinarios />
        </>
      )}

      {vista === "api" && (
        <>
          <h2>Medicamentos desde la API</h2>
          <ListaPractica />
        </>
      )}

      {vista === "practica" && (
        <>
          <h2>Mini catálogo con carrito</h2>
          <Practica />
        </>
      )}

      {vista === "semana10" && (
        <>
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
        </>
      )}
    </div>
  );
}

export default App;
