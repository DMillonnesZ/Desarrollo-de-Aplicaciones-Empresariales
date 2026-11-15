import { useEffect } from "react";

// Aviso que desaparece a los 4 segundos. Sirve para éxitos (tipo "ok") y errores (tipo "error").
// El efecto limpia el temporizador al desmontarse o cuando llega un aviso nuevo.
function AvisoPanel({ aviso, onTerminar }) {
  useEffect(() => {
    const temporizador = setTimeout(onTerminar, 4000);
    return () => clearTimeout(temporizador);
  }, [aviso, onTerminar]);

  return (
    <p className={aviso.tipo === "error" ? "aviso aviso-error" : "aviso"}>
      {aviso.texto}
    </p>
  );
}

export default AvisoPanel;
