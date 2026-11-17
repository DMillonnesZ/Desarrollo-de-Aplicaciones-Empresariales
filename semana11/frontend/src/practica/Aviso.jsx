import { useEffect, useState } from "react";

// El aviso solo guarda su visibilidad temporal; no duplica el estado del carrito.
export default function Aviso({ nombre }) {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const temporizador = setTimeout(() => {
      setVisible(false);
    }, 3000);

    // Evita un temporizador pendiente si el aviso cambia o se desmonta.
    return () => clearTimeout(temporizador);
  }, [nombre]);

  return visible && (
    <p className="practica-aviso" role="status">
      Agregado: {nombre}
    </p>
  );
}
