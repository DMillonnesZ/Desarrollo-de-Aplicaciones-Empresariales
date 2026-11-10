
import "./App.css";

const medicamentos = [
  { id: 1, uuid: "m1", nombre: "Amoxicilina 500mg", descripcion: "Antibiótico", stock: 50, precio_unitario: "12.50" },
  { id: 2, uuid: "m2", nombre: "Ivermectina", descripcion: "Antiparasitario", stock: 30, precio_unitario: "8.90" },
  { id: 3, uuid: "m3", nombre: "Meloxicam", descripcion: "Antiinflamatorio", stock: 40, precio_unitario: "15.00" },
  { id: 4, uuid: "m4", nombre: "Prednisolona 5mg", descripcion: "Corticoide", stock: 0, precio_unitario: "9.80" },
  { id: 5, uuid: "m5", nombre: "Omeprazol 20mg", descripcion: "Protector gástrico", stock: 4, precio_unitario: "11.20" },
];

const consultas = [
  {
    uuid: "c1",
    fecha: "2026-10-13T10:30:00Z",
    mascota: "Firulais",
    veterinario: "Ana Torres",
    motivo: "Vómitos",
    estado: "ATENDIDA",
    costo: "60.00",
    detalles_receta: [
      { uuid: "d1", medicamento: "Amoxicilina 500mg", cantidad: 2, precio_unitario: "12.50", dosis: "1 cada 12 horas", indicaciones: "" },
      { uuid: "d2", medicamento: "Ivermectina", cantidad: 2, precio_unitario: "8.90", dosis: "1 cada 12 horas", indicaciones: "" },
    ],
  },
  {
    uuid: "c2",
    fecha: "2026-10-10T16:00:00Z",
    mascota: "Rex",
    veterinario: "Luis Mendoza",
    motivo: "Cojera",
    estado: "ATENDIDA",
    costo: "80.00",
    detalles_receta: [
      { uuid: "d3", medicamento: "Meloxicam", cantidad: 3, precio_unitario: "15.00", dosis: "1 al día", indicaciones: "Con alimento" },
    ],
  },
  {
    uuid: "c3",
    fecha: "2026-10-20T09:00:00Z",
    mascota: "Michi",
    veterinario: "Ana Torres",
    motivo: "Control general",
    estado: "PENDIENTE",
    costo: "40.00",
    detalles_receta: [],
  },
];

const totalReceta = (detalles) =>
  detalles.reduce(
    (acc, d) => acc + d.cantidad * Number(d.precio_unitario),
    0
  );

const seguimientosActivos = (seguimientos) =>
  seguimientos.filter((s) => s.activo).length;

const veterinarios = [
  {
    id: 1,
    uuid: "v1",
    nombre: "Ana Torres",
    telefono: "",
    correo: "",
    activo: true,
    colegiatura: "CMVP-12345",
    especialidades: [1],
    fecha_ingreso: "2020-01-15",
    cupos_disponibles: 10,
  },
  {
    id: 2,
    uuid: "v2",
    nombre: "Luis Mendoza",
    telefono: "",
    correo: "",
    activo: true,
    colegiatura: "CMVP-23456",
    especialidades: [2],
    fecha_ingreso: "2021-03-10",
    cupos_disponibles: 0,
  },
  {
    id: 3,
    uuid: "v3",
    nombre: "Rosa Quispe",
    telefono: "",
    correo: "",
    activo: false,
    colegiatura: "CMVP-34567",
    especialidades: [1],
    fecha_ingreso: "2019-06-01",
    cupos_disponibles: 5,
  },
];

const fichaBase = {
  alergias: "Ninguna",
  condiciones_cronicas: "",
  seguro_veterinario: "",
  contacto_emergencia: "",
  observaciones: "Control anual",
};

const mascotas = [
  {
    uuid: "p1",
    nombre: "Firulais",
    sexo: "M",
    peso_kg: "28.50",
    activo: true,
    dueno: "Carlos Ramirez",
    raza: "Labrador",
    especie: "Perro",
    ficha_clinica: fichaBase,
    seguimientos: [
      {
        uuid: "s1",
        veterinario: "Ana Torres",
        rol: "TITULAR",
        fecha_asignacion: "2026-01-10",
        activo: true,
      },
      {
        uuid: "s2",
        veterinario: "Luis Mendoza",
        rol: "INTERCONSULTA",
        fecha_asignacion: "2026-02-05",
        activo: true,
      },
    ],
  },
  {
    uuid: "p2",
    nombre: "Michi",
    sexo: "H",
    peso_kg: "4.20",
    activo: true,
    dueno: "Maria Lopez",
    raza: "Siames",
    especie: "Gato",
    ficha_clinica: fichaBase,
    seguimientos: [
      {
        uuid: "s3",
        veterinario: "Ana Torres",
        rol: "TITULAR",
        fecha_asignacion: "2026-01-10",
        activo: true,
      },
      {
        uuid: "s4",
        veterinario: "Luis Mendoza",
        rol: "INTERCONSULTA",
        fecha_asignacion: "2026-02-05",
        activo: false,
      },
    ],
  },
  {
    uuid: "p3",
    nombre: "Rex",
    sexo: "M",
    peso_kg: "31.00",
    activo: true,
    dueno: "Jorge Salas",
    raza: "Labrador",
    especie: "Perro",
    ficha_clinica: fichaBase,
    seguimientos: [
      {
        uuid: "s5",
        veterinario: "Ana Torres",
        rol: "TITULAR",
        fecha_asignacion: "2026-01-10",
        activo: true,
      },
    ],
  },
  {
    uuid: "p4",
    nombre: "Luna",
    sexo: "H",
    peso_kg: "6.80",
    activo: false,
    dueno: "Maria Lopez",
    raza: "Poodle",
    especie: "Perro",
    ficha_clinica: fichaBase,
    seguimientos: [],
  },
];

function App() {
  const nombreApp = "VetCar";
  const igv = 0.18;

  const conIgv = (precio) =>
    (precio * (1 + igv)).toFixed(2);

  return (
    <div className="contenedor">
      <h1 style={{ color: "#0b6e4f", textAlign: "center" }}>
        {nombreApp} — Veterinaria
      </h1>

      <p className="subtitulo">
        Sistema de medicamentos, consultas y recetas
      </p>

      <p>
        Amoxicilina 500mg con IGV: S/ {conIgv(12.5)}
      </p>

      <h2>Medicamentos</h2>

      {medicamentos.length === 0 && (
        <p className="vacio">No hay registros</p>
      )}

      <ul className="lista">
        {medicamentos.map((m) => (
          <li key={m.id} className="tarjeta">
            <strong>{m.nombre}</strong>

            <p>{m.descripcion}</p>

            <p>
              Precio: S/{" "}
              {Number(m.precio_unitario).toFixed(2)}
            </p>

            {m.stock === 0 ? (
              <span className="agotado">Agotado</span>
            ) : (
              <span>Stock: {m.stock}</span>
            )}

            {m.stock > 0 && m.stock <= 5 && (
              <span className="ultimas">
                ¡Últimas unidades!
              </span>
            )}
          </li>
        ))}
      </ul>

      <h2>Consultas y recetas</h2>

      <div className="lista-consultas">
        {consultas.map((c) => (
          <div key={c.uuid} className="tarjeta">
            <h3>
              {c.mascota} — {c.motivo}
            </h3>

            <p>
              Estado:{" "}
              <span
                className={
                  c.estado === "ATENDIDA"
                    ? "atendida"
                    : "pendiente"
                }
              >
                {c.estado}
              </span>
            </p>

            <p>Veterinario: {c.veterinario}</p>

            <p>
              Costo consulta: S/{" "}
              {Number(c.costo).toFixed(2)}
            </p>

            <h4>Receta médica</h4>

            {c.detalles_receta.length === 0 ? (
              <p className="vacio">Sin receta</p>
            ) : (
              <ul>
                {c.detalles_receta.map((d) => (
                  <li key={d.uuid}>
                    {d.medicamento} × {d.cantidad}
                    {" — S/ "}
                    {(
                      d.cantidad *
                      Number(d.precio_unitario)
                    ).toFixed(2)}
                  </li>
                ))}
              </ul>
            )}

            <p className="total">
              Total receta: S/{" "}
              {totalReceta(
                c.detalles_receta
              ).toFixed(2)}
            </p>
          </div>
        ))}
      </div>

      <section className="seccion">
        <h2 style={{ color: "#0b6e4f" }}>
          Veterinaria — {veterinarios.length} veterinarios y{" "}
          {mascotas.length} mascotas
        </h2>

        <h3>Veterinarios</h3>

        {veterinarios.length === 0 && (
          <p className="vacio">No hay registros</p>
        )}

        <ul className="lista">
          {veterinarios.map((v) => (
            <li key={v.id} className="tarjeta">
              <strong>{v.nombre}</strong>{" "}
              ({v.colegiatura}) — ingreso: {v.fecha_ingreso}{" "}

              {v.cupos_disponibles === 0 ? (
                <span className="agotado">
                  Sin cupos
                </span>
              ) : (
                <span>
                  Cupos: {v.cupos_disponibles}
                </span>
              )}

              {!v.activo && (
                <span className="inactivo">
                  Inactivo
                </span>
              )}
            </li>
          ))}
        </ul>

        <h3>Mascotas</h3>

        {mascotas.length === 0 && (
          <p className="vacio">No hay registros</p>
        )}

        {mascotas.map((m) => (
          <div key={m.uuid} className="tarjeta">
            <h4 style={{ margin: 0 }}>
              {m.nombre} — {m.raza} ({m.especie})
            </h4>

            <p>
              Dueño: {m.dueno} | Peso:{" "}
              {Number(m.peso_kg).toFixed(2)} kg
            </p>

            {m.seguimientos.length === 0 ? (
              <p className="vacio">
                Sin seguimientos
              </p>
            ) : (
              <ul>
                {m.seguimientos.map((s) => (
                  <li key={s.uuid}>
                    {s.veterinario} — {s.rol}
                    {" (desde "}
                    {s.fecha_asignacion}
                    {") · "}
                    {s.activo
                      ? "activo"
                      : "inactivo"}
                  </li>
                ))}
              </ul>
            )}

            <p>
              <strong>
                Seguimientos activos:{" "}
                {seguimientosActivos(
                  m.seguimientos
                )}
              </strong>
            </p>
          </div>
        ))}
      </section>
    </div>
  );
}

export default App;
