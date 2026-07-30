# CLAUDE.md · Andrés Vargas Boutique (sastrería)

Web del cliente Andrés Vargas Boutique, sastrería a medida en Lima, Perú. Objetivo: una web a la altura de las mejores sastrerías del Perú. Referencia de nivel: firenze.pe (solo inspiración de estructura y estándar, NUNCA copiar su logo, fotos ni textos).

## Repo y deploy

- **Repo:** `alessandrocamasca-byte/andres-vargas-web` (privado). Decisión del 30 jul 2026: cuenta personal; migrar a `hag240401` si Hernán lo pide.
- **Deploy:** estático puro, por regla EQAPLA va a **Cloudflare Pages conectado al repo**. Push a `main` = deploy. Aún sin configurar (ver NOTAS.md).
- **Regla de oro:** lo publicado sale siempre del repo. Si no está pusheado, no existe.

## Estructura y fuente de verdad

- **`site.html` es la fuente de verdad actual.** Es una SPA autocontenida (CSS y JS inline) con las 6 secciones (home, telas, camisas, trajes, corporativo, blog) y el configurador interactivo de prendas. Se publica también como artifact de Claude: https://claude.ai/code/artifact/c849f2a7-2caf-48f9-8085-cd46b5bd802a
- Los archivos multipágina (`index.html`, `telas.html`, `camisas.html`, `trajes.html`, `corporativo.html`, `blog.html` + `css/styles.css` + `js/main.js`) fueron la primera versión y están DESACTUALIZADOS respecto a `site.html` (les falta: configurador, sección confección, Lima en vez de Bogotá, precios en soles). Antes del deploy real hay que sincronizarlos desde `site.html` o decidir publicar la SPA.
- `NOTAS.md`: memoria viva del proyecto (decisiones, pendientes, incidencias). Actualizarlo en cada sesión de trabajo.

## Design system del cliente

- **Azul característico:** `#10305F` (paleta completa de `#071633` a `#3D74BE`, tokens `--av-azul-*` en el CSS).
- **Acento oro champán:** `#C4A15A` / `#E4CE9C` / `#9B7C3C`.
- **Neutros:** hueso `#FBFAF7`, crema `#F4F1EA`, humo `#EBE7DF`, carbón `#1B1E24`.
- **Tipografía:** serif display (Playfair Display con fallback Georgia) + sans del sistema para cuerpo. En el artifact solo fallbacks del sistema (CSP bloquea CDNs de fuentes).
- **Tono:** elegancia sartorial clásica, sin estridencias. Detalles: divisores con diamante, eyebrows con letter-spacing amplio, radius 2px.

## Mensajes clave del negocio

1. **La confección es el punto fuerte:** entretela flotante cosida a mano, ojal milanés, botones funcionales, patrón archivado de por vida, 60+ horas por traje.
2. **Biblioteca de 400+ telas** italianas e inglesas, de las más grandes del Perú.
3. A medida de verdad: patrón individual, hasta 3 pruebas.

## Datos del negocio (estado)

- Ubicación: Lima, Perú (Miraflores como placeholder, CONFIRMAR dirección real).
- Teléfono `+51 1 600 0000` y correos `citas@` / `corporativo@andresvargas.com` son PLACEHOLDERS, confirmar con el cliente antes del go-live.
- Precios de referencia en soles (S/ 2,490 / 4,890 / 6,590): validar con el cliente.
- Logo y fotos: por ahora tipografía + fotos de Unsplash. Pendiente recibir assets reales del cliente.

## Cómo trabajar en local

- Servidor de prueba: config `andres-vargas` en `~/Claude/.claude/launch.json` (python3 http.server, puerto 8765). Abrir `http://localhost:8765/site.html`.
- El artifact se actualiza republicando `site.html` (mismo path = mismo URL).

## Convenciones

- Commits frecuentes y descriptivos, en español.
- Sin rayas (—) ni guiones medios (–) como puntuación en ningún texto redactado (regla EQAPLA).
- No inventar datos del cliente: lo no confirmado se marca como placeholder aquí y en NOTAS.md.
