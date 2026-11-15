// Funciones adaptadoras: convierten la forma de la API a la que usa la pantalla.

// DRF entrega los decimales como TEXTO ("12.50"). Aquí se convierten a número.
export function adaptarMedicamento(medicamento) {
  return { ...medicamento, precio_unitario: Number(medicamento.precio_unitario) };
}

export function adaptarVeterinario(veterinario) {
  return { ...veterinario, cupos_disponibles: Number(veterinario.cupos_disponibles) };
}

// Convierte cualquier error de Axios en una lista de mensajes legibles.
// - Sin err.response: el servidor no respondió (Django apagado o error de red).
// - Con 400: DRF envía un objeto como { precio_unitario: ["El precio ..."] }.
// - Con 404 / 409: DRF envía { detail: "..." }.
export function mensajesDeError(err) {
  if (!err.response) {
    return ["No hay conexión con el servidor. ¿Django está encendido?"];
  }

  const datos = err.response.data;

  if (datos && typeof datos === "object") {
    if (datos.detail) return [datos.detail];

    return Object.entries(datos).flatMap(([campo, mensajes]) =>
      (Array.isArray(mensajes) ? mensajes : [mensajes]).map(
        (mensaje) => `${campo}: ${mensaje}`
      )
    );
  }

  return [`Error ${err.response.status} del servidor.`];
}
