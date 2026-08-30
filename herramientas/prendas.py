# -*- coding: utf-8 -*-
"""Una página por prenda.

Lavallière tiene /blazer/, /esmoquin-a-medida/, /sacos-sport/ y /chaque-a-medida/;
aquí todo eso vivía dentro de /ternos-a-medida y no competía por nada.

Solo entran las prendas que el cliente dice confeccionar:
  · /a-medida  «Ternos y trajes de dos y tres piezas… Esmóquines y chaqués incluidos.»
  · /telas     describe hacer blazer, saco sport y abrigo.
Frac y arreglos no tienen respaldo y quedan fuera hasta que el cliente confirme.
"""
WA = 'https://wa.me/51959370397?text='

PRENDAS = [
{
 'slug':'esmoquin-a-medida', 'pag':'prenda-esmoquin', 'rotulo':'Prenda · Gala',
 'h1':'Esmoquin a medida', 'miga':'Esmoquin',
 'titulo':'Esmoquin a Medida en Lima | Sastrería Andrés Vargas',
 'desc':'Esmoquin confeccionado a medida en Lima: solapa de raso, galón en el pantalón y corbatín. Lo que pide una invitación que dice etiqueta.',
 'img':'/assets/editorial-esmoquin-marfil.jpg','w':1275,'h':1400,
 'alt':'Esmoquin marfil confeccionado a medida',
 'lead':'Es lo que piden las invitaciones que dicen etiqueta o black tie, y lo que no se resuelve con un terno negro y corbata.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué distingue un esmoquin de un terno negro?</h2>
<p class="lead">El raso. La solapa va forrada en raso, el pantalón lleva un galón del mismo tejido corriendo por el costado y el cierre es de un solo botón. Esos tres detalles se leen a distancia, y son la razón por la que sustituirlo por un terno oscuro con corbata negra se nota desde la puerta.</p>
<p class="lead">La solapa puede ser de pico o de chal. La de chal, redondeada y sin quiebre, es la más clásica de noche; la de pico levanta el hombro y estiliza. Se decide contigo en la primera cita.</p>
%(FIG1)s

<h2 class="t-xl">¿Cuándo se lleva?</h2>
<p class="lead">De noche. Bodas de etiqueta, galas, cenas de premiación y algunas fiestas de fin de año. De día, el equivalente formal no es el esmoquin sino el <a href="/chaque-a-medida">chaqué</a>, y confundirlos es el error más frecuente. Lo desarrollamos entero en <a href="/blog/codigo-de-vestimenta">qué se espera de cada código de vestimenta</a>.</p>

<h2 class="t-xl">¿Qué tela lleva?</h2>
<p class="lead">Caída por encima de resistencia, porque es una prenda de pocas puestas. Ahí tiene sentido subir de grado: la <a href="/telas/super-140s">Super 140s</a> de la colección Diamond es lo más fino del muestrario. Un <a href="/telas/casimir">casimir</a> de acabado rasado también funciona, con superficie más limpia y más formal.</p>
<p class="lead">En color, el <a href="/terno-negro">negro</a> es el canónico y el azul medianoche es la alternativa que muchos prefieren: bajo luz artificial se lee más profundo que el propio negro. El marfil se reserva para climas cálidos y ceremonias al aire libre.</p>
''',
 'faq':[('¿Puedo usar corbata en lugar de corbatín?','El código de black tie pide corbatín. Una corbata negra con esmoquin es una licencia que se ve, sobre todo si la solapa es de raso.'),
        ('¿El esmoquin lleva chaleco o faja?','Uno de los dos, nunca ambos ni ninguno. La faja se pone con el pliegue hacia arriba y el chaleco tiene que cubrir la pretina del pantalón.'),
        ('¿De qué color debe ser la camisa?','Blanca. Con pechera lisa o de piqué, y puño de gemelo.'),
        ('¿Sirve para una boda de día?','No es lo suyo. De día el equivalente es el chaqué; el esmoquin es prenda de noche.')],
 'fig':[('/assets/editorial/ed-gala-pinstripe.jpg',990,1120,'Traje de gala a medida','La solapa de raso y el galón del pantalón son lo que distingue un esmoquin de un terno oscuro.')],
 'rel':[('/telas/super-140s','Super 140s'),('/blog/codigo-de-vestimenta','Códigos de vestimenta'),('/trajes-de-novio','Trajes de novio')],
 'wa':'Hola%2C%20quiero%20consultar%20por%20un%20esmoquin%20a%20medida.',
},
{
 'slug':'chaque-a-medida', 'pag':'prenda-chaque', 'rotulo':'Prenda · Ceremonia',
 'h1':'Chaqué a medida', 'miga':'Chaqué',
 'titulo':'Chaqué a Medida en Lima | Sastrería Andrés Vargas',
 'desc':'Chaqué confeccionado a medida en Lima: levita, pantalón de raya diplomática y chaleco. La prenda de la ceremonia de día.',
 'img':'/assets/editorial/ed-gala-pinstripe.jpg','w':990,'h':1120,
 'alt':'Prenda de ceremonia confeccionada a medida',
 'lead':'La prenda de la ceremonia de día. Casi nadie la pide dos veces en la vida, y por eso casi nadie sabe qué lleva.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué es exactamente un chaqué?</h2>
<p class="lead">Tres piezas con reglas propias: la levita, de faldón largo que cae en curva por detrás y cierra con un solo botón; el pantalón de raya diplomática, en gris y negro, que nunca hace juego con la levita; y el chaleco, normalmente gris claro o beige.</p>
<p class="lead">Se completa con camisa blanca de cuello clásico y corbatón o plastrón. El zapato, negro y liso.</p>
%(FIG1)s

<h2 class="t-xl">¿Cuándo se usa?</h2>
<p class="lead">De día y solo en ceremonia: bodas de mañana o mediodía, actos protocolares, alguna ceremonia académica. Es el nivel de etiqueta rigurosa en su versión diurna; el nocturno es el frac. Si la invitación dice etiqueta rigurosa y la boda es a las once de la mañana, esto es lo que están pidiendo.</p>
<p class="lead">El error más repetido es aparecer con <a href="/esmoquin-a-medida">esmoquin</a> a una ceremonia de día. Son la misma categoría de formalidad en horarios opuestos.</p>

<h2 class="t-xl">¿Se hace a medida o se alquila?</h2>
<p class="lead">Nosotros lo confeccionamos a tu medida, dentro del servicio de ternos y trajes. Tiene sentido si es tu boda o si el cargo te va a pedir usarlo más de una vez; para una única ocasión, conviene conversarlo antes de decidir.</p>
<p class="lead">Si es para tu matrimonio, empieza por leer <a href="/blog/calendario-del-novio">el calendario del novio</a>: el chaqué tiene más piezas que un terno y cada una lleva su prueba.</p>
''',
 'faq':[('¿Cuál es la diferencia entre chaqué y frac?','El chaqué es de día y el frac de noche. El chaqué tiene faldón largo y entero por detrás; el frac va cortado por delante a la cintura y lleva corbatín y chaleco blancos.'),
        ('¿El pantalón hace juego con la levita?','No. El pantalón de chaqué es de raya diplomática en gris y negro, y contrasta con la levita a propósito.'),
        ('¿Se lleva corbata?','Corbatón o plastrón, que es lo tradicional. Una corbata normal baja el registro de la prenda.'),
        ('¿Lo confeccionan a medida?','Sí, dentro del servicio de ternos y trajes. Escríbenos con la fecha de la ceremonia y te decimos con qué margen cuentas.')],
 'fig':[('/assets/editorial/ed-verano-cruzado.jpg',990,1176,'Prenda cruzada a medida','El chaqué es la etiqueta rigurosa de día; el esmoquin, la de noche. Confundirlos se nota.')],
 'rel':[('/esmoquin-a-medida','Esmoquin'),('/trajes-de-novio','Trajes de novio'),('/blog/codigo-de-vestimenta','Códigos de vestimenta')],
 'wa':'Hola%2C%20quiero%20consultar%20por%20un%20chaqu%C3%A9%20a%20medida.',
},
{
 'slug':'blazer-a-medida', 'pag':'prenda-blazer', 'rotulo':'Prenda · Diario',
 'h1':'Blazer a medida', 'miga':'Blazer',
 'titulo':'Blazer a Medida en Lima | Sastrería Andrés Vargas',
 'desc':'Blazer confeccionado a medida en Lima, en casimir y superfine de Barrington. La prenda que sirve con pantalón de vestir y con jean.',
 'img':'/assets/editorial/ed-blazer-azul.jpg','w':1328,'h':1106,
 'alt':'Blazer azul confeccionado a medida',
 'lead':'Si vas a mandarte hacer una sola prenda y no sabes cuál, esta es la que más veces te vas a poner.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué separa un blazer de un saco de terno?</h2>
<p class="lead">Que vive solo. El saco de terno nace con su pantalón y pierde sentido separado; el blazer se corta para llevarse suelto, con pantalón de otro tono, con chino o con jean. Eso cambia el corte: hombro algo más blando, largo un punto más corto y botonadura pensada para verse abierta.</p>
<p class="lead">El azul marino liso es el que resuelve más situaciones. Con camisa blanca sube a reunión; con polo y jean baja a fin de semana sin verse disfrazado.</p>
%(FIG1)s

<h2 class="t-xl">¿Qué tela pedirle?</h2>
<p class="lead">Va a trabajar mucho, así que manda la resistencia. La <a href="/telas/super-100s">Super 100s</a> es la base del muestrario justamente para esto: aguanta el uso continuo y vuelve a su sitio al colgarla. Para un blazer con más textura, el <a href="/telas/superfine">Superfine</a> da microdiseño con mano suave.</p>
<p class="lead">En <a href="/terno-azul">azul</a> tienes desde el marino cerrado hasta el que solo revela su diseño de cerca. Si ya tienes uno azul, el siguiente paso lógico es un <a href="/terno-gris">gris</a> o un <a href="/terno-burdeos">burdeos</a>.</p>

<h2 class="t-xl">Blazer o saco sport</h2>
<p class="lead">Se confunden y no son lo mismo. El blazer es liso y urbano; el <a href="/saco-sport-a-medida">saco sport</a> lleva textura o diseño —tweed, cuadros, pied de poule— y pide un registro más relajado. Tener los dos cubre casi todo lo que no es terno.</p>
''',
 'faq':[('¿Puedo usar el blazer con jean?','Sí, y es de sus mejores usos. Conviene que el blazer sea liso y el jean oscuro y sin roturas.'),
        ('¿De qué color me conviene el primero?','Azul marino. Es el que entra en más sitios y admite más combinaciones de camisa y pantalón.'),
        ('¿Sirve el saco de mi terno como blazer?','Rara vez. El saco de terno está cortado para ir con su pantalón, y usado suelto se le nota que le falta algo. Además se desgasta distinto que el pantalón y el conjunto deja de casar.'),
        ('¿Cuántos botones?','Dos es lo más versátil. El de tres alarga el torso y el cruzado es una prenda distinta, más formal.')],
 'fig':[('/assets/editorial/ed-blazer-salmon.jpg',990,1064,'Blazer en tono claro a medida','El blazer se corta para llevarse suelto: hombro más blando y largo un punto más corto que el saco de terno.')],
 'rel':[('/telas/super-100s','Super 100s'),('/saco-sport-a-medida','Saco sport'),('/blog/salir-del-negro','Salir del negro')],
 'wa':'Hola%2C%20quiero%20consultar%20por%20un%20blazer%20a%20medida.',
},
{
 'slug':'saco-sport-a-medida', 'pag':'prenda-sport', 'rotulo':'Prenda · Fin de semana',
 'h1':'Saco sport a medida', 'miga':'Saco sport',
 'titulo':'Saco Sport a Medida en Lima | Sastrería Andrés Vargas',
 'desc':'Saco sport a medida en Lima, en tweed, superfine y pied de poule. La prenda del fin de semana, con textura y sin corbata.',
 'img':'/assets/editorial/ed-sport-cuadros.jpg','w':990,'h':1092,
 'alt':'Saco sport de cuadros confeccionado a medida',
 'lead':'La prenda con la que se sale de la oficina sin ponerse un terno. Textura, color y ninguna corbata.',
 'cuerpo':'''
<h2 class="t-xl">¿Qué hace que un saco sea sport?</h2>
<p class="lead">La tela, antes que el corte. Un saco sport lleva relieve visible —tweed, espiga, cuadros, pied de poule— donde un terno lleva superficie lisa. Esa textura es la que le da permiso para ir sin corbata y con pantalón de otro tono sin verse incompleto.</p>
<p class="lead">Suele llevar también detalles que el terno no admite: coderas, bolsillos de parche, una construcción más blanda que deja moverse. No es un terno relajado, es otra prenda.</p>
%(FIG1)s

<h2 class="t-xl">¿Qué tejidos funcionan?</h2>
<p class="lead">El <a href="/telas/tweed">tweed</a> es el clásico: hebras de distintos colores retorcidas en un mismo hilo, de ahí su relieve y su profundidad. Abriga, aguanta y envejece bien, aunque en Lima se queda para el invierno y el fin de semana.</p>
<p class="lead">Para el resto del año, el <a href="/telas/superfine">Superfine</a> da el carácter del tweed con mano más dulce, y el <a href="/telas/casimir">casimir</a> en cuadros o microdiseño funciona todo el año. En color, el <a href="/terno-marron">marrón</a> es el terreno natural del sport: admite el zapato marrón que el azul complica.</p>

<h2 class="t-xl">¿Con qué se lleva?</h2>
<p class="lead">Pantalón de franela o chino en tono contrastado, camisa clara sin corbata, y zapato de ante o con suela visible. Lo que no funciona es el pantalón de terno: si hace juego, ya no es un saco sport, es media prenda de un traje.</p>
<p class="lead">Si buscas algo más urbano y liso, lo tuyo es el <a href="/blazer-a-medida">blazer</a>.</p>
''',
 'faq':[('¿Cuál es la diferencia con un blazer?','El blazer es liso y urbano; el saco sport lleva textura o diseño y pide un registro más relajado. Los dos se llevan sueltos, pero no en los mismos sitios.'),
        ('¿Sirve para la oficina?','En oficinas con código relajado, sí. En un ambiente formal se lee como fin de semana.'),
        ('¿El tweed no da mucho calor en Lima?','Para el terno diario sí. Para un saco de invierno y de fin de semana funciona bien, que es justo su sitio.'),
        ('¿Lleva coderas?','Solo si las quieres. Son un detalle tradicional del sport, no una obligación.')],
 'fig':[('/assets/editorial/ed-saco-pieddepoule.jpg',988,966,'Saco a medida en pied de poule','La textura es lo que le da permiso al saco sport para ir sin corbata.')],
 'rel':[('/telas/tweed','Tweed'),('/blazer-a-medida','Blazer'),('/terno-marron','Terno marrón')],
 'wa':'Hola%2C%20quiero%20consultar%20por%20un%20saco%20sport%20a%20medida.',
},
{
 'slug':'abrigo-a-medida', 'pag':'prenda-abrigo', 'rotulo':'Prenda · Invierno',
 'h1':'Abrigo a medida', 'miga':'Abrigo',
 'titulo':'Abrigo a Medida en Lima | Sastrería Andrés Vargas',
 'desc':'Abrigo confeccionado a medida en Lima, en paño batanado, tweed y baby alpaca peruana. La prenda que se sostiene sola.',
 'img':'/assets/editorial/ed-abrigo-paisaje.jpg','w':1376,'h':1078,
 'alt':'Abrigo de paño confeccionado a medida',
 'lead':'Es la prenda que más se nota y la que menos gente se manda hacer. También la que mejor envejece.',
 'cuerpo':'''
<h2 class="t-xl">¿Por qué a medida y no de tienda?</h2>
<p class="lead">Porque va encima de todo lo demás. Un abrigo tiene que caber sobre un saco sin tirar del hombro ni acortar la manga, y ese cálculo es justamente lo que un patrón estándar no hace: los de tienda suelen quedar amplios de cuerpo y cortos de manga cuando llevas saco debajo.</p>
<p class="lead">El largo también es decisión tuya y no del fabricante. Por encima de la rodilla es más urbano y más fácil de llevar; por debajo protege más y se lee más formal.</p>
%(FIG1)s

<h2 class="t-xl">¿Qué telas se usan?</h2>
<p class="lead">El <a href="/telas/pano">paño</a> es la respuesta clásica: lana merino con acabado batanado, de la familia del melton, compactado hasta darle cuerpo y calor al tacto. Es la tela que se sostiene sola, y por eso el abrigo cae como cae.</p>
<p class="lead">El <a href="/telas/tweed">tweed</a> aporta relieve y profundidad de color, y la pelusa de su superficie repele el agua, lo que en una ciudad de garúa no es un detalle menor. Y está la <a href="/telas/baby-alpaca">baby alpaca</a>, fibra peruana de las más apreciadas del mundo: la suri da brillo y una ligereza que sorprende para el abrigo que tiene que ser excepcional.</p>

<h2 class="t-xl">¿Tiene sentido un abrigo en Lima?</h2>
<p class="lead">Menos que en una ciudad con invierno de verdad, y más de lo que la gente cree. Los meses de garúa piden una prenda de abrigo sobre el terno, y lo que suele ocupar ese lugar es una casaca que rompe todo lo que hay debajo. Un abrigo bien cortado hace el trabajo sin deshacer la silueta.</p>
<p class="lead">Y si viajas fuera en invierno del norte, ahí la prenda deja de ser opcional. Cómo cuidarlo para que dure está en <a href="/blog/cuidar-un-traje">cómo cuidar un terno</a>: con la lana batanada, el gancho ancho y el cepillado importan todavía más.</p>
''',
 'faq':[('¿Qué largo debe tener un abrigo?','Depende de para qué lo quieras. Por encima de la rodilla es más versátil y urbano; por debajo abriga más y se ve más formal. Se decide contigo en la prueba, con el saco puesto debajo.'),
        ('¿Se puede hacer en baby alpaca?','Sí. Es fibra peruana y de las más apreciadas del mundo; la suri da brillo y ligereza, y el velour un tacto aterciopelado.'),
        ('¿Hay que probárselo con saco debajo?','Siempre. Es la única forma de que la manga y el hombro queden bien en el uso real de la prenda.'),
        ('¿El paño y el tweed dan mucho calor para Lima?','Para los meses de garúa funcionan. En verano ninguna de las dos tiene sentido, y ahí es mejor una prenda más ligera.')],
 'fig':[('/assets/editorial/ed-abrigo-alpaca.jpg',990,1204,'Abrigo en baby alpaca peruana','La baby alpaca es peruana y de las fibras más apreciadas del mundo.')],
 'rel':[('/telas/pano','Paño'),('/telas/baby-alpaca','Baby alpaca'),('/blog/cuidar-un-traje','Cuidar el terno')],
 'wa':'Hola%2C%20quiero%20consultar%20por%20un%20abrigo%20a%20medida.',
},
]


import json, re
SITIO = 'https://sastreriaandresvargas.pe'


def seccion(p):
    figs = {'FIG%d' % (i + 1): (
        '<figure class="fig-art"><img src="%s" alt="%s" loading="lazy" width="%d" height="%d">'
        '<figcaption>%s</figcaption></figure>' % (f[0], f[3], f[1], f[2], f[4]))
        for i, f in enumerate(p['fig'])}
    cuerpo = re.sub(r'%\((\w+)\)s', lambda m: figs[m.group(1)], p['cuerpo'])

    rel = '\n'.join(
        '        <a class="puerta rev"%s href="%s">\n'
        '          <span class="puerta-cuerpo"><svg class="icono icono-puerta" viewBox="0 0 32 32" data-icono="%s" aria-hidden="true"></svg><b>%s</b></span>\n'
        '        </a>' % ((' data-d="%d"' % i if i else ''), u,
                          'nota' if u.startswith('/blog/') else ('tela' if u.startswith('/telas/') else
                          ('gota' if u.startswith('/terno-') else ('anillos' if 'novio' in u else 'saco'))), t)
        for i, (u, t) in enumerate(p['rel']))

    faq_html = '\n'.join('          <details>\n            <summary>%s</summary>\n'
                         '            <p>%s</p>\n          </details>' % (q, r) for q, r in p['faq'])
    faq_ld = json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q,
                        'acceptedAnswer': {'@type': 'Answer', 'text': re.sub(r'<[^>]+>', '', r)}}
                       for q, r in p['faq']]}, ensure_ascii=False, separators=(',', ':'))

    # Service y no Product: no se publica precio, y un Product sin oferta es
    # justo lo que Google marca como incompleto.
    serv_ld = json.dumps({'@context': 'https://schema.org', '@type': 'Service',
        'name': p['h1'], 'description': p['desc'],
        'serviceType': 'Sastrería a medida', 'areaServed': {'@type': 'City', 'name': 'Lima'},
        'provider': {'@type': 'ClothingStore', 'name': 'Andrés Vargas Sastrería', 'url': SITIO},
        'url': SITIO + '/' + p['slug']}, ensure_ascii=False, separators=(',', ':'))

    return '''
<!-- ==================== PRENDA · %(H1)s ==================== -->
<main class="pagina" data-pag="%(pag)s">
  <section class="pag-hero sobre-azul">
    <img class="pag-hero-img" src="%(img)s" alt="%(alt)s" loading="lazy" width="%(w)d" height="%(h)d">
    <div class="pag-hero-velo"></div>
    <div class="caja">
      <div class="miga"><a href="/" data-ir="inicio">Inicio</a> · <a href="/ternos-a-medida" data-ir="trajes">Ternos y trajes</a> · %(miga)s</div>
      <span class="rotulo">%(rotulo)s</span>
      <h1 class="t-hero">%(h1)s</h1>
      <p class="lead medida" style="margin-top:1.25rem;">%(lead)s</p>
    </div>
  </section>

  <section class="seccion">
    <div class="caja">
      <article class="articulo medida centro rev">
%(cuerpo)s
      </article>
    </div>
  </section>

  <section class="seccion fondo-nube">
    <div class="caja">
      <div class="enc centro">
        <span class="rotulo">Sigue por aquí</span>
        <h2 class="t-xl">Lo que puede interesarte</h2>
      </div>
      <div class="puertas">
%(rel)s
      </div>
    </div>
  </section>

  <section class="seccion">
    <div class="caja">
      <div class="enc"><span class="rotulo">Preguntas frecuentes</span><h2 class="t-xl">Lo que más nos preguntan</h2></div>
      <div class="faq medida" style="margin-top:2rem;">
%(faq)s
      </div>
    </div>
  </section>

  <section class="seccion-corta fondo-azul sobre-azul con-foto" style="--foto:url('/assets/editorial/ed-macro-orillo-fondo.jpg');">
    <div class="caja centro">
      <h2 class="t-xl">¿Lo hablamos?</h2>
      <p class="lead centro medida" style="margin-top:1rem;">Cuéntanos para cuándo lo necesitas y te decimos con qué margen cuentas. O pásate por cualquiera de nuestras seis tiendas de Lima.</p>
      <div class="acciones" style="justify-content:center;margin-top:2rem;">
        <a class="btn btn-claro" href="%(waurl)s" target="_blank" rel="noopener"><svg class="ico-btn" viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.8-.9-2.1-1s-.5-.2-.7.1-.7.9-.9 1.1-.4.3-.7.1a8 8 0 01-2.4-1.5 9 9 0 01-1.6-2.1c-.2-.3 0-.5.1-.7l.6-.8c.1-.2.1-.4 0-.6l-.9-2.1c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 00-.9.4A3.5 3.5 0 005.9 9c0 1.3.5 2.6 1.1 3.7a12 12 0 004.6 4.4c2.3 1.1 3.2 1 3.8.9a3.2 3.2 0 002.1-1.5 2.6 2.6 0 00.2-1.5c-.1-.2-.2-.4-.4-.5zM12 22a10 10 0 01-5.1-1.4L2 22l1.4-4.8A10 10 0 1112 22z"/></svg>Escríbenos</a>
        <a class="btn btn-linea-clara" href="/tiendas" data-ir="tiendas">Ver tiendas</a>
      </div>
    </div>
  </section>
  <script type="application/ld+json">%(servld)s</script>
  <script type="application/ld+json">%(faqld)s</script>
</main>
''' % dict(p, H1=p['h1'].upper(), cuerpo=cuerpo, rel=rel, faq=faq_html,
           servld=serv_ld, faqld=faq_ld, waurl=WA + p['wa'])
