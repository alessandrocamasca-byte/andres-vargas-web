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

Afinada el 7 ago 2026: la escala anterior se sentía grande y restaba elegancia. El criterio del ajuste fue **tipo más pequeña, más ligera y con más aire**, que es como se comportan las casas de lujo. Todo bajó entre un 15 y un 20 %, los titulares grandes pasaron a peso 200 y el tracking de los rótulos subió.

| Clase | Tamaño | Peso | Uso |
|---|---|---|---|
| `.t-hero` | `clamp(2.05rem, 5vw, 4.1rem)` | 200 | Titular de página interior. |
| `.t-xl` | `clamp(1.65rem, 3.4vw, 2.6rem)` | 200 | Titular de sección. |
| `.t-lg` | `clamp(1.32rem, 2.2vw, 1.78rem)` | 300 | Subtitular. |
| `.rotulo` | `0.67rem`, tracking `0.42em` | 400 | Rótulo superior, en Oswald mayúsculas. |
| `.lead` | `clamp(0.96rem, 1.1vw, 1.05rem)`, interlínea 1.82 | 300 | Párrafo de entrada. |
| `.mini` | `0.79rem` | 300 | Nota al pie, dato secundario. |
| `.btn` | `0.71rem`, tracking `0.24em` | 400 | Botones. |

Base del cuerpo: **15.5px con interlínea 1.8**. Los párrafos de componente van entre `0.82` y `0.89rem` con interlínea `1.75` a `1.82`. Las secciones ganaron aire: `padding-block` de `clamp(4rem, 9vw, 8.5rem)`.

**Regla:** en Oswald, cuanto más grande el texto, más ligero el peso y menos tracking; cuanto más pequeño, más peso y más tracking. Por eso `.t-hero` va en 200 con `0.008em` y `.rotulo` en 400 con `0.42em`.

Reglas: los titulares van en Oswald **mayúsculas**, peso 300, `line-height: 1.03` y `text-wrap: balance`. El cuerpo va en Montserrat peso 300–400 con `line-height: 1.75`. El slogan del hero es la excepción: Oswald peso 200 en **caja baja**, porque es una frase, no un rótulo.

---

## 3. Motivo estructural: el doble filete

El escudo del logo tiene un **doble contorno**. Ese detalle se convirtió en el separador estructural de toda la web: la clase `.doble-filete` dibuja dos líneas de 1px separadas por 3px, y aparece bajo cada bloque de argumento y cada ficha.

No es decoración arbitraria: es el logo hablando en la maquetación.

El escudo completo (`assets/escudo-*.png`) se usa además como glifo divisor centrado entre dos filetes (`.marca-div`), en lugar del típico rombo genérico.

---

## 3.b Cabecera maison

Referencia tomada de Firenze: **logo centrado con el menú debajo**, sobre una banda de color sólido, y una cinta superior que repite la propuesta de valor.

Encaja especialmente bien aquí porque el logotipo de Andrés Vargas **es un lockup vertical** (escudo sobre el nombre): centrarlo respeta su forma natural, mientras que alinearlo a la izquierda en horizontal la contradecía.

- **Cinta (`.cinta`):** desplazamiento continuo con cuatro lemas reales de la casa. Se duplica el contenido cuatro veces para que el bucle no tenga saltos. Se oculta al hacer scroll y respeta `prefers-reduced-motion`.
- **Estado normal:** `.nav` en columna, logo centrado con el escudo arriba, menú centrado debajo.
- **Estado con scroll (`.fijo`):** `.nav` pasa a fila, el logo se vuelve horizontal y encoge, la cinta colapsa a altura cero.
- **Móvil:** vuelve a fila siempre, con el menú a pantalla completa.

La cabecera es **azul sólido en todos los estados**. Esto elimina de raíz la clase de bug que dio problemas antes (texto azul sobre fondo azul cuando la cabecera era transparente) y permite que el escudo sea siempre el blanco, sin intercambios por JavaScript.

> Ojo de especificidad: `.menu a` fija el color en blanco con (0,1,1) y le gana a `.btn-claro` (0,1,0), lo que dejaba el botón "Agenda tu cita" en blanco sobre blanco. Se corrige con `.menu .btn-claro`.

## 4. Layout

- Ancho máximo `1280px`, margen lateral `clamp(1.25rem, 5vw, 4rem)`.
- **Hero a sangre completa** (`assets/hero.jpg`): una sola fotografía de ancho total, que empieza **debajo** de la banda de cabecera, no detrás. Es el patrón de Firenze y evita que el encabezado corte la cabeza del modelo.
  - La foto está compuesta con el **sujeto a la izquierda y el muro de piedra a la derecha**, así que el bloque de texto va a la derecha y el velo oscurece por ese lado. No es una decisión arbitraria: es la composición de la foto la que manda.
  - En móvil el velo pasa a vertical (de abajo hacia arriba) y el texto se alinea a la izquierda.
  - Se recortó desde `portada.tif` (3012×3307) a 1900×1008. Las fotos de marca son verticales, así que el recorte panorámico se hizo conservando la cabeza con aire y sacrificando las piernas.
- **Cabeceras de página interior con fotografía** (`.pag-hero`): las siete páginas interiores abren con una fotografía de fondo distinta y velo azul, no con azul plano. Estructura igual que el hero: `img` + `.pag-hero-velo` + contenido con `z-index: 2`.
  - El velo es **direccional**: fuerte a la izquierda, donde va el texto (0.93 a 0.90 hasta el 46 %), y se abre hacia la derecha (0.36 al 80 %, 0.18 al final) para que la fotografía se vea. En móvil pasa a un velo vertical uniforme, porque el texto ocupa todo el ancho.
  - Asignación: trajes → editorial-duo · camisas → traje-gris · telas → editorial-esmoquin-negro · novios → novios-trio-wide · corporativo → editorial-esmoquin-marfil · tiendas → hero · blog → traje-burdeos. El `object-position` se afina por página en el propio atributo `style`.
- **`--alto-cabecera`**: variable que el script mantiene sincronizada con la altura real de la cabecera (232px en escritorio, ~60px en móvil). La usan el hero (`margin-top` y `min-height`) y las cabeceras de página interior (`padding-top`). Se mide al cargar y al redimensionar, siempre en estado no condensado.
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
| Icono | `.icono` | SVG de trazo fino de 1px, 34px, sin contenedor. Hereda el color de la sección (`--azul-medio` en claro, `--azul-claro` sobre azul). Dibujados a mano, no de librería, para que el trazo sea igual de fino que los filetes. |
| Canal de contacto | `.canal` | Tarjeta con icono, nombre, explicación y el dato. Se usan en el cierre para que el visitante elija cómo agendar. |
| Cierre | `.cierre` | Sección de cierre con fotografía de fondo y velo azul denso (0.88 a 0.94). Reemplaza a los cierres planos: la foto da profundidad sin restar legibilidad. |
| Distintivo de tienda | `.tienda-badge` | Píldora sobre la foto. Marca Chacarilla como sede de la experiencia de novios. |
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

## Tema de Corporativo · ciruela

Corporativo es la única sección que no va en el azul de marca. Usa **#5D3347**.

```css
body.tema-corporativo {
  --azul:          #5D3347;
  --azul-medio:    #79445D;
  --azul-profundo: #502B3D;
  --azul-pizarra:  #7D5468;
  --azul-bruma:    #9B7889;   /* decorativo: no apto para texto */
  --azul-claro:    #CEB6C1;
  --azul-tenue:    #F0E6EA;
  --rgb-profundo:  80, 43, 61;
  --papel:  #FCFAFB;  --nube: #F5F1F3;  --filete: #E8E0E4;
}
```

**Por qué en el `<body>` y no en la página.** La cabecera vive fuera de
`.pagina`. Si se quedara azul justo encima de un héroe ciruela, esa junta se
leería como un error, no como una decisión. El middleware pone la clase también
en el servidor, así la página no entra azul y vira a la vista del visitante.

**De dónde salen los tintes.** No están elegidos a ojo: es el mismo tono (331°)
recorriendo los pasos de claridad de la familia azul, para conservar las
relaciones de contraste del sistema.

| | ratio | equivalente azul |
|---|---|---|
| ciruela sobre blanco | 10.3:1 | 14.4:1 |
| pizarra sobre blanco | 6.3:1 | 6.3:1 |
| claro sobre ciruela | 5.5:1 | 6.3:1 |

Los 49 textos de la página quedaron verificados: ninguno incumple AA.

**Los neutros también cambian.** `--papel`, `--nube` y `--filete` son fríos
porque salen de la familia azul; sobre ciruela se notaban verdosos. Se inclinan
al mismo tono conservando su claridad. `--piedra` y `--grafito` se quedan
neutros: para leer párrafos es lo que mejor funciona.

**Requisito para que funcione.** Ningún velo puede llevar el azul escrito a
mano. Los 46 `rgba(23,39,64,…)` que había pasaron a
`rgba(var(--rgb-profundo),…)`. Si se añade un degradado nuevo con el color
literal, en Corporativo se quedará azul.
