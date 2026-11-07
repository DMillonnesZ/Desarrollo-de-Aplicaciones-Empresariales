// Componente contenedor: recibe un título y children (lo que se escribe entre sus etiquetas).
function Tarjeta({ titulo, children }) {
  return (
    <section className="tarjeta-contenedor">
      <h3 className="tarjeta-titulo">{titulo}</h3>
      {children}
    </section>
  );
}

export default Tarjeta;
