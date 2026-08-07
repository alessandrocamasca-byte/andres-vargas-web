# CLAUDE.md · Andrés Vargas Boutique (sastrería)

Web del cliente Andrés Vargas Boutique, sastrería a medida en Lima, Perú. Objetivo: una web a la altura de las mejores sastrerías del Perú. Referencia de nivel: firenze.pe (solo inspiración de estructura y estándar, NUNCA copiar su logo, fotos ni textos).

## Repo y deploy

- **Repo:** `alessandrocamasca-byte/andres-vargas-web` (privado). Decisión del 30 jul 2026: cuenta personal; migrar a `hag240401` si Hernán lo pide.
- **Deploy:** **Cloudflare Pages conectado al repo**, proyecto `andres-vargas-web`, cuenta de Cloudflare con correo de agencia (alessandrocamasca@eqapla.com). URL de producción: **https://andres-vargas-web.pages.dev** · Push a `main` = deploy automático (sin build command, HTML puro).
- **Regla de oro:** lo publicado sale siempre del repo. Si no está pusheado, no existe.

## Estructura y fuente de verdad

- **`index.html` es la ÚNICA fuente de verdad.** Un solo archivo autocontenido (CSS y JS inline) que funciona como SPA con las 6 secciones (home, telas, camisas, trajes, corporativo, blog) más el configurador interactivo de prendas. Tiene doctype, viewport, lang, meta SEO/Open Graph y favicon inline.
- Decisión 30 jul 2026: se eliminaron `site.html` y la versión multipágina (`telas.html`, `camisas.html`, `trajes.html`, `corporativo.html`, `blog.html`, `css/`, `js/`) para evitar dos fuentes desincronizadas. Siguen en el historial de git (commit 2659660) si hiciera falta recuperarlas.
- `assets/`: logos y fotos reales del cliente, optimizados a sRGB sin perfiles ICC (2.5MB en total). Ya no se usa ninguna imagen de stock.
- Al servirse desde hosting propio sí carga Google Fonts (Oswald + Montserrat). El artifact de Claude no los permite por CSP.
- `DESIGN-SYSTEM.md`: el sistema de diseño completo y su trazabilidad al manual de marca.
- `NOTAS.md`: memoria viva del proyecto (decisiones, pendientes, incidencias). Actualizarlo en cada sesión de trabajo.

### `pauta/`: la pauta de Meta, separada de la web

La web (`index.html` + `assets/`) y la pauta son dos cosas distintas y no se mezclan. Todo lo de campañas vive en `pauta/`, con dos subcarpetas según hacia dónde mira el documento:

- **`pauta/planificacion/`**: lo que se va a hacer. Un archivo por mes, nombre `AAAA-MM-plan-mensual.html`, para que ordene solo por fecha. El de agosto 2026 (`2026-08-plan-mensual.html`) trae el embudo de conversión, el reparto del presupuesto, la estructura de campañas, el semáforo de decisión y la regla de crecimiento.
- **`pauta/reportes/`**: lo que pasó. Resultados de campaña ya corridos, misma convención de nombre (`AAAA-MM-reporte.html`). Se crea cuando haya el primer mes cerrado con datos.

Los documentos de pauta son **HTML autocontenido**: CSS inline y los escudos incrustados en base64, cero rutas a `assets/`. Así se pueden mover o enviar sueltos sin romperse. Usan el design system del cliente (`DESIGN-SYSTEM.md`), no el de e-Qapla.

**Cuidado al commitear:** el repo está conectado a Cloudflare Pages y despliega la raíz, así que cualquier cosa dentro de `pauta/` que llegue a `main` queda accesible en `andres-vargas-web.pages.dev/pauta/...`. Son documentos internos con presupuestos. Antes de pushear, decidir destino (rama aparte, repo privado propio o exclusión del deploy).

## Design system del cliente

**Fuente de verdad: `DESIGN-SYSTEM.md`** en este repo. Derivado del Manual de Marca oficial. Resumen:

- **Los tres azules del manual, y solo esos:** `--azul #1A2744` (rgb 26,39,68), `--azul-medio #293661` (41,54,97), `--azul-profundo #172740` (23,39,64). El manual dice literalmente que se usen únicamente los colores primarios.
- **NO usar oro ni ningún acento metálico.** Se eliminó el `#C4A15A` que se había inventado antes de tener el manual.
- **Neutros cálidos** derivados de la fotografía de marca: papel `#FCFBF8`, lino `#F2EEE7`, arena `#E5DFD4`, piedra `#8A8378`, tinta `#1E1E1C`.
- **Tipografía:** el manual pide **Big Noodle Titling** (display) + **Gotham** (texto). Sin webfont gratuita, así que se usan **Oswald** y **Montserrat** como sustitutos. Titulares en Oswald mayúsculas peso 300.
- **Motivo estructural:** doble filete (`.doble-filete`), tomado del doble contorno del escudo del logo. El escudo se usa como glifo divisor.
- **Tono:** heráldico y estructurado (corona, escudo, Since 1982), no atelier italiano. Alto contraste azul/papel, mayúsculas condensadas con tracking amplio, mucho aire, la fotografía carga la emoción.
- **Logo:** no distorsionar, no recolorear, no añadir efectos. El escudo no baja de 28px de ancho en pantalla.

## Mensajes clave del negocio

1. **Distribuidores oficiales de telas nacionales e importadas.** Es el diferenciador real: variedad amplia y mejores precios porque no hay intermediarios.
2. **44 años de oficio** (desde 1982). El cliente vive el proceso de crear su traje desde cero.
3. **Asesoría de sastres expertos** en telas, colores, cortes y acabados. Cada prenda sobre los gustos, necesidades y medidas del cliente.
4. **Servicio de novios** como línea propia: traje de 2 o 3 piezas, camisa a medida, corbata, pajarita, pañuelos y gemelos.

## Datos del negocio (confirmados por el cliente)

- **Slogan:** "Cada prenda que hacemos, guarda la medida exacta del carácter de quién la viste"
- **Fundación:** 1982 · más de 44 años de experiencia
- **WhatsApp:** 959 370 397 · **Correo:** servicioalcliente@andresvargas.pe · **Web:** andresvargas.pe
- **Tiendas:** Av. Primavera 252, Santiago de Surco · Jr. Ucayali 115 · 119 · 121, Cercado de Lima
- **Redes:** IG @andres_vargas_sastreria · TikTok @andresvargasboutique · Facebook "Andres Vargas" (falta URL exacta)

## Regla de honestidad de datos

**No inventar nada sobre el cliente.** En una versión anterior se inventaron precios, dos testimonios con nombres de personas inexistentes y cifras de producción; todo se eliminó. Lo que el cliente no ha confirmado no se publica: se deja fuera o se explica con una caja `.aviso` (por ejemplo, los precios se cotizan por WhatsApp, y los artículos del blog están marcados "Próximamente").

## Cómo trabajar en local

- Servidor de prueba: config `andres-vargas` en `~/Claude e-Qapla/.claude/launch.json` (python3 http.server, puerto 8765). Abrir `http://localhost:8765/` (sirve `index.html`, la única fuente de verdad).
- Los documentos de `pauta/` son autocontenidos: se abren directo con `file://`, no necesitan servidor.

## Convenciones

- Commits frecuentes y descriptivos, en español.
- Sin rayas (—) ni guiones medios (–) como puntuación en ningún texto redactado (regla EQAPLA).
- No inventar datos del cliente: lo no confirmado se marca como placeholder aquí y en NOTAS.md.
