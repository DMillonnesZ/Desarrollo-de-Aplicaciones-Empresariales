import { useEffect } from "react";

// Ejercicio 8: aviso temporal. Desaparece a los 3 segundos con setTimeout
// y limpia el temporizador con la función que devuelve el efecto.
function Aviso({ aviso, onTerminar }) {
  useEffect(() => {
    const temporizador = setTimeout(onTerminar, 3000);
    return () => clearTimeout(temporizador);
  }, [aviso, onTerminar]);

  return <p className="aviso">Agregado: {aviso.nombre}</p>;
}

export default Aviso;
