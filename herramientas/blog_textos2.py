# -*- coding: utf-8 -*-
"""Seis artículos más, escritos para búsquedas donde hoy no aparecemos.

Reglas heredadas del primer lote, y una nueva:
  · Nada de plazos, cifras ni casos que la web no pueda sostener.
  · Ningún superlativo comparativo sin prueba. «Distribuidor oficial» se puede
    decir porque la web ya lo declara y las casas son verificables; «el más
    grande» no, porque nadie lo ha medido y en Perú una afirmación objetiva sin
    sustento la sanciona Indecopi (D. L. 1044).
  · Los horarios y las direcciones salen del JSON-LD de las seis tiendas, no de
    lo que uno recuerda. Solo Huallaga 558 abre domingo.
"""

# ------------------------------------------------------------------------ 7
A7 = {
 'slug':'camisa-a-medida-lima', 'pag':'art-camisa', 'cat':'Guías',
 'h1':'Camisa a medida: el cuello, el puño y por qué el patrón lo decide todo',
 'titulo':'Camisa a Medida en Lima: Cuello, Puño y Patrón | Andrés Vargas',
 'desc':'Qué se decide en una camisa a medida y qué no se corrige después: el cuello, el puño, la caída del cuerpo y la tela. Guía de un sastre de Lima.',
 'img':'/assets/camisa-hero.jpg', 'w':1200, 'h':2153,
 'alt':'Camisa a medida de Andrés Vargas Sastrería',
 'lead':'La camisa es la prenda que toca la piel todo el día y la que más se nota cuando no calza: si el cuello aprieta, se ve; si el hombro sobra, se ve. Y a diferencia del saco, aquí casi nada se arregla después.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué se decide primero?</h2>
<p class="lead">El cuello, siempre. Es lo primero que mira quien te habla y lo que fija el carácter de la camisa entera. Un cuello italiano, con las puntas abiertas, pide corbata y nudo con cuerpo; uno button-down se sostiene solo y admite ir sin corbata sin verse desarmado; el mao prescinde de la corbata por definición. Elegir mal aquí no se corrige: el cuello no se cambia sin rehacer la camisa.</p>
<p class="lead">Después viene el puño. Simple para el día a día, doble si vas a usar gemelos. Y aquí hay un detalle que casi nadie pregunta y que se nota todos los días: cuánto puño quieres que asome bajo la manga del saco. Un centímetro y medio es lo habitual, pero eso depende de tus brazos, no de una tabla.</p>
%(FIG1)s

<h2 class="t-xl">¿Por qué el patrón propio cambia tanto?</h2>
<p class="lead">Una camisa de talla parte de un cuerpo promedio que no existe. Si tienes hombros anchos y cintura estrecha, la talla que te cierra en el cuello te sobra en el torso; si es al revés, te queda justa donde no debe. Cortar sobre tus medidas resuelve las dos cosas a la vez, porque el cuello y el cuerpo dejan de estar atados a la misma talla.</p>
<p class="lead">Lo que más se agradece con el tiempo no es el largo ni el ancho, sino la sisa: dónde nace la manga. Bien puesta, puedes levantar el brazo sin que la camisa se salga del pantalón. Es la diferencia que se siente a las cuatro de la tarde, no en el probador.</p>

<h2 class="t-xl">¿Qué tela conviene en Lima?</h2>
<p class="lead">El clima de Lima es húmedo casi todo el año y eso pesa más que la temperatura. Un popelín de hilo fino respira y se plancha limpio; un óxford tiene más cuerpo y perdona mejor el uso diario; el lino es fresquísimo y se arruga, y hay que aceptarlo de entrada o no elegirlo.</p>
<p class="lead">Trabajamos con casas nacionales e importadas: %(CREDITEX)s del Perú, y %(ALBINI)s y %(THOMASMASON)s, dos de las camiserías con más historia de Europa. Tratamos directo con ellas, así que la tela llega a tu camisa sin intermediarios. Cuál te conviene depende de para qué la quieres, y eso se ve mejor con la tela en la mano que en una pantalla.</p>
%(FIG2)s

<h2 class="t-xl">¿Cuántas camisas tiene sentido pedir de una vez?</h2>
<p class="lead">Si es la primera, una. El patrón se afina con la primera puesta: hay ajustes que solo aparecen cuando la camisa ha pasado un día entero contigo. Una vez que el patrón está bien, repetirlo es rápido y ahí sí tiene sentido pedir varias, porque el trabajo de medida ya está hecho.</p>
<p class="lead">Ese patrón queda guardado con tu nombre. Volver a pedir no vuelve a empezar de cero.</p>

<h2 class="t-xl">¿Y si ya tengo una camisa que me queda bien?</h2>
<p class="lead">Tráela. Es la referencia más útil que existe, mejor que cualquier descripción: nos dice qué te gusta de cómo cae, y también qué corregir. Lo mismo vale al revés: si hay una que te incomoda, tráela también y te decimos exactamente dónde está el problema.</p>
<p class="lead">Puedes verlo en cualquiera de nuestras <a href="/tiendas" data-ir="tiendas">seis tiendas de Lima</a>, o empezar por las <a href="/camisas-a-medida" data-ir="camisas">camisas a medida</a> para ver las opciones de cuello y puño con foto.</p>
''',
 'faq':[
  ('¿Cuánto tarda una camisa a medida?','Depende de la carga del taller y de la tela elegida. Escríbenos con lo que necesitas y te damos un plazo concreto antes de empezar, no una estimación genérica.'),
  ('¿Qué cuello me conviene si uso corbata todos los días?','El italiano o el semi-italiano: las puntas abiertas dejan sitio al nudo y enmarcan mejor la corbata. El button-down funciona mejor sin corbata o con nudos pequeños.'),
  ('¿Se puede arreglar una camisa que quedó ancha?','Se puede entrar de costados y estrechar la manga, pero el cuello y la sisa no se mueven sin rehacer la prenda. Por eso conviene acertar en la primera medida.'),
  ('¿Puedo llevar mi propia tela?','Consúltanos antes de comprarla. No toda tela sirve para camisa: el peso, la torsión del hilo y el ancho del rollo condicionan el corte.'),
 ],
 'wa':'Hola%2C%20quiero%20una%20camisa%20a%20medida.',
 'rel':[('/camisas-a-medida','Camisas a medida'),('/tiendas','Las seis tiendas'),('/blog/primer-terno-a-medida','Tu primer terno')],
 'fig':[('/assets/camisa-cuellos.jpg',1200,800,'Tipos de cuello de camisa a medida','El cuello es lo primero que se decide y lo único que no se corrige después.'),
        ('/assets/camisa-detalle.jpg',632,421,'Detalle de puño de camisa a medida','Cuánto puño asoma bajo la manga del saco depende de tus brazos, no de una tabla.')],
}

# ------------------------------------------------------------------------ 8
A8 = {
 'slug':'telas-italianas-en-lima', 'pag':'art-italianas', 'cat':'Telas',
 'h1':'Qué cambia una tela italiana en un terno',
 'titulo':'Telas Italianas para Terno en Lima | Andrés Vargas Sastrería',
 'desc':'Vitale Barberis Canonico, Albini y Thomas Mason: qué distingue a una tela italiana, cuándo vale la pena y cuándo no. Distribuidores oficiales en Lima.',
 'img':'/assets/editorial/ed-macro-orillo.jpg', 'w':1160, 'h':1500,
 'alt':'Orillo de una tela italiana para terno a medida',
 'lead':'«Italiana» se usa como sinónimo de buena y no es tan simple. Lo que cambia de verdad está en el hilo, en la torsión y en el acabado, y hay encargos donde una tela italiana es la decisión correcta y otros donde es dinero mal puesto.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué hace distinta a una tela italiana?</h2>
<p class="lead">No el país, sino lo que el país acumuló. Biella, al norte de Italia, lleva siglos hilando lana y eso se traduce en dos cosas concretas: hilos muy finos hilados con una regularidad difícil de igualar, y acabados que dejan la tela con caída sin quitarle recuperación. Una lana Super 130s italiana bien acabada cae como si pesara menos de lo que pesa y vuelve a su sitio al colgarla.</p>
<p class="lead">%(VBC)s hila en Biella desde 1663 y es la referencia en tejido de lana para sastrería. En camisería, %(ALBINI)s y %(THOMASMASON)s trabajan algodones de hilo altísimo con la misma lógica. Somos distribuidores oficiales de las tres, así que tratamos directo con ellas.</p>
%(FIG1)s

<h2 class="t-xl">¿Cuándo vale la pena y cuándo no?</h2>
<p class="lead">Vale la pena cuando la prenda va a lucirse: un terno de gala, el traje de novio, el saco con el que te presentas a algo que importa. Ahí la caída y el brillo apagado de una lana fina se ven a metro y medio de distancia.</p>
<p class="lead">No vale la pena si el terno va a salir de casa cuatro o cinco días por semana con maletín al hombro. Un hilo muy fino es más delicado por definición: brilla antes en los codos y en el asiento. Para eso conviene un peso medio y un tejido más cerrado, y ahí las telas nacionales compiten de igual a igual. Lo desarrollamos en <a href="/blog/tela-nacional-o-importada" data-ir="art-nacional-importada">tela nacional o importada</a>.</p>

<h2 class="t-xl">¿Qué significa el número de la tela?</h2>
<p class="lead">El Super 100s, 120s o 140s mide la finura del hilo, no la calidad de la prenda. A más número, hilo más fino: más caída, más tacto y menos resistencia al roce. Un Super 140s no es «mejor» que un Super 100s; es distinto, y sirve para otra cosa.</p>
<p class="lead">La %(IWTO)s publica los estándares del sector si quieres el detalle técnico. Nosotros lo resumimos así: del 100s al 120s, para llevar; del 130s en adelante, para lucir. Tenemos las tres gradaciones en <a href="/catalogo-de-telas" data-ir="catalogo">el catálogo</a>, con el orillo y el tejido de cada una.</p>
%(FIG2)s

<h2 class="t-xl">¿Cómo se reconoce una tela italiana de verdad?</h2>
<p class="lead">Por el orillo. Las casas serias tejen su nombre en el borde del rollo, y ese orillo viaja con la tela hasta el taller. Si nadie te lo puede mostrar, la pregunta se responde sola.</p>
<p class="lead">Pídelo. En cualquiera de nuestras <a href="/tiendas" data-ir="tiendas">tiendas</a> te enseñamos el rollo con el orillo a la vista, no una muestra suelta sin identificación.</p>

<h2 class="t-xl">¿Y el clima de Lima?</h2>
<p class="lead">Pesa más de lo que la gente cree. La humedad alta durante buena parte del año castiga los hilos muy finos y agradece los tejidos con algo más de cuerpo. Una lana italiana de peso medio con acabado seco se comporta muy bien aquí; una tela de verano europea pensada para calor seco, bastante peor.</p>
<p class="lead">Es la clase de detalle que no sale en ningún catálogo y que solo se aprende cosiendo en esta ciudad.</p>
''',
 'faq':[
  ('¿Una tela italiana siempre es mejor?','No. Es distinta. Para lucir, la caída de un hilo fino italiano es difícil de igualar; para uso diario intensivo, un peso medio más cerrado aguanta mejor, y ahí la tela nacional compite de igual a igual.'),
  ('¿Qué quiere decir Super 120s?','Es una medida de la finura del hilo, no de la calidad de la prenda. A más número, hilo más fino: más caída y menos resistencia al roce.'),
  ('¿Son ustedes distribuidores oficiales?','Sí, de telas nacionales e importadas: Barrington y Creditex del Perú, y Vitale Barberis Canonico, Albini y Thomas Mason de Italia e Inglaterra. Tratamos directo con las casas.'),
  ('¿Cómo compruebo el origen de una tela?','Por el orillo del rollo, donde la casa teje su nombre. Pide verlo antes de decidir.'),
 ],
 'wa':'Hola%2C%20quiero%20ver%20telas%20italianas%20para%20un%20terno.',
 'rel':[('/catalogo-de-telas','El catálogo'),('/blog/tela-nacional-o-importada','Nacional o importada'),('/telas','Las casas')],
 'fig':[('/assets/editorial/ed-macro-super100.jpg',1050,1500,'Macro del tejido de una lana Super 100s','El número mide la finura del hilo, no la calidad de la prenda.'),
        ('/assets/editorial/ed-macro-cuadros.jpg',1050,1500,'Macro de una tela de cuadros para sastrería','Del 100s al 120s, para llevar. Del 130s en adelante, para lucir.')],
}

# ------------------------------------------------------------------------ 9
A9 = {
 'slug':'telas-barrington-muestrario-completo', 'pag':'art-barrington', 'cat':'Telas',
 'h1':'El muestrario completo de Barrington, tela por tela',
 'titulo':'Telas Barrington en Lima: Muestrario Completo | Andrés Vargas',
 'desc':'Somos distribuidores oficiales de Barrington y publicamos su muestrario entero: 483 telas con código, composición, gramaje y color, filtrables desde la web.',
 'img':'/assets/editorial/ed-macro-cuadros.jpg', 'w':1050, 'h':1500,
 'alt':'Macro de una tela de Barrington para sastrería a medida',
 'lead':'Casi ninguna sastrería publica su muestrario. Se enseña en el mostrador, tela por tela, y quien no puede ir se queda sin verlo. Nosotros lo pusimos entero en la web: las 483 telas, con su código y su composición.',
 'cuerpo':'''
<h2 class="t-xl">¿Por qué publicar el muestrario?</h2>
<p class="lead">Porque la conversación cambia. Quien llega habiendo visto las telas pregunta por códigos concretos en vez de «algo azul», y eso ahorra una visita entera. Y quien está a dos horas de Lima puede elegir antes de moverse.</p>
<p class="lead">El muestrario está en <a href="/catalogo-de-telas" data-ir="catalogo">el catálogo</a>, filtrable por colección, grado, tejido y color. Cada ficha lleva el código con el que la pides, la composición y una foto del tejido; en muchas, también el orillo.</p>
%(FIG1)s

<h2 class="t-xl">¿Qué es Barrington?</h2>
<p class="lead">Una casa de telas peruana. Somos distribuidores oficiales, lo que significa que tratamos directo con ellos: la tela llega al taller sin pasar por intermediarios y con el orillo identificable. Puedes verlos en %(BARRINGTON)s.</p>
<p class="lead">Trabajamos con ellos desde hace años y también fuera del mostrador: hicimos el vestuario de su equipo, y eso está contado en <a href="/proyectos/barrington" data-ir="proy-barrington">el proyecto con Barrington</a>.</p>

<h2 class="t-xl">¿Qué hay dentro del muestrario?</h2>
<p class="lead">Nueve tejidos distintos, y conviene saber para qué sirve cada uno. El casimir es el grueso del muestrario y el terreno del terno de oficina y de ocasión. La lanilla es más ligera, para climas templados. El superfine sube en finura de hilo. El tweed y el paño son de abrigo y de saco sport, con cuerpo y textura. Y hay baby alpaca, suri y velour, que es fibra peruana y no tiene equivalente europeo.</p>
<p class="lead">En gradaciones hay Super 100s, 120s y 140s, incluida la Diamond Collection. Lo que significan esos números lo explicamos en <a href="/blog/telas-italianas-en-lima" data-ir="art-italianas">qué cambia una tela italiana</a>, porque la escala es la misma para todas las casas.</p>
%(FIG2)s

<h2 class="t-xl">¿Cómo se elige entre 483?</h2>
<p class="lead">No se elige entre 483. Se elige entre seis u ocho, y para llegar ahí hay dos filtros que hacen casi todo el trabajo: para qué es la prenda y de qué color. Con eso el catálogo baja a un puñado y ya se puede comparar de verdad.</p>
<p class="lead">Después conviene verlas en persona. Una foto en el celular no transmite el brillo ni el peso, y el cielo cubierto de Lima cambia cómo se lee un tono. Llega con los códigos apuntados y en el mostrador se resuelve en diez minutos.</p>

<h2 class="t-xl">¿Se puede pedir una tela que no esté en la web?</h2>
<p class="lead">Sí. El catálogo es el muestrario de Barrington, y además somos distribuidores oficiales de %(CREDITEX)s del Perú y de %(VBC)s, %(ALBINI)s y %(THOMASMASON)s de Italia e Inglaterra. Si buscas algo que no está publicado, pregúntalo.</p>
<p class="lead">Y si no sabes qué pedir, eso también se resuelve: dinos para qué es y en <a href="/tiendas" data-ir="tiendas">cualquiera de las seis tiendas</a> te sacamos tres o cuatro opciones al mostrador.</p>
''',
 'faq':[
  ('¿Cuántas telas tiene el catálogo?','El muestrario completo de Barrington: 483 telas, cada una con su código, su composición y foto del tejido, filtrables por colección, grado, tejido y color.'),
  ('¿Puedo pedir una tela solo con el código?','Sí. Escríbenos el código que viste en el catálogo y te confirmamos disponibilidad antes de que te muevas de casa.'),
  ('¿Qué es la Diamond Collection?','Una de las colecciones de Barrington dentro del muestrario, en gradación Super 140s: hilo muy fino, más caída y más tacto, pensada para prendas de lucir antes que de uso diario.'),
  ('¿Trabajan solo con Barrington?','No. Somos distribuidores oficiales de Barrington y Creditex del Perú, y de Vitale Barberis Canonico, Albini y Thomas Mason de Italia e Inglaterra.'),
 ],
 'wa':'Hola%2C%20quiero%20consultar%20por%20una%20tela%20del%20cat%C3%A1logo.',
 'rel':[('/catalogo-de-telas','El catálogo'),('/proyectos/barrington','Proyecto Barrington'),('/telas','Las casas')],
 'fig':[('/assets/editorial/ed-macro-orillo.jpg',1160,1500,'Orillo de una tela del muestrario de Barrington','El orillo lleva tejido el nombre de la casa. Es la forma de comprobar el origen.'),
        ('/assets/editorial/ed-macro-super100.jpg',1050,1500,'Macro de un tejido Super 100s del muestrario','Nueve tejidos distintos, del casimir de oficina al paño de abrigo.')],
}

# ------------------------------------------------------------------------ 10
A10 = {
 'slug':'sastreria-abierta-domingo-lima', 'pag':'art-domingo', 'cat':'Tiendas',
 'h1':'¿Hay alguna sastrería abierta el domingo en Lima?',
 'titulo':'Sastrería Abierta Domingo en Lima | Andrés Vargas Sastrería',
 'desc':'Abrimos los domingos de 10 a 16 en Jr. Huallaga 558, Cercado de Lima. Qué se puede resolver un domingo y qué conviene dejar para día de semana.',
 'img':'/assets/editorial/ed-oficina-azul.jpg', 'w':848, 'h':1106,
 'alt':'Terno azul a medida en el atelier de Andrés Vargas',
 'lead':'Casi todo el rubro cierra domingo, y es justo el día que mucha gente tiene libre. Nosotros abrimos una de las seis tiendas: Jr. Huallaga 558, en Cercado de Lima, de 10 de la mañana a 4 de la tarde.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué tienda abre el domingo?</h2>
<p class="lead">Solo una, y conviene decirlo claro para que nadie se dé un viaje en balde: <b>Jr. Huallaga 558, Cercado de Lima, domingos de 10:00 a 16:00</b>. Las otras cinco —Huallaga 570, las tres de Jr. Ucayali y la de Av. Primavera 252 en Chacarilla— no abren domingo.</p>
<p class="lead">Los horarios completos de las seis, día por día, están en <a href="/tiendas" data-ir="tiendas">la página de tiendas</a>. Si vas un domingo, apunta esa dirección y no otra.</p>
%(FIG1)s

<h2 class="t-xl">¿Qué se puede resolver un domingo?</h2>
<p class="lead">Bastante más de lo que parece. Tomar medidas, ver telas y decidir una prenda se hace igual de bien un domingo que un miércoles: el mostrador es el mismo y el muestrario está completo. Si vienes a empezar un encargo, el domingo sirve perfectamente.</p>
<p class="lead">También sirve para una prueba, que es la parte que suele complicar a quien trabaja de lunes a viernes. Un terno a medida lleva varias, y encajarlas en horario de oficina es el motivo más común por el que un encargo se estira semanas.</p>

<h2 class="t-xl">¿Qué conviene dejar para día de semana?</h2>
<p class="lead">Cualquier cosa que dependa del taller y no del mostrador. Un arreglo urgente, una consulta técnica sobre una tela que hay que pedir, o algo que necesite que el maestro lo vea: eso se resuelve mejor de lunes a sábado, cuando el taller está a pleno.</p>
<p class="lead">Si tienes dudas de si tu caso es de domingo o de semana, escríbenos antes por <a href="https://wa.me/51959370397" target="_blank" rel="noopener">WhatsApp</a> y te lo decimos. Es un minuto y te ahorra el viaje.</p>
%(FIG2)s

<h2 class="t-xl">¿Hace falta cita?</h2>
<p class="lead">No hace falta, puedes llegar y te atendemos. Pero el domingo es el día con más movimiento en Huallaga y una hora acordada es la diferencia entre entrar y esperar. Si vienes con algo concreto en la cabeza, avísanos.</p>
<p class="lead">Y si vienes a ver telas, adelanta trabajo desde casa: el <a href="/catalogo-de-telas" data-ir="catalogo">catálogo completo</a> está publicado, y llegar con tres o cuatro códigos apuntados convierte una hora de mostrador en diez minutos.</p>

<h2 class="t-xl">¿Por qué solo una tienda?</h2>
<p class="lead">Porque preferimos abrir una bien que seis a medias. El domingo el equipo es más corto y concentrarlo en un punto significa que quien llega encuentra a alguien que puede medir, aconsejar y cerrar un encargo, no solo abrir la puerta.</p>
<p class="lead">Huallaga 558 es la elegida por sitio y por espacio. Si vives por el sur y te queda lejos, la de <a href="/tiendas" data-ir="tiendas">Chacarilla</a> abre de lunes a sábado hasta las 8 de la noche, que para muchos funciona mejor que un domingo.</p>
''',
 'faq':[
  ('¿Qué sastrería abre domingo en Lima?','La nuestra de Jr. Huallaga 558, Cercado de Lima, domingos de 10:00 a 16:00. Las otras cinco tiendas no abren ese día.'),
  ('¿Puedo tomarme medidas un domingo?','Sí. Medidas, elección de tela y pruebas se hacen igual que cualquier otro día. Lo que depende del taller conviene dejarlo para lunes a sábado.'),
  ('¿Necesito cita para ir un domingo?','No es obligatoria, pero es el día de más movimiento. Escríbenos por WhatsApp y acordamos una hora.'),
  ('¿Hasta qué hora abren los demás días?','De lunes a sábado hasta las 20:00 en Huallaga y en Chacarilla. Las tiendas de Jr. Ucayali cierran al mediodía entre 13:00 y 14:00.'),
 ],
 'wa':'Hola%2C%20quiero%20ir%20un%20domingo.%20%C2%BFMe%20confirman%20la%20hora%3F',
 'rel':[('/tiendas','Las seis tiendas'),('/catalogo-de-telas','El catálogo'),('/blog/como-llegar-a-nuestras-tiendas','Cómo llegar')],
 'fig':[('/assets/editorial/ed-verano-cruzado.jpg',990,1176,'Terno cruzado a medida','Medir, ver telas y probar se hace igual un domingo que un miércoles.'),
        ('/assets/editorial/ed-macro-orillo.jpg',1160,1500,'Orillo de tela en el mostrador','Llegar con los códigos apuntados convierte una hora de mostrador en diez minutos.')],
}

# ------------------------------------------------------------------------ 11
A11 = {
 'slug':'como-llegar-a-nuestras-tiendas', 'pag':'art-como-llegar', 'cat':'Tiendas',
 'h1':'Cómo llegar a nuestras seis tiendas de Lima',
 'titulo':'Sastrerías en Cercado de Lima y Surco: Cómo Llegar | Andrés Vargas',
 'desc':'Seis tiendas en Lima: tres en Jr. Ucayali, dos en Jr. Huallaga y una en Chacarilla, Surco. Direcciones, horarios y cuál te conviene según lo que necesites.',
 'img':'/assets/hero.jpg', 'w':1900, 'h':1008,
 'alt':'Sastrería Andrés Vargas en Lima',
 'lead':'Tenemos seis tiendas y no son intercambiables: dos zonas de la ciudad, horarios distintos y un domingo abierto. Aquí está cuál te conviene según lo que vengas a hacer y cómo te muevas.',
 'cuerpo':'''
<h2 class="t-xl">Cercado de Lima: Jr. Ucayali y Jr. Huallaga</h2>
<p class="lead">Cinco de las seis están en Cercado, a pocas cuadras entre sí. Tres en <b>Jr. Ucayali 115, 119 y 121</b> y dos en <b>Jr. Huallaga 558 y 570</b>. Es el centro histórico, así que la referencia útil no es una avenida sino la Plaza Mayor: desde ahí se llega caminando.</p>
<p class="lead">Los horarios no son iguales. Huallaga abre de lunes a sábado de 10:00 a 20:00 corrido, y el 558 además <a href="/blog/sastreria-abierta-domingo-lima" data-ir="art-domingo">abre domingo de 10:00 a 16:00</a>. Las tres de Ucayali abren de lunes a viernes con cierre al mediodía, de 13:00 a 14:00. Si vas a Ucayali, evita esa hora.</p>
%(FIG1)s

<h2 class="t-xl">Surco: Av. Primavera 252, Chacarilla</h2>
<p class="lead">La sexta está en <b>Av. Primavera 252, Chacarilla</b>, y es la que resuelve el lado sur de la ciudad. Abre de lunes a sábado de 10:00 a 20:00. Para quien vive o trabaja en Surco, San Borja, Miraflores o La Molina, es la que ahorra el viaje al centro.</p>
<p class="lead">Es también la que solemos recomendar para la <a href="/trajes-de-novio" data-ir="novios">experiencia de novios</a>, donde suelen venir varias personas a la vez y el espacio y el estacionamiento importan.</p>

<h2 class="t-xl">¿Cuál me conviene?</h2>
<p class="lead">Si vienes en transporte público desde el norte, el este o el propio centro, cualquiera de Cercado. Si vienes en carro desde el sur, Chacarilla sin dudar: estacionar en Cercado un día de semana consume más tiempo que la visita.</p>
<p class="lead">Si tu única ventana es el domingo, la respuesta es una sola: Huallaga 558. Y si tienes que venir en hora de almuerzo, Huallaga o Chacarilla, porque Ucayali cierra.</p>
%(FIG2)s

<h2 class="t-xl">¿Qué conviene llevar la primera vez?</h2>
<p class="lead">Los zapatos con los que vas a usar la prenda, porque condicionan el largo del pantalón. Y si tienes un terno o una camisa que te queda bien, tráelo: es la referencia más útil que existe para entender qué te gusta de cómo cae.</p>
<p class="lead">Si vienes a ver telas, adelanta desde casa. El <a href="/catalogo-de-telas" data-ir="catalogo">muestrario completo</a> está publicado con código y composición; llegar con tres o cuatro códigos apuntados cambia por completo el ritmo de la visita.</p>

<h2 class="t-xl">¿Hace falta cita?</h2>
<p class="lead">No, puedes llegar y te atendemos. Pero si vienes desde lejos, si vienes con poco tiempo o si vienes en grupo, acordar una hora evita la espera. Un mensaje por <a href="https://wa.me/51959370397" target="_blank" rel="noopener">WhatsApp</a> basta.</p>
<p class="lead">Las seis direcciones con sus horarios día por día están en <a href="/tiendas" data-ir="tiendas">la página de tiendas</a>.</p>
''',
 'faq':[
  ('¿Dónde están las tiendas de Andrés Vargas?','Cinco en Cercado de Lima: Jr. Ucayali 115, 119 y 121, y Jr. Huallaga 558 y 570. La sexta en Av. Primavera 252, Chacarilla, Santiago de Surco.'),
  ('¿Cuál abre domingo?','Solo Jr. Huallaga 558, de 10:00 a 16:00.'),
  ('¿Las tiendas de Ucayali cierran al mediodía?','Sí, de 13:00 a 14:00, y abren de lunes a viernes. Huallaga y Chacarilla abren corrido de 10:00 a 20:00 de lunes a sábado.'),
  ('¿Qué tienda me conviene si vengo en carro desde el sur?','La de Av. Primavera 252, Chacarilla. Estacionar en Cercado en día de semana suele tomar más tiempo que la visita.'),
 ],
 'wa':'Hola%2C%20quiero%20visitarlos.%20%C2%BFQu%C3%A9%20tienda%20me%20conviene%3F',
 'rel':[('/tiendas','Las seis tiendas'),('/blog/sastreria-abierta-domingo-lima','Abrimos domingo'),('/trajes-de-novio','Novios')],
 'fig':[('/assets/editorial/ed-oficina-camel.jpg',1364,1050,'Terno a medida en tono camel','Cinco tiendas en Cercado, a pocas cuadras entre sí, y una en Chacarilla.'),
        ('/assets/editorial/ed-blazer-azul.jpg',1328,1106,'Blazer azul a medida','Lleva los zapatos con los que vas a usar la prenda: condicionan el largo.')],
}

# ------------------------------------------------------------------------ 12
A12 = {
 'slug':'terno-a-medida-o-de-tienda', 'pag':'art-medida-tienda', 'cat':'Guías',
 'h1':'Terno a medida o de tienda: en qué se nota la diferencia',
 'titulo':'Terno a Medida o de Tienda: Diferencias Reales | Andrés Vargas',
 'desc':'Qué hace distinto a un terno a medida: el patrón, el hombro, la tela elegida y los arreglos que no hacen falta. Y cuándo un terno de tienda basta.',
 'img':'/assets/editorial/ed-gala-pinstripe.jpg', 'w':990, 'h':1120,
 'alt':'Terno a rayas a medida de Andrés Vargas',
 'lead':'La diferencia no está donde la gente cree. No es el forro, ni los botones, ni el número de la tela: es el hombro y es el patrón. Y hay casos en los que un terno de tienda resuelve perfectamente.',
 'cuerpo':'''
<h2 class="t-xl">¿Dónde se nota primero?</h2>
<p class="lead">En el hombro. Es la única parte del saco que no se arregla después, y es la que la vista registra antes que ninguna otra. Si la costura del hombro cae donde termina tu hombro, el saco se ve bien aunque todo lo demás sea discreto; si cae un centímetro afuera, no hay sastre que lo salve sin desmontar la prenda.</p>
<p class="lead">Un terno de talla parte de un hombro promedio. A medida, esa línea se traza sobre el tuyo, y con ella la sisa, que es donde nace la manga. De esas dos decisiones depende que puedas levantar el brazo sin que el saco entero se levante contigo.</p>
%(FIG1)s

<h2 class="t-xl">¿Y el patrón, qué cambia?</h2>
<p class="lead">Que deja de haber una talla. En una prenda de tienda el pecho, la cintura y el largo vienen atados: si eliges por pecho, la cintura sobra. Sobre un patrón propio cada medida es independiente, y ahí es donde encajan los cuerpos que ninguna talla contempla: espalda ancha con cintura estrecha, un hombro más bajo que el otro, torso largo con piernas cortas.</p>
<p class="lead">Ese patrón queda guardado con tu nombre. La segunda prenda no vuelve a empezar de cero, y eso hace que a partir de la segunda el proceso sea mucho más corto. Cómo es la primera vez lo contamos en <a href="/blog/primer-terno-a-medida" data-ir="art-primer-traje">cómo elegir tu primer terno</a>.</p>

<h2 class="t-xl">¿La tela cambia mucho?</h2>
<p class="lead">Cambia lo que puedes elegir. En tienda eliges entre las telas de esa temporada; a medida eliges entre el muestrario completo, y eso incluye decidir el peso según cuántas veces al mes vas a usarlo, que es la variable que más condiciona la vida de un terno.</p>
<p class="lead">Trabajamos con casas nacionales e importadas y somos distribuidores oficiales: %(BARRINGTON)s y %(CREDITEX)s del Perú, y %(VBC)s, %(ALBINI)s y %(THOMASMASON)s de Italia e Inglaterra. Las 483 telas de Barrington están publicadas en <a href="/catalogo-de-telas" data-ir="catalogo">el catálogo</a>.</p>
%(FIG2)s

<h2 class="t-xl">¿Cuándo basta un terno de tienda?</h2>
<p class="lead">Con más frecuencia de la que un sastre admitiría. Si tu cuerpo se parece bastante al promedio, si lo vas a usar dos o tres veces al año y si estás dispuesto a pagar unos arreglos, un terno de tienda bien arreglado se ve bien. Decir lo contrario sería vender humo.</p>
<p class="lead">A medida tiene sentido cuando el terno trabaja —sale de casa varios días por semana—, cuando tu cuerpo no entra limpio en una talla, o cuando la ocasión importa lo suficiente para que nada quede al azar: un matrimonio propio, una presentación, un cargo nuevo.</p>

<h2 class="t-xl">¿Cuántas pruebas lleva?</h2>
<p class="lead">Varias, y el número depende de la prenda y del cuerpo. No damos una cifra fija porque no la hay: un saco cruzado sobre un torso complicado pide más ajuste que un pantalón. Lo que sí decimos de entrada, antes de empezar, es cuántas esperamos en tu caso.</p>
<p class="lead">Si quieres ver el proceso completo, está en <a href="/a-medida" data-ir="medida">cómo trabajamos a medida</a>. Y si prefieres preguntarlo, en <a href="/tiendas" data-ir="tiendas">cualquiera de las seis tiendas</a> te responde un sastre.</p>
''',
 'faq':[
  ('¿Cuál es la diferencia real entre un terno a medida y uno de tienda?','El hombro y el patrón. La costura del hombro es lo único que no se arregla después, y sobre un patrón propio el pecho, la cintura y el largo dejan de estar atados a una misma talla.'),
  ('¿Vale la pena a medida si uso terno dos veces al año?','Si tu cuerpo entra limpio en una talla, un terno de tienda bien arreglado puede bastar. A medida se justifica cuando el terno se usa mucho, cuando el cuerpo no encaja en una talla o cuando la ocasión no admite azar.'),
  ('¿Cuántas pruebas necesita un terno a medida?','Depende de la prenda y del cuerpo. Te decimos cuántas esperamos en tu caso antes de empezar, no después.'),
  ('¿Se puede arreglar el hombro de un saco?','No sin desmontar la prenda. Es la razón por la que el hombro es lo primero que miramos y lo que más justifica la medida.'),
 ],
 'wa':'Hola%2C%20quiero%20saber%20si%20me%20conviene%20un%20terno%20a%20medida.',
 'rel':[('/a-medida','Cómo trabajamos'),('/ternos-a-medida','Ternos a medida'),('/blog/primer-terno-a-medida','Tu primer terno')],
 'fig':[('/assets/editorial/ed-saco-pieddepoule.jpg',988,966,'Detalle de hombro de un saco a medida','El hombro es lo único que no se arregla después. Por eso es lo primero que miramos.'),
        ('/assets/editorial/ed-macro-cuadros.jpg',1050,1500,'Macro de tela de cuadros para sastrería','A medida no eliges entre la temporada: eliges entre el muestrario completo.')],
}

ARTS2 = [A7, A8, A9, A10, A11, A12]
