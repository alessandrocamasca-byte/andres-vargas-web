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
- **Tarjeta de caso (30 jul, tarde):** a pedido de Alessandro, la sección de proyectos se rehizo con el formato de caso de e-Qapla (foto con degradado, badge, métrica grande, cuerpo con chips) pero traducido al manual de Andrés Vargas: esquinas rectas, azul del manual, Oswald y el escudo como firma sobre la foto. Se alimenta del arreglo `PROYECTOS` en el script, que sirve a inicio y a corporativo a la vez. **La métrica es opcional**: sin ella la tarjeta muestra el nombre del proyecto en grande, para no verse incompleta mientras faltan las cifras.
- **Bug corregido:** el escudo sobre la foto salía a pantalla completa porque `.caso-visual img` (0,1,1) le ganaba en especificidad a `.caso-escudo` (0,1,0). La foto ahora tiene su propia clase `.caso-foto`.
- **Fotos de los casos:** por ahora cada tarjeta usa una foto del catálogo del cliente, no del proyecto concreto. Pedir fotos reales de cada proyecto para sustituirlas.

## Sesión del 31 jul 2026 · pauta de agosto

- **Nuevo documento:** `pauta/planificacion/2026-08-plan-mensual.html`, embudo de conversión y plan de pauta de agosto 2026 sobre un presupuesto de S/ 2 000 indicado por el cliente. Arquitectura tomada del reporte de Blicket (`5. Flama/Reporte-Blicket-Ruta-Jul2026.html`): embudo invertido AIDA con TOFU/MOFU/BOFU/LEAL, tabla de tasas de paso, ruta del mes, semáforo de decisión y regla de crecimiento. Traducido al manual de Andrés Vargas: solo los tres azules, Oswald y Montserrat, doble filete, esquinas rectas, escudo como firma, sin acento metálico.
- **Estructura nueva `pauta/`:** se separó la pauta de la web, con `planificacion/` (lo que se va a hacer) y `reportes/` (lo que pasó, aún vacía). Convención de nombre `AAAA-MM-...`. Detalle en `CLAUDE.md`.
- **Reparto del cliente:** 50% camisas a WhatsApp (S/ 1 000), 35% trajes a WhatsApp (S/ 700), 15% seguidores en Instagram (S/ 300). Sobre 31 días: S/ 32,26 / S/ 22,58 / S/ 9,68 al día, S/ 64,52 en total.
- **Techos de costo derivados del presupuesto** (umbral de ~50 eventos por conjunto y por semana que Meta necesita para salir del aprendizaje): S/ 4,52 por conversación en camisas, S/ 3,16 en trajes, S/ 1,35 por seguidor. **Son requisitos que impone el presupuesto, no proyecciones.** No hay ninguna proyección de resultados en el documento.
- **Tensión señalada al cliente:** el techo de trajes es el más apretado justo en el producto de decisión más lenta, así que esa campaña probablemente no salga del aprendizaje. Se respeta el reparto porque es decisión del cliente, y se deja escrito que trajes se evalúa por cotizaciones y ticket, no por costo por conversación. Recomendación asociada: un solo conjunto de anuncios por campaña, variantes a nivel de anuncio.
- **BLOQUEANTE de datos · campañas de julio 2026:** no se pudieron leer. La cuenta `Andres Vargas Boutique E-qapla` (ID **1655176831742937**, PEN) está activa y con medio de pago, pero Meta **no le tiene habilitada la conexión de API** (`is_ads_mcp_enabled: false`, motivo: despliegue por etapas de Meta). Se descartó `Textiles Vargas` (ID 1736919700284229): sin actividad en julio 2026, no es la de la sastrería. El documento **no lleva ninguna cifra histórica**: las celdas van marcadas "Por leer" y "Sin registro", nunca rellenadas con números plausibles. Se cierra el hueco por export del Administrador de Anuncios, por revisión en navegador con sesión abierta, o esperando a que Meta habilite la API.
- **Verificado en navegador** a 375, 691 y 1280 px: sin desbordes, sin texto recortado por el `clip-path` del embudo, escudos base64 cargando, cero rayas (—) ni guiones medios en el texto.

### Segunda versión del documento (misma sesión)

A pedido de Alessandro se recortó a lo esencial y se rehizo el enfoque. El archivo es el mismo (`pauta/planificacion/2026-08-plan-mensual.html`), reescrito de 8 bloques a 4.

- **De documento estático a modelo vivo.** Como la cuenta sigue sin API (se reconsultó, sigue `is_ads_mcp_enabled: false`), en vez de dejar el hueco de julio el documento trae un **panel de entrada**: se escriben inversión, alcance, clics, conversaciones y seguidores de julio, y todo el pronóstico se recalcula solo. Con los campos vacíos, cada cifra dice "Pendiente"; no se rellena nada con estimaciones.
- **Comparador de dos columnas:** julio real a la izquierda, agosto proyectado a la derecha, cinco etapas (alcance, clics, conversaciones, cotizaciones, ventas).
- **Cómo proyecta:** toma los costos unitarios reales de julio (CPM, CPC, costo por conversación, costo por seguidor) y los aplica al presupuesto de agosto. Cada cifra lleva un **escenario conservador con el costo +25%**, porque partir por zonas y mover presupuesto encarece.
- **Cotizaciones y ventas son supuestos declarados**, con controles editables (arranque 40% y 20%). Van con chip "Supuesto", fondo rayado y nota de que no deben presentarse al cliente como pronóstico. Autorizado explícitamente por Alessandro, que pidió suposiciones siempre que quedaran marcadas.
- **NUEVA ESTRUCTURA: 5 conjuntos.** Camisas y trajes se parten en dos conjuntos cada una, **Chacarilla** y **Lima** (excluyendo Chacarilla), con el mismo presupuesto por zona. Seguidores queda en uno solo.

  | Conjunto | Presupuesto | Al día | Techo por evento |
  |---|---|---|---|
  | Camisas Chacarilla | S/ 500 | S/ 16,13 | S/ 2,26 |
  | Camisas Lima | S/ 500 | S/ 16,13 | S/ 2,26 |
  | Trajes Chacarilla | S/ 350 | S/ 11,29 | S/ 1,58 |
  | Trajes Lima | S/ 350 | S/ 11,29 | S/ 1,58 |
  | Seguidores Lima | S/ 300 | S/ 9,68 | S/ 1,35 |

- **Consecuencia señalada:** partir en dos parte en dos el presupuesto por conjunto y con él el techo de costo. Camisas baja de S/ 4,52 a S/ 2,26 y trajes de S/ 3,16 a S/ 1,58. Con S/ 1,58 por conversación de WhatsApp sobre un traje a medida, lo más probable es que **los cuatro conjuntos de WhatsApp corran en aprendizaje casi todo el mes**. Se gana lectura por zona y se paga con eficiencia. Queda dicho en el documento.
- **Detalles de formato corregidos en revisión:** el JS formateaba en `es-PE` puro (`1,200.00`) y el texto estático usa estilo europeo (`1 200,00`); se unificó al segundo, porcentajes incluidos. La etiqueta del escenario conservador decía "425 a 340", que se leía como rango invertido, y pasó a "conservador 340". Las barras de cotizaciones y ventas salían a todo el ancho (julio no tiene valor con qué comparar, así que la fila entera era su máximo) y hacían parecer que las ventas eran tan grandes que el alcance: ahora se escalan contra las conversaciones y se ve la caída real del embudo.
- **Verificado con cifras de prueba** (inv 1200, alcance 40 000, clics 1600, conv 300, seg 250): CPM 30, CPC 0,75, costo por conversación 4,00 y costo por seguidor 4,80; proyecta 56 667 de alcance, 2 267 clics y 425 conversaciones sobre los S/ 1 700 de WhatsApp, con 250 y 175 por campaña. Aritmética comprobada a mano.

### Tercera versión: con datos reales de julio

Alessandro cuestionó por qué no se podía leer la cuenta teniendo Facebook conectado. Al revisarlo salieron dos cosas: que yo no había llegado a **intentar** la llamada (me frené en el flag `is_ads_mcp_enabled: false` sin ver que `is_queryable` venía en `true`), y que al intentarla la API la rechaza igual con un error explícito. Con su autorización se leyó por navegador y **el hueco de datos quedó cerrado**.

**CÓMO LEER ESTA CUENTA (importante para el futuro):** la API de Meta no funciona para `1655176831742937` y no hay nada que arreglar de nuestro lado (ver memoria [[andres-vargas-proyecto]]). Se lee por navegador, con la sesión del usuario:
`https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=1655176831742937&date=AAAA-MM-DD_AAAA-MM-DD`
Las columnas de clics, CTR, CPM e impresiones no salen en el primer pantallazo: hay que arrastrar la barra horizontal del pie de la tabla (aparece con shift + rueda sobre la tabla).

**JULIO 2026 · 1 al 30 (30 días) · leído el 31-jul-2026:**

| Campaña | Invertido | Alcance | Frec. | Clics | CTR | Resultados | Costo |
|---|---|---|---|---|---|---|---|
| 2. EQ_MENSAJES A WSP_CAMISAS A MEDIDA | S/ 604,28 | 24 196 | 1,92 | 630 | 1,36% | **328** conversaciones | **S/ 1,84** |
| 3. EQ_MENSAJES A WSP_TRAJES A MEDIDA | S/ 730,00 | 25 767 | 2,14 | 561 | 1,02% | **199** conversaciones | **S/ 3,67** |
| 4. EQ_MENSAJES A WSP_GIFTCARD (off) | S/ 187,12 | 6 792 | 1,89 | 123 | 0,96% | 45 conversaciones | S/ 4,16 |
| 1. EQ_TRAFICO A IG_ANDRES VARGAS | S/ 738,71 | 63 305 | 1,65 | 4 013 | 3,85% | 4 135 **visitas al perfil** | S/ 0,18 |
| **Total (22 campañas)** | **S/ 2 260,11** | 102 251 único | 2,14 | 5 327 | 2,44% | 572 conversaciones | |

Comprobación: la suma de las cuatro campañas da exactamente los S/ 2 260,11 que reporta Meta como gasto total. Las otras 18 campañas están desactivadas con S/ 0,00.

**Hallazgos que cambian el plan:**

1. **Ya existían campañas separadas de camisas y trajes.** No hay que crearlas, hay que partirlas por zona.
2. **La partición funciona en camisas y no en trajes.** Con el costo real y el umbral de 50 eventos por conjunto y semana: camisas a S/ 1,84 da 61 conversaciones semanales por conjunto (pasa); trajes a S/ 3,67 da 22 (no pasa). **Trajes tampoco pasa sin partir**: en un solo conjunto serían 43, todavía bajo 50. El problema no es la partición, es que el presupuesto de trajes es chico para lo que cuesta su conversación. Se armó partido igual porque es la instrucción del cliente, con la advertencia escrita en el bloque 03.
3. **Agosto es un recorte, no un aumento.** Julio gastó S/ 75,34 al día contra los S/ 64,52 de agosto: **14% menos por día**. El pronóstico de conversaciones sube igual porque se retira presupuesto de Instagram y de la giftcard y se concentra en camisas, la campaña más barata de la cuenta.
4. **NO SE PUEDE PROYECTAR SEGUIDORES.** La campaña de IG de julio medía **visitas al perfil** (S/ 0,18), no seguidores. Son eventos distintos y el seguidor cuesta bastante más. No se inventó una cifra: el bloque 04 explica el hueco y deja la decisión al cliente (mantener visitas al perfil, que sí tiene referencia, o cambiar a seguidores asumiendo que el primer mes es para averiguar el costo).

**Pronóstico de agosto** (cada campaña con su propio costo de julio, no con un promedio): camisas 543 conversaciones (+215 vs julio), trajes 191 (-8), **total 734**; escenario conservador con costo +25%: 434 + 153 = **587**. Alcance de 49 963 a 64 749 y clics de 1 191 a 1 581.

El documento ya no tiene panel de entrada: julio va fijo en el script. Solo quedan editables los dos supuestos de cotización y venta.

### Plan de medios real de agosto (reemplaza todo lo anterior)

Alessandro entregó su cuadro de plan de medios, que es bastante distinto de lo que se había supuesto. **Fuente de verdad: `pauta/planificacion/2026-08-plan-medios.html`.** El plan de S/ 2 000 quedó como `2026-08-plan-mensual-SUPERADO.html` (no borrar todavía: tiene el comparador de embudos julio contra agosto, que puede reutilizarse).

**Diferencias contra lo que se había asumido:** el presupuesto es **S/ 3 103,99** y no S/ 2 000; son **8 campañas** y no 3; y la segunda zona es **Huallaga**, no "resto de Lima". Las dos zonas son las dos tiendas.

| Frente | Campañas | Inversión | % |
|---|---|---|---|
| Leads (WhatsApp) | Camisas Chacarilla S/ 372, Camisas Huallaga S/ 310, Trajes Chacarilla S/ 372, Trajes Huallaga S/ 310 | S/ 1 364,00 | 43,9% |
| Seguidores IG | 1 480 seguidores/mes a S/ 0,6486 | S/ 959,99 | 30,9% |
| Alcance | Cómo llegar Chacarilla S/ 310, Cómo llegar Huallaga S/ 310, Atendemos domingos S/ 160 | S/ 780,00 | 25,1% |

Aritmética del cuadro verificada: cuadra exacto en S/ 3 103,99.

**OBJETIVO DE LEADS FIJADO: 450 conversaciones** (piso conservador 445, techo con la eficiencia de julio 556). Estimado con el costo por conversación real de julio por producto (camisas S/ 1,84, trajes S/ 3,67), no con promedios ni referencias de sector. Por campaña en escenario conservador: camisas Chacarilla 162, camisas Huallaga 135, trajes Chacarilla 81, trajes Huallaga 68. Hitos semanales acumulados: 102, 203, 305, 406, 450. Techos de alarma: camisas S/ 2,30, trajes S/ 4,59.

**Hallazgos que hay que tener presentes:**

1. **El objetivo es MENOR que julio y hay que decirlo.** Julio: S/ 1 334,28 en 2 campañas dieron 527 conversaciones. Agosto: S/ 1 364 en 4 campañas, objetivo 450. Un 15% menos de leads con un 2% más de presupuesto. Es el precio de partir por zonas: el mismo dinero en cuatro campañas deja a cada una con pocos eventos semanales.
2. **Ninguna de las 4 campañas de leads llega al umbral de 50 eventos/semana** por conjunto: camisas 46 y 38, trajes 23 y 19. **Arreglo barato en camisas:** subir las dos zonas a S/ 13,20 al día y las dos pasan; cuesta S/ 134 más al mes y es el mejor uso de ese dinero en todo el plan. **Trajes no tiene arreglo:** necesitaría S/ 26,20 al día (S/ 812/mes) en un solo conjunto, y tiene S/ 682 repartidos en dos.
3. **CATCH DE CALENDARIO: agosto 2026 empieza en sábado**, así que tiene 5 sábados y 5 domingos, no 4. La campaña "Atendemos los domingos" está presupuestada con 16 días (S/ 160) pero jue+vie+sáb+dom son **18 días = S/ 180**. Faltan S/ 20. Se sube la línea a S/ 180 (total S/ 3 123,99) o se baja el diario a S/ 8,89.
4. **PENDIENTE DE CONFIRMAR: el costo por seguidor de S/ 0,6486** (1 184 seguidores por S/ 767,99). No se pudo verificar porque la campaña de IG de julio medía **visitas al perfil** (4 135 a S/ 0,18), no seguidores. Preguntado a Alessandro de qué campaña o periodo sale.
5. **No hay pronóstico de alcance.** La cuenta no tiene ninguna campaña con objetivo Alcance, así que no hay costo de referencia. Solo se acotó un rango con los costos por mil alcanzados de julio (27 500 a 66 800 personas con los S/ 780), declarado como razonamiento y no como dato.

### Versión ejecutiva con datos por conjunto (VIGENTE)

Alessandro entregó el nivel **conjunto de anuncios** de julio y pidió tres cosas: ajustar los leads con esa data, **quitar el escenario conservador** (julio ya es el piso, la meta es mantener y mejorar es ganancia) y volverlo **presentación ejecutiva para CEO sin tiempo**: título sobrio, poco texto, solo lo esencial. Documento reescrito a 5 bloques, 1 037 palabras, 5 tablas y casi nada de prosa.

**JULIO 2026 · 1 al 31 · nivel conjunto de anuncios:**

| Conjunto | Conversaciones | Alcance | Frec. | Costo |
|---|---|---|---|---|
| 2.1 CAMISAS_HUALLAGA_ACOTADO | 206 | 15 005 | 1,92 | **S/ 1,52** |
| 2.2 CAMISAS_CHACARILLA_ACOTADO | 139 | 12 615 | 1,47 | S/ 2,25 |
| 3.1 TRAJES_HUALLAGA_ACOTADO | 93 | 13 467 | 1,85 | S/ 3,36 |
| 3.3 TRAJES_CHACARILLA_ACOTADO | 64 | 8 095 | 1,64 | **S/ 2,92** |
| 3.2 TRAJES_CHACARILLA_NOVIOS | 34 | 8 536 | 1,67 | S/ 5,49 |
| 3.4 TRAJES_CHACARILLA_PAPAS | 13 | 2 520 | 1,56 | S/ 5,41 |
| **Total leads** | **549** | | | ~S/ 1 381 |

Camisas cuadra con el S/ 1,81 que reporta Meta; trajes cuadra exacto con los S/ 755,69 de gasto total.

**HALLAZGO PRINCIPAL: cada zona vende un producto distinto, y julio ya lo respondió.** No hace falta esperar agosto para saberlo:
- **Camisas: Huallaga gana** (S/ 1,52 contra S/ 2,25), 32% más barato.
- **Trajes: Chacarilla gana** (S/ 2,92 contra S/ 3,36), 13% más barato.
- **Los conjuntos temáticos de trajes fueron los caros:** Novios S/ 5,49 y Papás S/ 5,41, o sea S/ 257 de julio a S/ 5,46 la conversación, más del triple del mejor conjunto. En agosto no se repiten y ese dinero va a los que funcionan.
- Orden de recorte si algún mes hay que ajustar: primero los temáticos, nunca camisas Huallaga.

**OBJETIVO VIGENTE: 588 conversaciones**, con costo objetivo de S/ 2,32. Cada campaña con el costo de su conjunto equivalente de julio: camisas Chacarilla 165 (S/ 2,25), camisas Huallaga 204 (S/ 1,52), trajes Chacarilla 127 (S/ 2,92), trajes Huallaga 92 (S/ 3,36). **Son +39 conversaciones que julio con S/ 18 menos**, y la ganancia sale íntegra de no repetir los dos temáticos. Hitos semanales acumulados: 133, 266, 398, 531, 588. Techos de alarma = el costo de julio de cada conjunto, con 10% de tolerancia por variación normal.

**CORRECCIÓN IMPORTANTE sobre la fase de aprendizaje:** en la versión previa advertí fuerte que los conjuntos no llegarían a 50 eventos por semana y que eso encarecería el costo. **La data de julio contradice esa alarma:** camisas Huallaga hizo 206 conversaciones en 31 días (46 por semana, bajo el umbral) con S/ 10 al día, y fue **el costo más bajo de toda la cuenta**. Los conjuntos de esta cuenta ya entregan bien por debajo del umbral, así que el aviso estaba sobredimensionado y se quitó del documento. La regla de las 50 es una guía, no una condición.

**Único punto de escalado con riesgo:** trajes Chacarilla pasa de S/ 6 a S/ 12 al día, el único que dobla presupuesto. Es donde el costo tiene más margen para moverse.

Siguen pendientes los tres puntos de decisión: los S/ 20 de la campaña de domingos (18 días, no 16), confirmar el costo por seguidor de S/ 0,6486, y que el alcance no tiene referencia hasta cerrar el primer mes.

### Cuadro final del cliente · VERSIÓN VIGENTE

Alessandro ajustó el cuadro y pidió: quitar el bloque de recomendaciones (ya las aplicó), quitar las columnas vacías de "Real" y "Costo real" del seguimiento, y cerrar con la inversión total incluyendo IGV y comisión bancaria. El documento va **al gerente del cliente**: es la etapa de "esto voy a gastar y esto espero lograr"; el avance real se presenta después, semana a semana.

**Cambios del cuadro contra la versión anterior:** meta de seguidores baja de 20 000 a **15 000** (restante 2 400, crecimiento 480/mes, **S/ 311,35** al mes en vez de S/ 959,99); las cuatro campañas de leads suben a **S/ 15 al día, S/ 465 cada una** (antes 12/12/10/10); la campaña de domingos sube a S/ 12 al día, S/ 192. **Total S/ 2 983,35**, verificado y exacto.

| Frente | Inversión | % |
|---|---|---|
| Leads (4 campañas a S/ 465) | S/ 1 860,00 | 62% |
| Alcance (Chacarilla 310, Huallaga 310, domingos 192) | S/ 812,00 | 27% |
| Seguidores IG | S/ 311,35 | 10% |

**OBJETIVO VIGENTE: 810 leads**, costo objetivo **S/ 2,30**. Por campaña, con el costo real de su conjunto de julio: camisas Chacarilla 207 (S/ 2,25), camisas Huallaga 306 (S/ 1,52), trajes Chacarilla 159 (S/ 2,92), trajes Huallaga 138 (S/ 3,36). Son **+261 leads que julio (+47,5%) con 34,6% más inversión**: crecen más rápido que el dinero porque no se repiten los conjuntos temáticos caros. Ruta semanal: 183, 366, 549, 732, 810.

**Cierre de inversión (bloque 05):** plataforma S/ 2 983,35 + IGV 18% S/ 537,00 = **S/ 3 520,35 facturado por Meta**. La comisión bancaria por pago al exterior está **pendiente del dato del cliente**: en el script hay una constante `COMISION_BANCO` (hoy `null`, muestra "Por confirmar"); poniendo la tasa (por ejemplo `0.035`) la fila y el total se calculan solos.

**Ajuste final (misma sesión):** Alessandro pidió **quitar la fila de comisión del banco** (queda fuera del documento) y **añadir el objetivo de seguidores hasta el cierre de diciembre**. El documento quedó en 6 bloques:

1. El plan (8 campañas, S/ 2 983,35)
2. El objetivo de leads (810)
3. El día a día (26,1 leads diarios)
4. Lo que julio ya respondió (zonas)
5. El objetivo de seguidores
6. La ruta semanal
7. La inversión (plataforma + IGV = S/ 3 520,35, sin banco)

**Bloque 03, el día a día:** 810 leads en 31 días son **26,1 al día y 183 a la semana**. Por campaña: camisas Chacarilla 6,7, camisas Huallaga 9,9, trajes Chacarilla 5,1, trajes Huallaga 4,5. Julio promedió 17,7 diarios, así que agosto son **+8,4 conversaciones más por día** entrando al WhatsApp. Es un dato operativo además de comercial: hay que poder responderlas.

**Rampa de seguidores, verificada y exacta:** de 12 600 hoy a **15 000 al cierre de diciembre**, sumando 480 al mes durante cinco meses (agosto a diciembre). Agosto cierra en **13 080**. Inversión S/ 311,35 al mes, **S/ 1 556,74** en total, que cuadra al céntimo con el cuadro del cliente. Crecimiento del 19%.

**Preguntas abiertas con Alessandro:**
1. **Campaña de domingos:** el cuadro presupuesta 16 días (4 de cada uno) pero agosto 2026 tiene 5 sábados y 5 domingos, o sea 18 días posibles. A S/ 12 serían S/ 216 y no S/ 192, y el total subiría a S/ 3 007,35. Puede estar bien si se programa a 16 días a propósito. Preguntado, sin respuesta todavía.
2. **Costo por seguidor de S/ 0,6486:** sigue sin verificar, la campaña de IG de julio medía visitas al perfil. Con la meta en 15 000 pesa poco (S/ 311,35 al mes), así que no bloquea.
3. **Tratamiento del IGV:** se presenta como 18% que Meta añade a la factura. Si la cuenta lo lleva por utilización de servicios de no domiciliados, el monto es el mismo pero cambia el momento de pago y el crédito fiscal. Preguntado, sin respuesta todavía.

## Sesión del 7 ago 2026 · elegancia tomada de Firenze

- **Cabecera maison:** a pedido de Alessandro se tomó la elegancia de firenze.pe. El cambio de mayor impacto: **logo centrado con el menú debajo** sobre banda azul sólida, más una **cinta superior** con los lemas de la casa. Encaja porque el logo de Andrés Vargas es un lockup vertical, que pedía centrado. La cabecera pasa a fila al hacer scroll y en móvil.
- **Efecto lateral bueno:** al ser la cabecera siempre azul sólida, desaparece la clase de bug del texto azul sobre fondo azul, y el escudo ya no necesita intercambiarse por JavaScript.
- **Bug corregido:** el botón "Agenda tu cita" del menú salía blanco sobre blanco. `.menu a` (0,1,1) le ganaba a `.btn-claro` (0,1,0). Resuelto con `.menu .btn-claro`.
- **Novios reestructurado** siguiendo el ritmo de Firenze: titular de promesa ("todo en un solo lugar"), qué incluye, tres pilares de la experiencia, calendario en cuatro pasos, cortejo y cierre. CTA repetido cuatro veces, como hace Firenze.
- **Locales:** se añade "atendemos previa cita", que es el patrón de Firenze y además es cierto aquí.
- **NO se copiaron imágenes de Firenze.** Sus fotos llevan cajas y etiquetas con el logo FIRENZE impreso, y además son material con derechos de un competidor directo. Se usan solo las fotos del propio cliente.

### Hero a sangre completa (misma sesión)

A pedido de Alessandro, el hero pasa de panel partido a **una sola imagen de ancho total**, como Firenze.

- **Problema resuelto:** las fotos de marca son verticales (3012×3307) y no se pueden recortar a panorámico sin cortar al modelo. La única horizontal era la de novios, pero encuadraba toda la marca como "novios". Se optó por recortar `portada.tif` conservando cabeza y torso: 1900×1008, 291 KB.
- **La composición manda:** el sujeto queda a la izquierda y el muro de piedra a la derecha, así que el texto va **a la derecha** y el velo oscurece por ese lado. No se espejó la foto para poner el sujeto a la derecha, porque el cruce de la solapa quedaría al revés y en una sastrería eso se nota.
- **La foto empieza debajo de la banda**, no detrás: si va detrás, el encabezado de 232px corta la cabeza del modelo. Se resolvió con la variable `--alto-cabecera`, que el script sincroniza con la altura real y que usan también las cabeceras de página interior.

### Reordenado el inicio y nueva página de Tiendas (misma sesión)

Alessandro preguntó si el orden del inicio estaba bien. Revisado, **no lo estaba**, por tres motivos:

1. **El producto aparecía en séptimo lugar.** Se veía filosofía, telas, cifras, clientes y el configurador antes de una sola prenda.
2. **El configurador iba antes que las colecciones**, o sea, se pedía diseñar una prenda antes de mostrar las prendas.
3. **Tres bandas oscuras seguidas** (azul, profundo, azul), un tramo largo sin respiro visual.

Orden nuevo, con el ritmo de fondos rebalanceado:

| # | Fondo | Sección |
|---|---|---|
| 1 | foto | Hero |
| 2 | papel | Colecciones (lo que confeccionamos) |
| 3 | nube | La casa (el oficio) |
| 4 | azul | Telas: la ventaja |
| 5 | profundo | Cifras |
| 6 | papel | Configurador |
| 7 | nube | Novios |
| 8 | azul | Proyectos |
| 9 | papel | Blog |
| 10 | azul | Visítanos |

También se quitó una repetición: el titular de "La casa" decía "Cuarenta y cuatro años tomando medidas" justo debajo de un hero que ya dice "44 años de oficio". Ahora es "El oficio, sin atajos".

**Nueva página Tiendas** (octava): las dos fichas con zona, dirección, qué encuentras en cada una y botones de Cómo llegar y WhatsApp, más un bloque de tres pasos sobre cómo es la visita. Enlazada desde el menú, el pie y el bloque "Visítanos" del inicio. El escudo va de marca de agua en cada ficha.

### Datos reales de tiendas (7 ago 2026, de Alessandro)

**Son TRES tiendas, no dos.** La web decía dos porque el documento original del cliente solo listaba dos direcciones.

| Tienda | Dirección | Horario |
|---|---|---|
| **Primavera** | Av. Primavera 252, Chacarilla, Santiago de Surco | Lun a Sáb 10 am a 8 pm · Dom 10 am a 4 pm |
| **Huallaga** | Jr. Huallaga 558 y 570, Cercado de Lima | Lun a Sáb 10 am a 8 pm · Dom 10 am a 4 pm |
| **Ucayali** | Jr. Ucayali 115 · 119 · 121, Cercado de Lima | Lun a Vie 10 am a 8 pm · **fin de semana por confirmar** |

**PENDIENTE:** el mensaje sobre Ucayali quedó cortado ("atiende en esos horarios de lunes a viernes pero los sábados."). No se inventó nada: la ficha muestra lunes a viernes confirmado y "Fin de semana · Consúltanos". Falta preguntar el horario de sábado y si abre domingo.

Se actualizaron todos los sitios que decían dos tiendas: la cifra del inicio (2 → 3), el titular "Dos tiendas en Lima" → "Tres", el pie, la meta descripción y la firma del hero.

**Fotos:** cada ficha lleva una foto general de prendas del cliente, no del local. Alessandro autorizó usar "una foto general". **Pedir fotos reales de cada tienda** para sustituirlas: en una página de tiendas, la foto del local es lo que genera confianza.

Las tres fichas salen de un solo arreglo `TIENDAS` en el script, que alimenta a la vez la sección del inicio y la página. Añadir una tienda es añadir un objeto.

**Bug corregido (tercera vez que aparece este patrón):** el escudo sobre la foto salía estirado porque `.tienda-foto img` (0,1,1) le gana a `.sello` (0,1,0). Regla general para este proyecto: **cuando haya dos imágenes dentro del mismo contenedor, nunca estilarlas con un selector de tipo `contenedor img`**; darle clase propia a cada una o scopear (`.tienda-foto img.sello`).

### Refinamiento visual (7 ago 2026)

Alessandro pidió que se viera más exclusivo y que la letra era grande.

- **Tipografía afinada en todo el sitio, 30 ajustes.** Criterio: más pequeña, más ligera y con más aire. Todo bajó entre 15 y 20 %, el cuerpo de 16 a 15.5px con interlínea 1.8, los titulares grandes a peso 200 y más tracking en los rótulos (0.34em a 0.42em). Las secciones ganaron aire. Detalle y regla en `DESIGN-SYSTEM.md`.
- **Iconos de trazo fino** en los tres pasos de la visita y en los canales de contacto. Dibujados a mano en SVG con `stroke-width: 1`, no de librería, para que el trazo pese lo mismo que los filetes del sistema.
- **Cierre rediseñado.** El bloque "¿Prefieres escribirnos antes?" era el más flojo de la página. Ahora es "¿Cómo te gustaría agendar?", sobre fotografía con velo azul denso, con dos tarjetas de canal (WhatsApp y correo) con icono, explicación y el dato. Se aplicó el mismo componente al cierre de Novios.
- **Experiencia de novios en Chacarilla.** Sección propia en la página de Novios con la dirección, los horarios y dos CTA, más un distintivo "Experiencia novios" sobre la foto de esa tienda en la página de Tiendas. Dato dado por Alessandro.

### Cabeceras interiores con fotografía (7 ago 2026)

Alessandro: "solo letras y el color azul no es muy llamativo, hazlo en todos". Las siete páginas interiores abrían con azul plano.

- Ahora **cada una tiene su propia fotografía de fondo** con velo direccional: fuerte donde va el texto, abierto a la derecha para que la imagen se vea. En móvil el velo pasa a vertical uniforme.
- Se afinó el velo en dos pasadas: la primera quedó demasiado densa y la foto casi no se leía, que era justo lo que Alessandro quería evitar.
- El distintivo de Chacarilla pasa a **"Única con experiencia de novios"**, texto de Alessandro.
- Se quitó la textura diagonal de las cabeceras interiores: con fotografía detrás competía y ensuciaba.

### Resumen de tiendas en la cabecera (7 ago 2026)

Alessandro notó que la cabecera de Tiendas tenía muy pocos datos. Era cierto: era la única con un botón suelto y mucho aire vacío.

Ahora lleva un **resumen de las tres tiendas** bajo un doble filete: zona, nombre, dirección corta y un enlace que baja a la ficha. Sale del mismo arreglo `TIENDAS`, así que no hay nada que mantener por duplicado. La de Chacarilla muestra "Única con experiencia de novios" en lugar de "Ver horarios".

**Dos bugs reales encontrados al probarlo:**

1. **Ids duplicados.** Como el mismo renderizador alimenta el inicio y la página, las fichas salían con el mismo `id` dos veces y `getElementById` devolvía la del inicio, que está oculta. Se resolvió buscando por índice dentro de `#tiendas-pagina`, sin ids.
2. **El desplazamiento no ocurría si la pestaña está oculta.** `scrollIntoView({behavior:'smooth'})` no hacía nada en el panel de previsualización. Investigado: el panel reporta `visibilityState: "hidden"` y `requestAnimationFrame` da **0 fotogramas**, así que ni el desplazamiento nativo ni una animación propia avanzan. Se escribió `desplazarA()` con animación propia y **salvaguarda: si `document.hidden` o hay movimiento reducido, salta directo a la posición**. Así la navegación funciona siempre, con o sin animación.

`desplazarA()` reemplaza también al `scrollIntoView` que usaba la navegación por ancla, que tenía el mismo problema latente.

### Horario rotulado, referencia y datos estructurados (7 ago 2026)

- **Rótulo "Horario de atención"** sobre la tabla de horarios de cada ficha. Antes las horas aparecían sueltas, sin decir qué eran.
- **Campo `ref`** para la referencia de ubicación de cada tienda, muy usada en Perú ("frente a", "a media cuadra de"). Está en la estructura y se pinta solo si tiene contenido, así que hoy no se muestra. **PENDIENTE: pedir las tres referencias al cliente.**
- **Datos estructurados Schema.org (`ClothingStore`)** para las tres tiendas, generados del mismo arreglo `TIENDAS` para que no puedan quedar desfasados. Incluyen dirección, distrito, teléfono, correo y **horario legible por buscadores** (`openingHoursSpecification`). Sirve para que Google muestre cada tienda con su horario en la búsqueda y en Maps.
  - Se añadieron campos explícitos `calle` y `distrito`. La primera versión los deducía troceando la dirección y fallaba en Primavera: ponía el distrito como "Lima" en vez de "Santiago de Surco".
  - Ucayali solo declara lunes a viernes, que es lo confirmado. Cuando llegue el horario de fin de semana hay que añadirlo en `aperturas`.

### Auditoría completa del sitio (7 ago 2026)

Alessandro pidió revisar que todo fuera acorde a lo pedido. Se auditó el sitio real en navegador, no de memoria. **Cinco defectos encontrados y corregidos:**

1. **El inicio no tenía `<h1>`.** La página más importante no declaraba encabezado principal: el slogan era un `<p>`. Ahora es `h1` y mantiene su aspecto (la clase gana en especificidad a la regla de encabezados). Las siete páginas interiores sí lo tenían.
2. **Salto de nivel en Telas:** h2 → h4 en los nombres de tela. Pasaron a h3.
3. **Salto de nivel en Blog:** h1 → h3. Se añadió el encabezado de sección "Los primeros artículos".
4. **42 imágenes sin carga diferida.** Ahora solo quedan dos sin ella, y a propósito: el hero y el escudo de la cabecera, que están sobre el pliegue. En una SPA con las ocho páginas en el DOM esto importa: sin `lazy`, el visitante descarga imágenes de páginas que quizá no visite.
5. **Blog y Corporativo no tenían salida a WhatsApp.** Blog no tenía ninguna vía de contacto y Corporativo solo correo. Ahora Blog cierra con "Pregúntale al sastre" y Corporativo ofrece WhatsApp junto al correo.

Verificado tras el arreglo: las ocho páginas con exactamente un `h1`, cero saltos de nivel, cero ids duplicados, cero imágenes sin `alt` y todas con salida a WhatsApp.

### Página "A medida" (7 ago 2026)

Cerraba el único hueco real frente al pedido original: cuando Alessandro dio Firenze como referencia nombró seis secciones, entre ellas **Hecho a medida**, y era la que faltaba. Existían Trajes y Camisas por separado, pero no el concepto paraguas que explica el proceso como experiencia.

**Estructura:** cabecera con foto · qué cambia cuando es a medida (tres pilares con iconos) · las dos prendas, que enrutan a Trajes y Camisas · el proceso en cuatro pasos, común a ambas · la tela como primera decisión · cierre hacia el configurador.

**Reorganización del menú:** "A medida" **sustituye** a Trajes y Camisas, que pasan a colgar de ella. El menú baja de 8 a 7 ítems y se parece más al de Firenze (Shop, Made to Measure, Novios, Club, Blog, Contacto).

- Trajes y Camisas siguen existiendo como páginas y son accesibles desde "A medida", desde las tarjetas de Colecciones del inicio y desde el pie.
- Sus migas ahora dicen `Inicio · A medida · Trajes`.
- Al estar en Trajes o Camisas, el menú marca **"A medida"** como activo (mapa `padre` en `ir()`). Sin eso, no se iluminaría ningún ítem y el usuario perdería la referencia de dónde está.

### Marcas de tela y cierre de Corporativo (7 ago 2026)

**Marcas de tela.** Alessandro envió los logos de cuatro casas: Vitale Barberis Canonico, Reda, Thomas Mason y Barrington. El bloque `#bloque-marcas`, que llevaba oculto desde que se creó, ya está activo.

- **Los cuatro logos ya están puestos** (`assets/tela-vbc.png`, `tela-reda.png`, `tela-thomasmason.png`, `tela-barrington.png`). El componente acepta logo o nombre: si hay archivo muestra la imagen, si no, el nombre en la tipografía de la casa.
- **De dónde salieron:** Alessandro los pegó en el chat, pero una imagen pegada en el chat no llega al disco, así que no se podían copiar a `assets/`. Los había descargado a `~/Downloads` con nombres genéricos (`images.png`, `images (1).png`, `images (2).png`, `THOMAS.webp`) y desde ahí se procesaron. **Para la próxima: basta con que los deje en Descargas o el Escritorio.**
- **Tratamiento:** los archivos vienen con fondo blanco o crema, no transparente. Se resuelve con `mix-blend-mode: multiply` (funde el fondo con la tarjeta) más `filter: brightness(1.07)`, que empuja el crema de Thomas Mason hasta blanco sin oscurecer perceptiblemente las marcas, que son casi negras. Se recortaron los márgenes sobrantes de Barrington, Reda y Thomas Mason para que todos pesen visualmente parecido.
- Orígenes puestos solo donde son verificables y aparecen en el propio logo: VBC (Italia, 1663), Reda (Italia, 1865), Thomas Mason (Inglaterra, 1796). **Barrington va sin origen porque no está confirmado.**
- Copys actualizados en Telas, en el bloque de marcas y en el inicio: ahora dicen explícitamente **tela nacional, italiana e inglesa**, no solo "nacionales e importadas".

### Sección "Las casas" con slider (7 ago 2026)

Alessandro sumó **Albini** y **Brunello Cucinelli** (archivos en Descargas: `images.jpeg` y `851bef...jpg`) y pidió slider, una sección que cuente todas las marcas, y **destacar Barrington**.

**Estructura en la página Telas:**
1. `Las casas · Con quién trabajamos` con **slider continuo** de los seis logos. La pista se duplica para que el bucle no dé saltos, se pausa al pasar el ratón y respeta `prefers-reduced-motion`. Bordes con degradado para que los logos entren y salgan sin corte seco.
2. **Barrington destacado**, bloque propio: placa con doble filete interior (el motivo del escudo), sello "Distribuidor oficial" y tres puntos sobre lo que aporta la relación. Sale de `CASAS` con `destacada: true`, que además lo excluye de la rejilla de abajo para no repetirlo.
3. `Las demás casas`: ficha por casa con logo, origen, año y una línea de detalle.

**Sobre el contenido de cada casa:** solo se escribió lo verificable (VBC 1663 Biella, Reda 1865 lana merino, Albini 1876 camisería, Thomas Mason 1796 y su pertenencia al grupo Albini, Brunello Cucinelli de Solomeo y el cachemir). **De Barrington no se inventó historia**: el texto habla de lo que Alessandro sí confirmó, que la relación es la más cercana y que son distribuidores oficiales. Falta pedirle los datos reales (desde cuándo, si hay exclusividad, origen de la casa).

**Fondos de los logos:** solo VBC y Barrington venían en blanco puro; Albini llegaba a `#ECECEC` por compresión JPEG, y se veía un recuadro gris. Se subió el filtro a `brightness(1.13)`: como el filtro es multiplicativo, 236 × 1,13 satura en blanco mientras el negro de la marca sigue en negro. Combinado con `mix-blend-mode: multiply` los seis quedan sin recuadro.

**Ajuste del slider (mismo día):** Alessandro pidió logos más grandes y que no se cortaran. Dos correcciones:

- **El corte** venía de que el degradado del borde (110px) era más estrecho que un logo (hasta 250px), así que el logo llegaba al filo antes de haberse desvanecido. El degradado pasa a `clamp(110px, 18vw, 300px)`, siempre más ancho que el logo mayor. Altura de logo de 48 a 76px.
- **Volvieron los recuadros blancos** al agrandarlos. Causa: `.slider-pista` lleva `animation`, y eso **crea un contexto de apilado que aísla el `mix-blend-mode`**: los logos dejaban de mezclarse con el fondo de la sección y se mezclaban con el de la pista, que era transparente. Se resuelve dándole a la pista el mismo fondo que la sección. **Regla para el futuro:** `mix-blend-mode` no atraviesa un contexto de apilado; si el padre anima, transforma o tiene opacidad, hay que darle fondo explícito.

**Limpieza:** el componente anterior (`.marca-tela`, `.marcas-tela`, `.marca-logo`) quedó huérfano al sustituirlo y se eliminó su CSS, 1.323 caracteres.

**OJO, CONTRADICCIÓN PENDIENTE:** Barrington aparecía como **proyecto/cliente** en la sección de Proyectos ("Marca · Proyecto de confección para la marca"), por indicación anterior de Alessandro, y ahora llega como **marca de tela**. Las dos cosas no encajan. Hay que confirmar cuál es y corregir la que sobre.

**Cierre de Corporativo.** El aviso de "Cotización a medida" quedaba como una caja suelta en medio de mucho espacio vacío, señalado por Alessandro. Se sustituyó por un cierre con fotografía y las dos tarjetas de canal, igual que en Blog, Novios, Tiendas y A medida. Ya no queda ningún `.aviso` huérfano en esa página.

**Bug de rejilla:** el bloque de marcas usaba `repeat(auto-fill, ...)`, que dejaba columnas vacías a la derecha con solo cuatro marcas. Con `auto-fit` las columnas se reparten el ancho.

### Formulario de consulta y fin del azul plano (7 ago 2026)

**Fuera el muestrario de colores.** Alessandro lo pidió quitar. Con él se fueron los filtros por familia y el código genérico de `[data-filtro-grupo]`, que ya no tenía usuarios.

**En su lugar, formulario de consulta de tela** (`#consulta-tela`): nombre, teléfono o correo, selector de casa (se llena solo desde `CASAS`) y un mensaje **predeterminado que cambia según la casa elegida**. Si el visitante edita el mensaje, deja de reescribirse.

- **No hay backend, y no hace falta:** el formulario compone el texto y lo abre en **WhatsApp** o en el **correo**. Es lo que de verdad usa este cliente y no exige servidor, credenciales ni servicio de terceros. Si algún día se quiere recibir los envíos en una bandeja, habría que montar una función de Pages más un servicio de correo.
- Validación mínima: sin nombre no deja enviar, porque sin nombre no se puede responder.

**Fin de las bandas de azul plano.** Alessandro: "no quiero estas partes solo de azul, que la web se sienta viva". Las **nueve** secciones azules planas pasan a llevar fotografía de fondo con velo.

- Se resolvió con una clase `.con-foto` y una variable `--foto` por sección, en vez de reestructurar el HTML de cada una: `background-image: linear-gradient(velo), var(--foto)`. Añadir foto a una sección nueva es una clase y un `style`.
- El velo va al 0,93 para que el texto siga legible; existe `.velo-suave` al 0,88 para secciones con poco texto.

### HALLAZGO DE SEGURIDAD: los documentos internos estaban públicos

Cloudflare Pages despliega la raíz del repo, así que `NOTAS.md`, `CLAUDE.md` y `DESIGN-SYSTEM.md` respondían **HTTP 200** en `andres-vargas-web.pages.dev`. Cualquiera con la URL podía leer las notas internas del proyecto, incluida la nota sobre los datos que se inventaron en la primera versión.

**`_redirects` NO sirve para esto.** Se probó primero y falló: en Cloudflare Pages los archivos estáticos tienen prioridad sobre las reglas de redirección, así que los `.md` se seguían sirviendo con 200.

Resuelto con `functions/_middleware.js`, que sí se ejecuta antes que el archivo estático. Bloquea los `.md` de raíz, `/pauta/*` y `/.git/*`. Verificado en producción: los documentos dan 404 y la web sigue en 200.

**Dos cosas para no olvidar:** cualquier archivo nuevo en la raíz del repo es público por defecto, así que si se agrega documentación hay que sumarla al middleware. Y `/pauta/*` ya está bloqueado de antemano, así que esa carpeta se puede commitear sin quedar expuesta (aunque sigue siendo mejor decidir su destino final).

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
   - **FOTOS DE LOS TRES LOCALES (prioridad, decidida por Alessandro el 7 ago 2026).** Es lo que más confianza genera en la página de Tiendas. Especificaciones para pedirlas:
     - **Horizontales**, se recortan a **16:10**. Nada vertical.
     - Mínimo **1600 px de ancho**; sirve foto de celular moderno con buena luz.
     - Una por tienda: **Primavera (Chacarilla), Huallaga y Ucayali**.
     - Preferible **fachada con el letrero visible**, para que alguien la reconozca al llegar. Si el interior se ve mejor, sirve: mostrador, muestrario de telas o el taller.
     - Luz de día, sin flash, cámara a la altura del pecho y de frente. Evitar contraluz y autos delante.
     - El recorte deja libre la esquina superior derecha (escudo) e inferior izquierda (nombre de la zona): no poner ahí lo importante.
     - **Cambio en la web: una línea por tienda**, el campo `foto` del arreglo `TIENDAS`. Yo las optimizo a sRGB y las meto en `assets/`.
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

### Hero convertido en carrusel de banners (7 ago 2026)

El hero pasa de una sola imagen a tres banners que se cruzan por opacidad.
Autoavance de 6,8 s; se detiene al pasar el mouse, al recibir foco de teclado
y cuando el hero sale de pantalla (incluido el salto a otra página, que lo
deja en `display:none`). Flechas, barras y deslizamiento táctil. El banner
que no se ve queda con `inert`, así que sus botones no entran al tabulador.

Los tres textos salen tal cual de sus páginas: nada escrito solo para el hero.

1. Sastrería a medida · Lima → eslogan de marca (lleva el único `<h1>`)
2. Experiencia novio → `novios-trio-wide.jpg`
3. Distribuidores oficiales → `editorial-duo.jpg`

**Por qué solo tres.** De todo el material, únicamente `hero.jpg` (1900 px) y
`novios-trio-wide.jpg` (1300 px) sirven a sangre completa. `editorial-duo.jpg`
es vertical (1275×1400) y ya se recorta fuerte; las `traje-*.jpg` miden 562 px
de ancho y en un banner se verían borrosas. **No hay banner de Corporativo por
falta de foto**, no por decisión de diseño.

Para añadir banners hace falta foto **horizontal, mínimo 2000 px de ancho**,
con espacio vacío o de tono uniforme en el tercio derecho (ahí va el texto).
Pendientes: Corporativo (equipo o directivos), Telas (tejidos o el mostrador),
Tiendas (fachada).

**Colisión resuelta.** El botón flotante de WhatsApp ocupa 84 px desde el borde
derecho. El margen del contenedor (1280 px) solo lo libra a partir de 1352 px
de ventana; por debajo el mando se aparta 100 px. En táctil las flechas se
ocultan —se pasa deslizando— y las barras se van a la izquierda.

### Inicio orientado a conversión + SEO/GEO (8 ago 2026)

**Término principal.** El título abría con la marca. En Perú la búsqueda real
es «terno», no «traje», así que ahora abre con *Ternos y Trajes a Medida en
Lima* y deja la marca al final. Mismo criterio en los H2 del inicio.

**FAQ.** Siete preguntas con `FAQPage` en JSON-LD **generado desde el propio
HTML**, para que el dato estructurado no pueda separarse de lo que lee la
persona. Son las que llegan por WhatsApp: dónde están, horarios, qué
confeccionan, telas, novios, medios de pago y cómo agendar. Esto es lo que
citan los asistentes de IA cuando alguien pregunta «sastrería en Lima».

**Conversión.** Tarjetas de colección con texto sobre la foto (unifica los
fondos dispares de las fotos de producto y ocupa la mitad de alto), franja de
medios de pago arriba —la objeción del precio llega antes que el interés—, dos
banners de salida a Telas y Novios, y los enlaces flojos de Novios y
Corporativo convertidos en botones con mensaje de WhatsApp ya redactado.

**PENDIENTE · logos de empresas.** La sección existe y se alimenta del array
`EMPRESAS`, pero está **oculta** porque no hay ni un archivo de logo. Sin
archivo no se dibuja un rótulo tipográfico que parezca su marca.

Dos cosas que hay que resolver antes de publicarla:

1. **Los archivos.** PNG con fondo transparente o SVG, del logo oficial.
2. **La lista exacta.** El pedido decía «empresas como BCP, BBVA, Interbank,
   Universitario, e-Qapla y otros». «Como» no es una lista cerrada, y publicar
   la marca de un banco como cliente sin serlo es un problema legal para el
   cliente, no un detalle de diseño. Hace falta confirmación explícita de
   cuáles sí, y ojo con los contratos: algunas empresas exigen permiso escrito
   para usar su logo como referencia comercial.

### Una URL por sección (8 ago 2026) · el cambio de más peso para SEO

La web es de una sola página. Google solo puede posicionar una URL, así que
todo el contenido de Telas, Novios o Camisas no competía por nada: existía,
pero no tenía dirección propia a la que mandar tráfico.

Ahora cada sección tiene la suya y **el HTML llega ya con su `<title>`,
descripción y canonical reescritos en el servidor** con `HTMLRewriter`, en
`functions/_middleware.js`. Hacerlo ahí y no en el navegador importa: no
depende de que el rastreador ejecute JavaScript. El middleware marca además
`data-ruta` en el `<body>` y el script abre esa sección al cargar; el botón
«atrás» funciona vía `popstate`.

| Ruta | Sección |
|---|---|
| `/` | inicio |
| `/a-medida` | medida |
| `/ternos-a-medida` | trajes |
| `/camisas-a-medida` | camisas |
| `/telas` | telas |
| `/trajes-de-novio` | novios |
| `/corporativo` | corporativo |
| `/tiendas` | tiendas |
| `/blog` | blog |

**Dos defectos que aparecieron al revisar esto:**

1. `/robots.txt` devolvía la portada entera con `content-type: text/html`.
   Cualquier rastreador pidiendo robots.txt recibía HTML. Ya hay `robots.txt`
   y `sitemap.xml` reales.
2. Cualquier ruta inventada respondía **200 con la portada completa**:
   contenido duplicado en infinitas direcciones, que perjudica más que no
   tener rutas. Ahora es 404. `/telas/` e `/index.html` redirigen 301.

**Textos.** Los ocho H1 interiores eran etiquetas internas («Telas»,
«Camisas», «Corporativo»). Reescritos con término + ciudad. La frase emocional
de Novios baja al primer párrafo en vez de perderse.

**Fotos.** Las cuatro `traje-*.jpg` traían franjas blancas de 54 a 75 px a cada
lado —se veían como un marco sucio dentro de las tarjetas—. Recortadas en
origen con `sips`, detectando las bandas con un escaneo de columnas sobre BMP
(en esta máquina no hay PIL).

**Recomendación no aplicada:** en Perú «casimir» es un término de búsqueda muy
fuerte para tela de terno. No lo metí porque afirmar categorías de producto es
decisión del cliente, no mía. Si Andrés Vargas confirma que vende casimir,
entra en el H1 de Telas y en la FAQ.

### Segunda vuelta de SEO/GEO (8 ago 2026)

**El problema de fondo, que la primera vuelta no resolvió.** Dar una URL a cada
sección no bastaba: las nueve seguían sirviendo el MISMO HTML de 142 KB con las
nueve secciones dentro, y solo cambiaba un atributo. Para un buscador eran nueve
páginas casi idénticas. Y para los rastreadores de IA —que en su mayoría **no
ejecutan JavaScript**— preguntar por «trajes de novio en Lima» devolvía una
página que hablaba sobre todo de otra cosa.

Ahora el middleware **poda** las secciones que no son de la URL y pone `activa`
en la que queda (`.pagina` es `display:none` por defecto: servir el contenido
oculto es justo lo que los buscadores descuentan). Cada ruta pasa de 151 KB a
~100 KB y dice solo lo suyo.

Como consecuencia, los 33 enlaces internos llevan `href` real y la navegación es
una carga normal. `ir()` cae a `location.href` si la sección pedida no está en el
documento, así que los pocos elementos sin `href` siguen funcionando.

**Datos estructurados: estaban generados por JavaScript.** O sea, invisibles
justo para quien más los aprovecha. Ahora van escritos en el HTML:
`Organization` y `WebSite` (que no existían), las tres `ClothingStore` y
`BreadcrumbList` por ruta. El `FAQPage` va **dentro** de la sección de inicio
para que la poda se lo lleve: declararlo en una página que no muestra las
preguntas es dato inválido.

Como escribirlos a mano abre la puerta al desfase, hay una comprobación que
avisa por consola si las direcciones del JSON-LD dejan de coincidir con el
arreglo `TIENDAS`.

Fuera `priceRange: "$$$"`: Google lo muestra como indicador de precio y la regla
del cliente es no publicar ninguno.

**Compartir enlaces estaba roto.** `og:image` era una ruta relativa y ni WhatsApp
ni Facebook las resuelven, así que el enlace se compartía sin imagen. Ahora es
absoluta, con tamaño y alt, y **cada ruta tiene su propia foto**. Añadidas las
etiquetas de Twitter, que no había.

**Rendimiento.** Las 66 imágenes locales llevan `width`/`height` —evita el salto
de maquetado que Google mide como CLS— y la foto del héroe se precarga.

**El logo navegaba por JavaScript**, así que el enlace interno más repetido del
sitio no existía para un rastreador. Ahora es `<a href="/">`. Las diez migas de
pan, igual.

### Revisión del cliente (8 ago 2026) · «revision de la web AV.docx»

**Tiendas: eran seis, no tres.** Cada número de Ucayali y de Huallaga es una
tienda distinta, no una sola con varias puertas. Cinco en el Cercado de Lima
(Ucayali 115, 119 y 121; Huallaga 558 y 570) y una en Surco.

Horarios confirmados: **solo Huallaga 558 abre domingo** (10 am a 4 pm), y las
de **Ucayali parten la jornada**: 10 am a 1 pm y 2 pm a 8 pm. El resto, lunes a
sábado de 10 am a 8 pm.

**PENDIENTE:** el sábado de las tiendas de Ucayali. Sigue como «Consúltanos» —
es el mismo dato que quedó cortado en julio— y no se rellena con un horario
plausible.

**Novios.** Deja de anclarse a «Chacarilla»: ahora es «nuestra tienda de Surco»
y el foco pasa a los detalles de ese día. Fuera la frase de las fotos que se
van a tomar en la vida. «Chacarilla» solo se mantiene dentro de la dirección
postal, que es el nombre real de la zona.

**Telas.** La lista es la que pidió el cliente: Barrington, Vitale Barberis,
Albini, Thomas Mason, Brunello Cucinelli y **Creditex**. Sale **Reda**.

**Configurador.** «Diseña tu camisa» abría con Traje puesto —el botón prometía
una prenda y aparecía otra—. Ahora la prenda viaja en la URL (`?prenda=camisa`).

**El prototipo del saco** parecía un abrigo: sin línea de hombro, largo hasta
medio muslo, solapa indistinguible del cuerpo y botones bajo la cintura.
Redibujado con largo de saco, hombro marcado, delanteros abiertos bajo el
botón, bolsillos con tapa, botones de puño y solapa con filo claro para que se
lea sobre cualquier tela. Las costuras van en negro translúcido, así funcionan
sobre cualquier color sin tener que repintarse.

**Correo:** `ventas@sastreriaandresvargas.pe`. Ojo: el dominio de la marca es
**sastreriaandresvargas.pe**, no andresvargas.pe. Corrige la recomendación
anterior sobre el dominio propio.

**Catálogo de modelos en PDF.** El bloque de descarga ya está en Telas, oculto
hasta que exista `assets/catalogo-telas.pdf`. Se comprueba con una petición
HEAD antes de mostrar el botón: un enlace de descarga a un 404 es peor que no
tenerlo.

**PENDIENTE de archivos del cliente:**
1. Foto enfocada en camisa (hoy Camisas usa una foto de saco, `traje-gris.jpg`).
2. Logo de Creditex.
3. El PDF del catálogo de modelos.
4. Los logos de empresas, con la lista confirmada.
