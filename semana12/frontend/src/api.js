import axios from "axios";

// Semana 12, Ejercicio 3: UNA sola instancia de Axios para toda la aplicación.
// La dirección del servidor y el timeout se definen aquí; los componentes solo
// escriben rutas cortas como "/medicamentos/".
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 8000,
});

export default api;
