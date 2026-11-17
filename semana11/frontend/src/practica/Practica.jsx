import { useState } from "react";
import { productos } from "./datos";
import Buscador from "./Buscador";
import Catalogo from "./Catalogo";
import Carrito from "./Carrito";
import Aviso from "./Aviso";
import "./Practica.css";

// Padre común: conserva el estado que necesitan los componentes hermanos.
export default function Practica() {
  const [carrito, setCarrito] = useState([]);
  const [textoBusqueda, setTextoBusqueda] = useState("");
  const [aviso, setAviso] = useState(null);

  function agregarAlCarrito(producto) {
    if (producto.stock === 0) return;
    // Ejercicio 3: comprueba el evento en la consola del navegador.
    console.log("Agregar:", producto.nombre);

    // Actualización funcional e inmutable: el estado previo no se modifica.
    setCarrito((actual) => {
      const existe = actual.some((linea) => linea.id === producto.id);
      if (existe) {
        return actual.map((linea) =>
          linea.id === producto.id
            ? { ...linea, cantidad: linea.cantidad + 1 }
            : linea,
        );
      }
      return [
        ...actual,
        {
          id: producto.id,
          nombre: producto.nombre,
          precio: producto.precio,
          cantidad: 1,
        },
      ];
    });

    // Una key nueva reinicia Aviso incluso al agregar el mismo producto seguido.
    // Los efectos secundarios se mantienen fuera del actualizador de setCarrito.
    setAviso({ id: crypto.randomUUID(), nombre: producto.nombre });
  }

  function quitarDelCarrito(id) {
    setCarrito((actual) => actual.filter((linea) => linea.id !== id));
  }

  function vaciarCarrito() {
    setCarrito([]);
  }

  // El filtro también es derivado: no necesita otro estado ni un efecto.
  const productosFiltrados = productos.filter((producto) =>
    producto.nombre.toLowerCase().includes(textoBusqueda.trim().toLowerCase()),
  );

  return (
    <main className="practica">
      <header className="practica-cabecera">
        <span className="practica-etiqueta">Semana 11 · Parte 1</span>
        <h1>Cafetería</h1>
        <p>Elige tus favoritos y arma tu pedido.</p>
      </header>

      <div className="practica-contenido">
        <div>
          <Buscador valor={textoBusqueda} onCambiar={setTextoBusqueda} />
          <Catalogo productos={productosFiltrados} onAgregar={agregarAlCarrito} />
        </div>
        <Carrito
          lineas={carrito}
          onQuitar={quitarDelCarrito}
          onVaciar={vaciarCarrito}
        />
      </div>

      {aviso && <Aviso key={aviso.id} nombre={aviso.nombre} />}
      <footer className="practica-pie">
        Mini catálogo con carrito · Datos de práctica en memoria
      </footer>
    </main>
  );
}
