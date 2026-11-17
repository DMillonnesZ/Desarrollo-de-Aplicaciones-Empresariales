# Semana 11 — Mini catálogo con carrito

Se agregaron los ejercicios 1 al 8 de la Parte 1 en `frontend/src/practica`.
La práctica se abre al iniciar la aplicación. El botón **VetCar Semana 10**
permite abrir la pantalla anterior. El carrito y el buscador son datos en memoria:
al recargar o salir de la práctica se reinician.

## Cómo ejecutarlo en Windows

1. Extrae el ZIP completo con **Extraer todo**. No lo ejecutes dentro del ZIP.
2. Abre la carpeta `semana10` en Visual Studio Code.
3. Abre **Terminal > Nueva terminal** y ejecuta:

```powershell
cd frontend
npm ci
npm run dev
```

4. Abre http://localhost:5173/ y deja la terminal ejecutándose.
5. Para detener el servidor, presiona **Ctrl+C** en esa terminal.

Usa Node.js 24 con npm (versión utilizada para comprobar este proyecto).
Si `npm` no se reconoce, instala Node.js y vuelve a abrir Visual Studio Code.
Si PowerShell bloquea `npm.ps1`, usa una terminal **Command Prompt** de VS Code,
o los comandos `npm.cmd ci` y `npm.cmd run dev`.
Si Vite indica otro puerto porque el 5173 está ocupado, abre la URL que muestre
la terminal o detén el otro servidor antes de volver a ejecutar el comando.

Para estos ocho ejercicios solo se ejecuta el frontend: los productos están
escritos en `src/practica/datos.js` y no se consulta una API ni una base de datos.

En otra terminal, ubicada también en `semana10/frontend`, verifica:

```powershell
npm run lint
npm run build
```

`build` genera `dist`. Para revisar esa compilación puedes ejecutar
`npm run preview` y abrir la dirección que aparezca en la terminal.

## Archivos agregados

| Archivo en `frontend/src/practica` | Responsabilidad |
| --- | --- |
| `datos.js` | Los cinco productos, con precios como texto. |
| `Practica.jsx` | Padre común: carrito, búsqueda, último aviso y funciones de actualización. |
| `Catalogo.jsx` | Recibe los productos filtrados; usa `map()` y `key`. |
| `ProductoCard.jsx` | Lee un producto y avisa con `onAgregar(producto)`. |
| `Carrito.jsx` | Lee las líneas; calcula unidades y total; ejecuta el efecto del título. |
| `Buscador.jsx` | Campo controlado por `valor` y `onCambiar`. |
| `Aviso.jsx` | Muestra el nombre agregado durante 3 segundos y limpia el temporizador. |
| `Practica.css` | Estilos de la práctica, con clases propias. |

`App.jsx` incorpora la navegación entre las dos pantallas. `main.jsx` mantiene
`StrictMode`. Los componentes originales de VetCar y el backend se conservan.

## Respuestas de los ejercicios

### Ejercicio 1 — Datos del padre al hijo

`Practica` importa `productos` desde `datos.js` y los entrega a `Catalogo` por la
prop `productos`. `Catalogo` recorre el arreglo y entrega cada objeto a
`ProductoCard` mediante la prop `producto`, con `key={producto.id}`.

| id | nombre | precio almacenado | stock |
| --- | --- | --- | --- |
| 1 | Café americano | `"6.50"` | 50 |
| 2 | Capuchino | `"9.00"` | 40 |
| 3 | Torta de chocolate | `"10.50"` | 5 |
| 4 | Jugo de naranja | `"7.00"` | 0 |
| 5 | Tostada | `"4.50"` | 10 |

`ProductoCard` presenta el precio con `Number(producto.precio).toFixed(2)`.
El jugo muestra **Agotado** y su botón **Agregar** está desactivado.

### Ejercicio 2 — Tipos de props

Props del ejercicio 1:

| Prop | Tipo de valor | Componente que la define/entrega | Componente que la lee |
| --- | --- | --- | --- |
| `productos` | Arreglo de objetos | `Practica` | `Catalogo` |
| `producto` | Objeto | `Catalogo`, en cada iteración de `map()` | `ProductoCard` |

Campos dentro del objeto `producto`: `id` y `stock` son números; `nombre` y
`precio` son textos. Estos campos viajan dentro del objeto, no como props
individuales. `key` es una propiedad especial que usa React para identificar
cada elemento; el componente no la recibe como una prop normal.

Props añadidas durante los ejercicios siguientes:

| Prop | Tipo | Componente que define la fuente | Componente que la lee |
| --- | --- | --- | --- |
| `onAgregar` | Función | `Practica`, reenviada por `Catalogo` | `ProductoCard` |
| `lineas` | Arreglo de objetos | `Practica` | `Carrito` |
| `onQuitar` | Función | `Practica` | `Carrito` |
| `onVaciar` | Función | `Practica` | `Carrito` |
| `valor` | Texto | `Practica` | `Buscador` |
| `onCambiar` | Función | `Practica` (`setTextoBusqueda`) | `Buscador` |
| `nombre` | Texto | `Practica` | `Aviso` |

`ProductoCard` debe tratar `producto` como un dato de solo lectura. No es dueño
de ese objeto y no debe asignar valores a sus propiedades. Aunque JavaScript
permita mutar un objeto recibido, hacerlo puede desordenar el flujo de React y
no constituye una actualización de estado. El hijo avisa al padre por una función.

En Django, el `context` que una View entrega a un Template cumple un papel
parecido: proporciona los datos que la plantilla muestra. El Template los lee;
no es el lugar donde se modifica la fuente de esos datos. En React, las props
con funciones permiten además avisar al padre sobre una interacción.

### Ejercicio 3 — Aviso del hijo al padre

El botón usa `onClick={() => onAgregar(producto)}`. Al hacer clic, llama a
`agregarAlCarrito` de `Practica`. La función imprime, por ejemplo,
`Agregar: Capuchino` en la consola del navegador, además de actualizar el carrito.

La variante incorrecta es:

```jsx
// Solo para la comprobación temporal del ejercicio; después se revierte.
onClick={onAgregar(producto)}
```

Esta expresión ejecuta la función mientras React está dibujando la tarjeta,
antes del clic. Además, asigna su resultado (`undefined` en este caso) al evento.
Si la función únicamente hace `console.log`, puede no aparecer ningún error de
React: se observan mensajes al cargar y el clic ya no ejecuta la función.
Con la función final, que cambia el estado de `Practica`, React en desarrollo
advierte que se está actualizando otro componente durante el render:

```text
Cannot update a component (`Practica`) while rendering a different component (`ProductoCard`).
```

Puede continuar con un bucle de actualizaciones. La corrección es pasar una
función que React llame después: `onClick={() => onAgregar(producto)}`.
El proyecto entregado conserva la variante correcta.

Para tu captura de esta comprobación temporal: abre **F12 > Console**, guarda
la línea incorrecta, registra el mensaje observado y restablece inmediatamente
la línea correcta. Recarga y limpia la consola antes de seguir. Si todavía
estás en la etapa de solo `console.log`, documenta la ejecución anticipada;
no afirmes que hubo un error si no apareció.

### Ejercicio 4 — Estado elevado

El carrito vive en `Practica` mediante `useState([])`. Cada línea guarda
`id`, `nombre`, `precio` y `cantidad`. La actualización usa la forma funcional
`setCarrito((actual) => ...)`: si el id existe, `map()` crea un arreglo nuevo
e incrementa la cantidad con `{ ...linea, cantidad: linea.cantidad + 1 }`.
Si no existe, se crea `[...actual, nuevaLinea]`.

Guardar el carrito en cada `ProductoCard` produciría estados separados:
ninguna tarjeta tendría el pedido completo. Guardarlo solo en `Catalogo`
lo dejaría fuera del alcance directo de su hermano `Carrito`. Se eleva al
padre común para tener una única fuente del dato y compartirla por props.

### Ejercicio 5 — Datos derivados

En `Carrito`, dos llamadas a `reduce()` calculan las unidades y el importe.
El precio se convierte con `Number()` para realizar la multiplicación.

Prueba: pulsa **Agregar Capuchino** dos veces y **Agregar Café americano** una.

| Línea | Cantidad | Precio | Subtotal |
| --- | --- | --- | --- |
| Capuchino | 2 | S/ 9.00 | S/ 18.00 |
| Café americano | 1 | S/ 6.50 | S/ 6.50 |
| Total | 3 unidades | | **S/ 24.50** |

El total no necesita otro `useState` porque se obtiene completamente del
carrito actual. Al cambiar las líneas se vuelve a calcular durante el render.
Guardarlo también en estado duplicaría información que habría que sincronizar.

### Ejercicio 6 — Quitar y vaciar

El botón **Quitar** ejecuta `onQuitar(linea.id)`. `Practica` actualiza con
`actual.filter((linea) => linea.id !== id)`, eliminando la línea completa.
**Vaciar carrito** avisa con `onVaciar` y el padre ejecuta `setCarrito([])`.
`Carrito` usa `lineas.length === 0 && ...` para mostrar **El carrito está vacío**.

Desde la prueba anterior, quitar Café americano deja 2 unidades y S/ 18.00.
Vaciar deja 0 unidades, S/ 0.00 y el mensaje de carrito vacío.
En la práctica no se usan `push()` ni `splice()` sobre el estado.

### Ejercicio 7 — Filtro compartido

`textoBusqueda` vive en `Practica`. `Buscador` recibe `valor` y `onCambiar`;
su `onChange` envía al padre `evento.target.value`. El padre filtra con
`filter()` e `includes()`, ignorando mayúsculas y espacios al principio/final.

| Texto escrito | Resultado |
| --- | --- |
| `ca` | Café americano y Capuchino. |
| `zzz` | No hay productos que coincidan. |
| Campo vacío | Vuelven los cinco productos. |

`Buscador` y `Catalogo` no se comunican directamente: el buscador avisa al padre,
el padre actualiza su estado y entrega el resultado al catálogo mediante props.
Buscar no borra ni altera las líneas del carrito.

### Ejercicio 8 — Efectos y limpieza

`Carrito` calcula `cantidad` y usa un efecto con `[cantidad]`. En la prueba de
tres unidades el título es **Carrito (3) — Cafetería** y la consola registra
`Efecto Carrito: 3 unidades`. La limpieza restaura el título previo al salir.

| Dependencias | Cuándo se ejecuta el efecto |
| --- | --- |
| `[]` | Tras el montaje. No responde a cambios de cantidad. |
| `[cantidad]` | Tras el montaje y cuando cambia ese valor. Buscar sin cambiar unidades no lo vuelve a ejecutar. |
| Sin arreglo | Tras cada render confirmado del componente. |

Antes de repetir un efecto, React ejecuta su limpieza anterior; también la
ejecuta al desmontar. En desarrollo, `StrictMode` hace un ciclo adicional de
configuración y limpieza al montar para detectar problemas. Por eso puede
aparecer dos veces el mensaje inicial, sin que un clic agregue dos unidades.
La función que actualiza el carrito es pura y los logs y avisos se ejecutan
fuera de ella.

`Aviso` muestra **Agregado: nombre**. Usa `setTimeout(..., 3000)` y devuelve
`() => clearTimeout(temporizador)`. Cada agregado recibe una `key` nueva:
si agregas el mismo producto seguido, sus 3 segundos comienzan otra vez.
El único estado interno del aviso es su visibilidad temporal.

Las salidas de `npm run lint`, `npm run build` y las comprobaciones de
funcionamiento se registran en `docs/VERIFICACION-SEMANA11.txt`.

## Capturas para el Word

Pega cada evidencia debajo del ejercicio correspondiente. Puedes reutilizar
una misma captura si demuestra varios ejercicios. Usa **Win+Shift+S**.
Conserva las capturas de código: el enunciado también las solicita.

| Evidencia | Qué debes mostrar | Ejercicios |
| --- | --- | --- |
| Código de datos y props | VS Code con `src/practica` desplegado. Abre `datos.js`, `Catalogo.jsx` y `ProductoCard.jsx`; muestra `map`, `key`, `producto` y el evento. | 1, 2, 3 |
| Página inicial | Cinco productos, precios con dos decimales, Jugo de naranja agotado y botón desactivado. | 1, 3 |
| Código del padre | `Practica.jsx`: `useState`, actualización con `map` y spread, `filter`, vaciado y props de sus hijos. Desplázate si necesitas una segunda captura. | 4, 6, 7 |
| Carrito con el ejemplo | Dos Capuchinos + un Café americano: 3 unidades, S/ 24.50. Incluye la pestaña y la consola con el log. Pulsa el último Agregar justo antes para incluir el aviso. | 3, 4, 5, 8 |
| Quitar y vaciar | Después de quitar Café: S/ 18.00 y 2 unidades. Después de Vaciar: S/ 0.00 y mensaje vacío. Puedes unir ambas capturas en el Word. | 6 |
| Dos búsquedas | Una captura con `ca` (dos productos) y otra con `zzz` (mensaje sin coincidencias). | 7 |
| Código de efectos | VS Code dividido con `Carrito.jsx` (`reduce`, título y `[cantidad]`) y `Aviso.jsx` (`setTimeout` y `clearTimeout`). | 5, 8 |
| Evento incorrecto temporal | Consola con la ejecución anticipada o el aviso real, y la línea incorrecta. Después restaura el código correcto. | 3 |
| Verificación final | Terminal con `npm run lint` y `npm run build` completados; una captura puede mostrar ambos. | 8 |

Orden práctico: captura la página inicial; agrega 2 Capuchinos y 1 Café;
captura el total; quita Café; vacía; prueba `ca`; prueba `zzz`; borra la búsqueda;
captura el código y la terminal. Haz la comprobación del evento incorrecto
al final y restablece el código correcto antes de terminar.

Este ZIP corresponde a la Parte 1 solicitada. La adaptación del panel y su
publicación de los ejercicios 9 al 14 son la Parte 2 del documento.
