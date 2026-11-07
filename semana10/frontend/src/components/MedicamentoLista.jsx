import { useState } from "react";
import MedicamentoCard from "./MedicamentoCard";
import { medicamentos as medicamentosIniciales } from "../datos";

// Lista de medicamentos con buscador y formulario controlado.
// El estado de la lista vive aquí (todavía no se guarda en Django).
function MedicamentoLista() {
  const [medicamentos, setMedicamentos] = useState(medicamentosIniciales);
  const [busqueda, setBusqueda] = useState("");

  // Estado del formulario (campos controlados)
  const [nombre, setNombre] = useState("");
  const [precio, setPrecio] = useState("");
  const [stock, setStock] = useState("");
  const [error, setError] = useState("");

  const filtrados = medicamentos.filter((m) =>
    m.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  const manejarEnvio = (e) => {
    e.preventDefault();

    if (nombre.trim() === "") {
      setError("El nombre es obligatorio.");
      return;
    }
    // Regla tomada de la API de la Semana 8: validate_precio_unitario
    if (Number(precio) <= 0 || precio === "") {
      setError("El precio unitario debe ser mayor que cero.");
      return;
    }
    if (stock === "" || Number(stock) < 0) {
      setError("El stock no puede ser negativo.");
      return;
    }

    const nuevo = {
      id: Math.max(0, ...medicamentos.map((m) => m.id)) + 1,
      nombre: nombre.trim(),
      descripcion: "",
      stock: Number(stock),
      precio_unitario: precio,
    };

    // Arreglo NUEVO (spread), sin usar push
    setMedicamentos([...medicamentos, nuevo]);
    setNombre("");
    setPrecio("");
    setStock("");
    setError("");
  };

  return (
    <div>
      <input
        className="buscador"
        type="text"
        placeholder="Buscar medicamento..."
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
      />

      {filtrados.length === 0 && (
        <p className="vacio">No hay medicamentos que coincidan con la búsqueda.</p>
      )}

      <ul className="lista">
        {filtrados.map((m) => (
          <MedicamentoCard
            key={m.id}
            nombre={m.nombre}
            descripcion={m.descripcion || undefined}
            precio={m.precio_unitario}
            stock={m.stock}
          />
        ))}
      </ul>

      <form className="formulario" onSubmit={manejarEnvio}>
        <h4>Nuevo medicamento</h4>
        <input
          type="text"
          placeholder="Nombre"
          value={nombre}
          onChange={(e) => setNombre(e.target.value)}
        />
        <input
          type="number"
          step="0.01"
          placeholder="Precio unitario"
          value={precio}
          onChange={(e) => setPrecio(e.target.value)}
        />
        <input
          type="number"
          placeholder="Stock"
          value={stock}
          onChange={(e) => setStock(e.target.value)}
        />
        <button className="boton" type="submit">
          Agregar medicamento
        </button>
        {error && <p className="error">{error}</p>}
      </form>
    </div>
  );
}

export default MedicamentoLista;
