# Design System · Andrés Vargas Sastrería

Sistema de diseño de la web, derivado del **Manual de Marca oficial** del cliente (`2. Manual de marca.pdf`, 33 páginas) y de sus assets reales. Todo lo que está aquí sale del manual o de una decisión documentada; nada es inventado.

---

## 1. Color

El manual es explícito: *"se deberá utilizar únicamente los colores primarios especificados"*. Son tres azules, etiquetados en el manual en RGB decimal.

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--azul` | `#1A2744` | 26, 39, 68 | **Primario.** Titulares, fondos de banda, botones. |
| `--azul-medio` | `#293661` | 41, 54, 97 | Secundario. Hover, rótulos, numeración. |
| `--azul-profundo` | `#172740` | 23, 39, 64 | Fondos más profundos: pie de página, franja de cifras. |

### Cómo se verificaron (triple comprobación)

1. **Etiqueta impresa en el manual:** la página "Esquema de colores · Colores planos" imprime `26.39.68`, `41.54.97` y `23.39.64` junto a cada muestra.
2. **Píxeles del logo real:** muestreo del PNG oficial da `#18243F`, coincidente dentro del margen de conversión de perfil.
3. **Operadores de color del propio PDF:** extrayendo los `scn` de los flujos de contenido, las muestras se dibujan con `0.036 0.134 0.263` y `0.112 0.199 0.386` en el espacio de trabajo del documento, consistentes con las etiquetas.

### Tintes que el manual usa en su propia maquetación

Al extraer todos los operadores de color del PDF aparecieron dos azules desaturados usados **26 veces cada uno**, además de los primarios (50 y 47 usos). Forman parte del lenguaje visual real de la marca:

| Token | HEX | Uso |
|---|---|---|
| `--azul-pizarra` | `#505D7F` | Rótulos y metadatos sobre fondo claro. Contraste 6.3:1. |
| `--azul-claro` | `#9FAAC0` | Rótulos sobre azul. Contraste 6.3:1. |
| `--azul-bruma` | `#74819A` | El valor del manual tal cual. **Solo decorativo:** 3.8:1, no apto para texto. |
| `--azul-tenue` | `#E7EAF0` | Énfasis sobre azul. |

### Neutros

El manual no define neutros de interfaz, pero **sí revela su familia**: su maquetación usa gris neutro (`0.506` → `#818181`) y gris frío para filetes (`0.642 0.653 0.661` → `#A4A7A9`), nunca cálidos. Los neutros de la web siguen esa familia fría.

> Corrección registrada: una versión anterior usaba neutros cálidos (crema y arena) derivados de la fotografía. Se cambiaron a fríos al comprobar que el manual trabaja en gris neutro y azulado.

| Token | HEX | Uso | Contraste sobre papel |
|---|---|---|---|
| `--papel` | `#FBFBFC` | Fondo base. | — |
| `--nube` | `#F1F3F6` | Secciones alternas. | — |
| `--filete` | `#DFE3EA` | Bordes y separadores. | — |
| `--piedra` | `#676D79` | Texto secundario. | 5.0:1 |
| `--grafito` | `#4A4F58` | Texto de párrafo. | 8.0:1 |
| `--tinta` | `#1E2128` | Texto base. | 15.6:1 |

**Nota sobre el gris del manual:** su `#818181` es de documento impreso y en pantalla da 3.8:1, por debajo del mínimo AA de 4.5:1. Para texto se usa `#676D79`, la misma familia una parada más oscura. Es la única desviación deliberada del manual, y es por accesibilidad.

### Sin acento metálico (decisión)

La primera versión de la web usaba un oro champán (`#C4A15A`) como acento. **Se eliminó.** No existe en el manual, y el manual restringe el uso a los colores primarios. La jerarquía se consigue ahora con escala, peso, tracking y contraste azul/papel, que es más fiel y además más difícil de imitar.

Si el cliente quiere reintroducir un acento cálido, existe un argumento defendible: el muro cobrizo de su propia sesión editorial. Sería una ampliación del manual y debe aprobarla el cliente, no darse por supuesta.

---

## 2. Tipografía

El manual define dos familias: **Big Noodle Titling** (display) y **Gotham** (texto).

Ninguna de las dos está disponible como webfont gratuita, así que la web usa sustitutos de Google Fonts elegidos por proximidad:

| Rol | Fuente del manual | Sustituto en web | Por qué |
|---|---|---|---|
| Display | Big Noodle Titling | **Oswald** (200–600) | Condensada, alta, mayúsculas, terminaciones rectas. Es el sustituto estándar de Big Noodle. |
| Texto | Gotham | **Montserrat** (300–600) | Sustituto establecido de Gotham: geométrica, misma altura de x, proporciones muy próximas. |

**Pendiente:** si el cliente tiene licencia de Big Noodle Titling y Gotham para web, se autoalojan con `@font-face` y se sustituyen los tokens. Es un cambio de dos líneas.

### Escala

| Clase | Tamaño | Uso |
|---|---|---|
| `.t-hero` | `clamp(2.5rem, 6.6vw, 5.2rem)` | Titular de página interior. |
| `.t-xl` | `clamp(2rem, 4.4vw, 3.4rem)` | Titular de sección. |
| `.t-lg` | `clamp(1.55rem, 2.8vw, 2.2rem)` | Subtitular. |
| `.rotulo` | `0.76rem`, tracking `0.34em` | Rótulo superior de sección, en Oswald mayúsculas. |
| `.lead` | `clamp(1.02rem, 1.3vw, 1.15rem)`, peso 300 | Párrafo de entrada. |
| `.mini` | `0.86rem`, peso 300 | Nota al pie, dato secundario. |

Reglas: los titulares van en Oswald **mayúsculas**, peso 300, `line-height: 1.03` y `text-wrap: balance`. El cuerpo va en Montserrat peso 300–400 con `line-height: 1.75`. El slogan del hero es la excepción: Oswald peso 200 en **caja baja**, porque es una frase, no un rótulo.

---

## 3. Motivo estructural: el doble filete

El escudo del logo tiene un **doble contorno**. Ese detalle se convirtió en el separador estructural de toda la web: la clase `.doble-filete` dibuja dos líneas de 1px separadas por 3px, y aparece bajo cada bloque de argumento y cada ficha.

No es decoración arbitraria: es el logo hablando en la maquetación.

El escudo completo (`assets/escudo-*.png`) se usa además como glifo divisor centrado entre dos filetes (`.marca-div`), en lugar del típico rombo genérico.

---

## 4. Layout

- Ancho máximo `1280px`, margen lateral `clamp(1.25rem, 5vw, 4rem)`.
- **Hero partido asimétrico**: panel azul con el slogan (`1.02fr`) + foto editorial a altura completa (`0.98fr`). Resuelve que la fotografía de marca sea vertical, que se recortaría mal en un hero a sangre. Apila en móvil.
- Bandas alternas: papel → azul → profundo → lino. Cada página interior abre con una banda azul (`.pag-hero`), por eso la cabecera sin scroll va siempre en blanco.
- Espaciado por escala `--e1` a `--e7` (0.5rem a 4rem), con `gap` en flex y grid, nunca márgenes por elemento.

---

## 5. Componentes

| Componente | Clase | Nota |
|---|---|---|
| Botón sólido | `.btn.btn-azul` | Oswald, mayúsculas, tracking `0.2em`, sin radio. |
| Botón contorno | `.btn.btn-linea` / `.btn-linea-clara` | Versión clara para fondo azul. |
| Botón sobre azul | `.btn.btn-claro` | Fondo blanco, texto azul. |
| Enlace con flecha | `.enlace` | La flecha se separa en hover, no se mueve el texto. |
| Pilar de argumento | `.pilar.doble-filete` | Numeración `01`, `02`, `03` en Oswald. |
| Ficha de prenda | `.ficha` | Imagen `3/4` con zoom suave en hover. |
| Muestra de tela | `.tela` | Bloque de color `4/3` + nombre y descripción. |
| Chip / filtro | `.chip` | Estado activo `.on` en azul sólido. |
| Cifra | `.cifra` | Oswald peso 200 a gran tamaño sobre azul profundo. |
| Aviso | `.aviso` | Caja de lino para notas honestas (precios, alcance, estado). |
| Configurador | `.cfg` | Vista SVG pegajosa + panel de opciones. |
| Caso / proyecto | `.caso` | Tarjeta de proyecto con foto, escudo, badge, métrica y cuerpo con chips. Ver abajo. |
| Local | `.local` | Tienda con zona, dirección y enlace a Google Maps. |
| Marca de tela | `.marca-tela` | Casa de tejido. Se rellena desde el arreglo `MARCAS_TELA` del script; **si está vacío, el bloque entero se oculta**, para no publicar una caja vacía. |

**Numeración:** los `01/02/03` se usan solo donde el orden significa algo (los pasos del proceso) o donde hay exactamente tres pilares paralelos. No se numera por decorar.

### La tarjeta de caso (`.caso`)

Estructura de tarjeta de proyecto, inspirada en el formato de caso de e-Qapla pero traducida al lenguaje de Andrés Vargas: esquinas rectas en vez de redondeadas, azul del manual en vez de gradientes de color, Oswald en los rótulos y el escudo como firma sobre la foto.

```
.caso
  .caso-visual         foto 4/3 + degradado azul profundo de abajo hacia arriba
    .caso-foto         la fotografía (clase propia: si se usa .caso-visual img,
                       la regla también alcanza al escudo y lo estira a pantalla completa)
    .caso-escudo       escudo blanco, 30px, arriba a la izquierda
    .caso-badge        píldora con borde, arriba a la derecha
    .caso-meta         bloque inferior:
      .caso-rotulo     rótulo del dato, en --azul-claro
      .caso-valor      la métrica, Oswald 200 a gran tamaño
      .caso-sub        línea de apoyo
      .caso-nombre     alternativa cuando no hay métrica
  .caso-cuerpo
    .caso-cat          categoría, en --azul-pizarra
    h3                 titular del proyecto
    p                  descripción
    .caso-chips        etiquetas de lo que se hizo
```

**La métrica es opcional y el componente degrada con elegancia.** Se rellena desde el arreglo `PROYECTOS` del script, que alimenta a la vez la sección de inicio y la de corporativo. Si el campo `valor` está vacío, la tarjeta muestra el nombre del proyecto en grande sobre la foto en lugar del número, de modo que se ve intencional y no incompleta. Cuando el cliente entregue las cifras, basta con rellenar `rotulo`, `valor` y `sub`.

Variante `.sobre-azul .caso` para cuando la sección va sobre banda azul: fondo translúcido y texto en blanco.

---

## 6. Movimiento

Una sola animación: entrada al hacer scroll (`.rev` → `.ver`), 0.85s, desplazamiento de 22px, con retardos escalonados de 80ms (`data-d="1|2|3"`). Nada más. La elegancia aquí viene de la quietud, no del efecto.

`prefers-reduced-motion: reduce` desactiva todo y muestra el contenido de entrada.

---

## 7. Assets

En `assets/`, todos optimizados a sRGB y sin perfiles ICC incrustados (los TIF originales traían un perfil de 1.8MB que inflaba cada imagen a 2.6MB).

| Archivo | Origen | Uso |
|---|---|---|
| `logo-azul.png` / `logo-blanco.png` | Manual de marca | Lockup vertical completo. Pie de página. |
| `escudo-azul.png` / `escudo-blanco.png` | Recorte del isotipo del logo | Cabecera, hero, divisores. El manual define el isotipo como elemento propio. |
| `editorial-esmoquin-marfil.jpg` | `portada.tif` | Hero de inicio. |
| `editorial-duo.jpg` | `pag-14.tif` | Sección de telas y corporativo. |
| `editorial-esmoquin-negro.jpg` | `pag-15.tif` | Proceso y blog. |
| `traje-negro / petroleo / burdeos / gris .jpg` | Sesión de estudio | Colección de trajes. |
| `novios-novio / duo / trio / trio-wide .jpg` | Sesión de boda | Servicio de novios. |

Peso total: **2.5MB** (desde 8.6MB sin optimizar).

**Regla:** el logo nunca se distorsiona, no se le cambia el color ni se le añaden efectos. El manual define área restringida y tamaño mínimo de 4.2cm en impresión; en pantalla el escudo no baja de 28px de ancho.

---

## 8. Datos del negocio en la web

Todos verificados con el documento del cliente (`4. Slogan, características, datos de contacto.docx`):

- **Slogan:** "Cada prenda que hacemos, guarda la medida exacta del carácter de quién la viste"
- **Fundación:** 1982 (el logo dice *Since 1982*). Experiencia: más de 44 años.
- **Diferenciador principal:** distribuidores oficiales de telas nacionales e importadas, de ahí variedad y mejores precios.
- **WhatsApp Business:** 959 370 397
- **Correo:** servicioalcliente@andresvargas.pe
- **Web oficial:** andresvargas.pe
- **Tiendas:** Av. Primavera 252, Santiago de Surco · Jr. Ucayali 115 · 119 · 121, Cercado de Lima
- **Redes:** Instagram @andres_vargas_sastreria · Facebook Andres Vargas · TikTok @andresvargasboutique
- **Servicio de novios:** traje de 2 o 3 piezas, camisa a medida, corbata, pajarita, pañuelos y gemelos.

**No hay precios, testimonios ni cifras de producción en la web**, porque el cliente no los ha entregado. Ver `NOTAS.md`.
