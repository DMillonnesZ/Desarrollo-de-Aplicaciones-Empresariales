import { useCallback, useState } from "react";
import { productos } from "./datos";
import Catalogo from "./Catalogo";
import Carrito from "./Carrito";
import Buscador from "./Buscador";
import Aviso from "./Aviso";

// Componente PADRE: aquí vive todo el estado que comparten los hermanos.
function Practica() {
  const [carrito, setCarrito] = useState([]); // Ejercicio 4
  const [buscar, setBuscar] = useState(""); // Ejercicio 7
  const [aviso, setAviso] = useState(null); // Ejercicio 8

  // Ejercicios 3 y 4: el hijo la recibe por props como onAgregar y la ejecuta con el clic.
  const agregarAlCarrito = (producto) => {
    const yaEsta = carrito.some((l) => l.id === producto.id);

    if (yaEsta) {
      // Ya existe: arreglo nuevo con map(), solo cambia la cantidad de esa línea.
      setCarrito(
        carrito.map((l) =>
          l.id === producto.id ? { ...l, cantidad: l.cantidad + 1 } : l
        )
      );
    } else {
      // No existe: arreglo nuevo con spread (sin push).
      setCarrito([
        ...carrito,
        {
          id: producto.id,
          nombre: producto.nombre,
          precio: producto.precio,
          cantidad: 1,
        },
      ]);
    }
    setAviso({ nombre: producto.nombre, momento: Date.now() });
  };

  // Ejercicio 6: quitar y vaciar, sin push ni splice.
  const quitarDelCarrito = (id) => setCarrito(carrito.filter((l) => l.id !== id));
  const vaciarCarrito = () => setCarrito([]);

  // useCallback mantiene la misma función entre renders para no reiniciar el temporizador.
  const ocultarAviso = useCallback(() => setAviso(null), []);

  // Ejercicio 7: se filtra ANTES de entregar los productos a Catalogo.
  const filtrados = productos.filter((p) =>
    p.nombre.toLowerCase().includes(buscar.toLowerCase())
  );

  return (
    <div>
      <Buscador valor={buscar} onCambiar={setBuscar} />
      {aviso && <Aviso aviso={aviso} onTerminar={ocultarAviso} />}

      <div className="dos-columnas">
        <Catalogo productos={filtrados} onAgregar={agregarAlCarrito} />
        <Carrito
          lineas={carrito}
          onQuitar={quitarDelCarrito}
          onVaciar={vaciarCarrito}
        />
      </div>
    </div>
  );
}

export default Practica;
