import ConsultaCard from "./ConsultaCard";
import { consultas } from "../datos";

function ConsultaLista() {
  return (
    <div className="lista-consultas">
      {consultas.map((c) => (
        <ConsultaCard
          key={c.uuid}
          mascota={c.mascota}
          motivo={c.motivo}
          estado={c.estado}
          veterinario={c.veterinario}
          costo={c.costo}
          detalles={c.detalles_receta}
        />
      ))}
    </div>
  );
}

export default ConsultaLista;
