import { useEffect, useState } from "react";
import api from "../api";
import { adaptarMedicamento, mensajesDeError } from "../adaptadores";

// Semana 12, Parte 1: recurso simple = Medicamento (GET, POST, PATCH y DELETE).
function ListaPractica() {
  const [medicamentos, setMedicamentos] = useState([]);
  const [cargando, setCargando] = useState(true); // Ejercicio 5
  const [error, setError] = useState(""); // Ejercicio 5
  const [buscar, setBuscar] = useState(""); // Ejercicio 8

  // Ejercicio 6: campos controlados del formulario
  const [nombre, setNombre] = useState("");
  const [precio, setPrecio] = useState("");
  const [stock, setStock] = useState("");
  const [erroresForm, setErroresForm] = useState([]);

  const [mensaje, setMensaje] = useState(""); // errores de DELETE / PATCH

  // Ejercicios 4, 5 y 8: GET dentro de useEffect.
  // El efecto NO es async (devolvería una promesa y no la función de limpieza):
  // la función async se declara dentro y se llama.
  useEffect(() => {
    let cancelado = false;

    async function cargar() {
      setCargando(true);
      setError("");
      try {
        const respuesta = await api.get("/medicamentos/", {
          params: { search: buscar }, // Ejercicio 8: ?search=...
        });
        if (!cancelado) {
          setMedicamentos(respuesta.data.map(adaptarMedicamento));
        }
      } catch (err) {
        console.error("No se pudo cargar la lista de medicamentos:", err);
        if (!cancelado) setError("No se pudo cargar la lista");
      } finally {
        if (!cancelado) setCargando(false);
      }
    }

    cargar();
    return () => {
      cancelado = true;
    };
  }, [buscar]); // Ejercicio 4 usaba []; el Ejercicio 8 cambia la dependencia a [buscar]

  // Ejercicio 6: POST
  const crear = async (e) => {
    e.preventDefault();
    setErroresForm([]);
    try {
      const respuesta = await api.post("/medicamentos/", {
        nombre,
        precio_unitario: precio,
        stock,
      });
      // Arreglo NUEVO (spread), sin push
      setMedicamentos((actuales) => [...actuales, adaptarMedicamento(respuesta.data)]);
      setNombre("");
      setPrecio("");
      setStock("");
    } catch (err) {
      // 400: err.response.data trae los mensajes del serializer
      setErroresForm(mensajesDeError(err));
    }
  };

  // Ejercicio 7: DELETE (204) y filter()
  const eliminar = async (id) => {
    setMensaje("");
    try {
      await api.delete(`/medicamentos/${id}/`);
      setMedicamentos((actuales) => actuales.filter((m) => m.id !== id));
    } catch (err) {
      setMensaje(mensajesDeError(err)[0]);
    }
  };

  // Ejercicio 7: PATCH (200) y map()
  const subirStock = async (medicamento) => {
    setMensaje("");
    try {
      const respuesta = await api.patch(`/medicamentos/${medicamento.id}/`, {
        stock: medicamento.stock + 1,
      });
      setMedicamentos((actuales) =>
        actuales.map((m) =>
          m.id === medicamento.id ? adaptarMedicamento(respuesta.data) : m
        )
      );
    } catch (err) {
      setMensaje(mensajesDeError(err)[0]);
    }
  };

  return (
    <div>
      {/* Ejercicio 8: campo de búsqueda controlado */}
      <input
        className="buscador"
        type="text"
        placeholder="Buscar medicamento..."
        value={buscar}
        onChange={(e) => setBuscar(e.target.value)}
      />

      {mensaje && <p className="error">{mensaje}</p>}

      {/* Ejercicio 5: los tres estados */}
      {cargando && <p className="cargando">Cargando...</p>}
      {error && !cargando && <p className="error">{error}</p>}
      {!cargando && !error && medicamentos.length === 0 && (
        <p className="vacio">No hay medicamentos para mostrar.</p>
      )}

      {!cargando && !error && (
        <ul className="lista">
          {medicamentos.map((m) => (
            <li key={m.id} className="tarjeta">
              <strong>{m.nombre}</strong>
              <p>Precio: S/ {m.precio_unitario.toFixed(2)}</p>
              {m.stock === 0 ? (
                <span className="agotado">Agotado</span>
              ) : (
                <span>Stock: {m.stock}</span>
              )}
              <div className="acciones">
                <button className="boton" onClick={() => subirStock(m)}>
                  +1 stock
                </button>
                <button className="boton boton-peligro" onClick={() => eliminar(m.id)}>
                  Eliminar
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}

      {/* Ejercicio 6: formulario controlado */}
      <form className="formulario" onSubmit={crear}>
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
        {erroresForm.map((texto) => (
          <p key={texto} className="error">
            {texto}
          </p>
        ))}
      </form>
    </div>
  );
}

export default ListaPractica;
