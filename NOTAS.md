# NOTAS.md · Andrés Vargas Boutique

Memoria viva del proyecto. Se actualiza en cada sesión.

## Decisiones tomadas

- **30 jul 2026 · Repo:** `alessandrocamasca-byte/andres-vargas-web`, privado, cuenta personal de Alessandro. Se migra a `hag240401` si Hernán lo pide.
- **30 jul 2026 · Fuente de verdad:** `site.html` (SPA autocontenida). La versión multipágina quedó desactualizada y se sincronizará antes del deploy real.
- **30 jul 2026 · Ubicación corregida:** la web decía Bogotá por error, ahora todo es Lima, Perú. Precios en soles.
- **18 jul 2026 · Identidad visual:** azul característico #10305F + oro champán #C4A15A, serif display + sans de sistema.
- **30 jul 2026 · Referencia de mercado:** firenze.pe/pages/sastreria como estándar a igualar o superar. No se copian sus assets (logo, fotos, textos) por derechos de marca.

## Pendientes (backlog)

1. Crear el repo remoto en GitHub y hacer el primer push (en curso).
2. Conectar Cloudflare Pages al repo (preguntar cuenta de Cloudflare a usar, regla de rigor).
3. Recibir del cliente: logo real, fotos del taller y prendas, dirección exacta, teléfono, correos, precios validados.
4. Botón flotante de WhatsApp (clave de conversión en Perú).
5. Agenda de citas real (Calendly o similar, como Firenze).
6. Sincronizar la versión multipágina desde `site.html` o decidir publicar la SPA tal cual.
7. Instalar Homebrew y `gh` CLI en esta máquina (pendiente general del workspace).
8. Dominio del cliente: preguntar si ya tiene (andresvargas.pe o similar).

## Incidencias y limitaciones

- El artifact de Claude bloquea CDNs de fuentes: Playfair Display solo carga en la versión servida con hosting propio; en el artifact se usa el fallback serif del sistema.
- `gh` CLI no está instalado en esta máquina, el repo remoto se crea vía web UI de GitHub.
- Datos de contacto y precios de la web son placeholders sin confirmar con el cliente.
