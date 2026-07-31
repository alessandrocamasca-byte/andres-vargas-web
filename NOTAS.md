# NOTAS.md · Andrés Vargas Boutique

Memoria viva del proyecto. Se actualiza en cada sesión.

## Decisiones tomadas

- **30 jul 2026 · Design system oficial:** se recibió el material de marca real del cliente (manual de marca, logos, fotos, slogan y datos de contacto) y se reconstruyó la web sobre él. Detalle completo en `DESIGN-SYSTEM.md`.
  - Color: solo los tres azules del manual (`#1A2744`, `#293661`, `#172740`). Se **eliminó el oro champán** que se había inventado, porque el manual restringe a los colores primarios.
  - Tipografía: el manual pide Big Noodle Titling + Gotham. No hay webfont gratuita de ninguna, así que se usan **Oswald** y **Montserrat** como sustitutos. Si el cliente tiene licencia web de las originales, se autoalojan.
  - Motivo estructural: doble filete, tomado del doble contorno del escudo del logo.
  - Fundación corregida a **1982** (el logo dice Since 1982). Antes decía "Est. 1994", que era inventado.
- **30 jul 2026 · Se eliminaron todos los datos inventados** de la versión anterior: precios en soles, dos testimonios con nombres de personas que no existen (Ricardo Mejía, Daniel Ospina), cifras de producción (12.000 trajes, 400+ telas, 120 empresas, 8.000 prendas), especificaciones de confección sin confirmar (entretela flotante, ojal milanés, 17 y 25 medidas, 3 pruebas, 60 horas) y la dirección de Miraflores. Verificado en navegador: cero coincidencias.
- **30 jul 2026 · Se añadió la sección Novios**, que es una línea de servicio real del cliente según su documento, y estaba ausente.
- **30 jul 2026 · Repo:** `alessandrocamasca-byte/andres-vargas-web`, privado, cuenta personal. Se migra a `hag240401` si Hernán lo pide.
- **30 jul 2026 · Fuente de verdad:** `index.html`, un solo archivo. La versión multipágina se eliminó (recuperable en el commit 2659660).
- **30 jul 2026 · Referencia de mercado:** firenze.pe como estándar a igualar. No se copian sus assets ni textos.

## Sesión del 30 jul 2026 (segunda parte)

- **Auditoría de color contra el manual, más a fondo:** se extrajeron los operadores `scn` de los flujos de contenido del PDF. Resultado: los tres azules quedan confirmados por triple vía, y aparecieron dos tintes azul grisáceo que el manual usa 26 veces cada uno (`#505D7F` y `#74819A`). **Los neutros cálidos que había puesto eran una desviación**: el manual trabaja en gris neutro y frío. Corregidos.
- **Contraste:** el gris de texto del manual (`#818181`) da 3.8:1 en pantalla y falla AA. Se usa `#676D79` para texto, misma familia. Es la única desviación deliberada del manual y está documentada.
- **Decisión sobre testimonios (Alessandro, 30 jul):** no se publican testimonios de personas inventadas. En su lugar, prueba social real con los proyectos institucionales.
- **Nuevo:** sección de proyectos (inicio y corporativo), locales con enlace a Google Maps, bloque de marcas de tela (oculto hasta tener la lista).
- **No se publica ningún precio.** Confirmado por Alessandro.

## Pendientes (backlog)

1. ~~Crear el repo remoto y primer push.~~ HECHO: https://github.com/alessandrocamasca-byte/andres-vargas-web
2. ~~Conectar Cloudflare Pages.~~ HECHO: https://andres-vargas-web.pages.dev · Push a `main` = deploy en ~20s.
3. ~~Recibir logo y fotos reales del cliente.~~ HECHO 30 jul 2026, ya integrados.
4. ~~Botón de WhatsApp.~~ HECHO: flotante + CTAs en todas las páginas, número real 959370397.
5. ~~¿Se publican precios?~~ RESUELTO: **no se publica ningún precio.**
6. **DATOS QUE FALTAN PARA COMPLETAR LA WEB** (bloquean secciones ya construidas):
   - **Cifras:** número de ternos confeccionados, de camisas confeccionadas y de novios vestidos. Las tres tienen su componente listo; falta el número. No se inventan.
   - **Marcas de telas:** la lista de casas de tejido con las que trabajan. El bloque existe y se rellena desde el arreglo `MARCAS_TELA` en el script; mientras esté vacío el bloque no se muestra.
   - **Proyectos:** confirmar el nombre oficial de cada uno (¿"Universitario de Deportes"?, ¿qué teatro exactamente?, ¿"Barrington" es la grafía correcta?) y una línea real de qué se hizo en cada proyecto. Ahora hay una descripción mínima y genérica, sin inventar detalles.
   - **Locales:** el documento del cliente lista dos direcciones. Confirmar si hay más locales activos y sus direcciones, horarios y teléfono por local.
   - **Autorización de marca:** confirmar que el cliente puede nombrar públicamente a Universitario, el teatro y Barrington como clientes.
7. **Escribir los artículos del blog.** Los seis temas están maquetados y marcados "Próximamente" con un aviso honesto. Falta el contenido.
8. **Dominio:** el cliente ya tiene `andresvargas.pe` con una web activa. Decidir si esta reemplaza la actual, y si va al dominio raíz o a un subdominio para revisión.
9. **Licencia de fuentes:** preguntar si tienen Big Noodle Titling y Gotham para web.
10. **Facebook:** el documento solo dice "Facebook: Andres Vargas", sin URL. Se omitió el enlace en el pie para no apuntar a un perfil equivocado. Pedir la URL exacta.
11. Instalar Homebrew y `gh` CLI (pendiente general del workspace, para poder crear repos sin la web UI).

## Incidencias y limitaciones

- **Perfil ICC gigante en los TIF del cliente:** las imágenes originales (`portada.tif`, `pag 14`, `pag 15`) traían un perfil ICC incrustado de 1.8MB que hacía que cada JPEG exportado pesara 2.6MB con solo 172KB de imagen real. Se resuelve convirtiendo a sRGB y usando `--deleteColorManagementProperties` en `sips`. Dejarlo anotado por si llegan más TIF de la misma fuente.
- **Nombres de archivo con acentos en los ZIP:** el ZIP de fotos guardaba "Sin título" en cp437 y `unzip` fallaba con un error engañoso de "disk full". Se extrae con Python recodificando el nombre.
- **El panel de navegador de Claude Code es inestable en esta máquina:** se cuelga con frecuencia y las capturas van un paso por detrás del DOM. La verificación fiable es por consultas al DOM y estilos computados, no por captura de pantalla.
- **Bug corregido (30 jul):** en las páginas interiores el menú de la cabecera quedaba azul sobre el hero azul, invisible. Ahora la cabecera sin scroll va siempre en blanco, porque toda página abre con banda azul.
- **Bug corregido (30 jul):** el menú móvil no ocupaba la altura de la pantalla (64px en vez de 812px) porque dependía de que `inset: 0` resolviera la altura. Ahora lleva `height: 100svh` explícito.
- **Fotos de Unsplash retiradas:** ya no se usa ninguna. Todas las imágenes son del cliente y viven en el repo, así que no hay riesgo de que una URL externa desaparezca.
- Las muestras de tela de la página Telas son **referencias de color**, no telas reales del muestrario. Está advertido en la propia página. Si el cliente entrega fotos macro de sus telas, se sustituyen.
