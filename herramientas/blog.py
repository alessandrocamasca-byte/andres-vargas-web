# -*- coding: utf-8 -*-
"""Los seis artículos del blog. El texto vive aquí y se inserta en index.html.

Regla que se respeta en todos: nada de plazos, cifras ni casos que la web no
pueda sostener. Cuando el dato depende del encargo, se dice que depende y se
manda a preguntar, que además es lo que queremos que haga el lector.
"""
FECHA = '2026-08-30'
FECHA_TXT = '30 de agosto de 2026'

ARTS = [
{
 'slug':'primer-traje-a-medida', 'pag':'art-primer-traje', 'cat':'Guías',
 'h1':'Cómo elegir tu primer traje a medida',
 'titulo':'Cómo Elegir tu Primer Traje a Medida | Andrés Vargas',
 'desc':'Qué decidir antes de ir al sastre, qué llevar a la primera cita y el error que casi todos cometen con la tela. Guía de Andrés Vargas, Lima.',
 'img':'/assets/editorial/ed-oficina-azul.jpg', 'w':848, 'h':1106,
 'alt':'Terno azul a medida',
 'lead':'Casi todos llegan con la misma frase: «azul, elegante, que me quede bien». Sirve para empezar, pero hay tres decisiones que conviene traer tomadas de casa.',
 'cuerpo':'''
<h2 class="t-xl">Lo primero no es el color</h2>
<p class="lead">Es cuántas veces al mes te lo vas a poner. Suena a pregunta menor y es la que más condiciona todo lo demás; sin embargo casi nadie llega con la respuesta preparada. Un terno para tres matrimonios al año y uno que sale de casa de martes a viernes no se construyen con la misma tela, ni con el mismo forro, ni con los mismos refuerzos, aunque de lejos se parezcan bastante.</p>
<p class="lead">Si vas a usarlo mucho, lo que necesitas es un tejido que aguante y vuelva a su sitio al colgarlo. Si es para ocasiones contadas, ahí sí tiene sentido irse a algo más fino, porque no va a sufrir el roce diario del maletín y del asiento del carro.</p>

<h2 class="t-xl">Trae los zapatos</h2>
<p class="lead">Los que vas a usar con ese terno, no unos parecidos que tengas a la mano. El largo del pantalón se marca con el zapato puesto y dos centímetros de taco mueven el quiebre lo suficiente como para que se note. Es el arreglo que más veces nos toca rehacer, y siempre por lo mismo.</p>
<p class="lead">Si el terno es para una fecha concreta, dila en la primera cita. No al final, cuando ya elegiste tela: la disponibilidad del tejido y el número de pruebas dependen de esa fecha, y a veces conviene elegir otra tela sencillamente porque llega antes.</p>

<h2 class="t-xl">El error más común con la tela</h2>
<p class="lead">Pensar que el número más alto es el mejor. Ese número, el que va detrás de la palabra Super, mide la finura del hilo: cuanto más alto, más delgada la fibra, más suave el tacto y mejor la caída. También más delicada la prenda.</p>
<p class="lead">De ahí que un grado alto sea excelente para el terno que se usa poco y una mala idea para el que va a la oficina todos los días. La <a href="/telas/super-100s">Super 100s</a> es la que resiste el uso continuo; la <a href="/telas/super-140s">Super 140s</a> es la de gala. Ninguna es mejor que la otra, son para cosas distintas, y confundirlas cuesta caro porque el desgaste se ve al año.</p>

<h2 class="t-xl">Si vas a tener uno solo, que sea azul</h2>
<p class="lead">El <a href="/terno-azul">azul</a> entra en la oficina, en un matrimonio y en una entrevista sin llamar la atención en ninguno de los tres sitios. El negro es más específico de lo que la gente cree: funciona de noche y en ceremonia, y de día, en una reunión, se ve fuera de lugar. El gris es la segunda opción más segura.</p>
<p class="lead">Con un azul de microdiseño puedes cambiar de camisa y de corbata y parecer que llevas ternos distintos. Es lo más rentable que puedes hacer con una primera prenda.</p>

<h2 class="t-xl">Qué pasa en la cita</h2>
<p class="lead">Conversamos sobre para qué es la prenda, vemos telas, tomamos medidas. Después el taller construye el terno sobre tu patrón y volvemos a vernos en las pruebas, que son donde de verdad se decide la caída. Ven sin apuro: elegir bien la tela toma más rato del que la gente calcula, y es la parte que no se puede corregir después.</p>
''',
 'wa':'Hola%2C%20quiero%20agendar%20una%20cita%20para%20mi%20primer%20terno%20a%20medida.',
 'rel':[('/a-medida','Cómo trabajamos'),('/telas','Las telas'),('/tiendas','Dónde estamos')],
},
{
 'slug':'tela-nacional-o-importada', 'pag':'art-nacional-importada', 'cat':'Telas',
 'h1':'Nacional o importada: cómo decidir',
 'titulo':'Tela Nacional o Importada para tu Terno | Andrés Vargas',
 'desc':'Qué cambia de verdad entre una tela peruana y una importada, y por qué la mejor fibra del mundo para abrigo es nacional. Andrés Vargas, Lima.',
 'img':'/assets/editorial/ed-macro-super100-fondo.jpg', 'w':900, 'h':1285,
 'alt':'Orillo de una tela Super 100s',
 'lead':'La pregunta llega casi siempre planteada como una jerarquía: importada arriba, nacional abajo. En sastrería no funciona así, y el mejor contraejemplo lo tenemos en casa.',
 'cuerpo':'''
<h2 class="t-xl">Empecemos por el contraejemplo</h2>
<p class="lead">La <a href="/telas/baby-alpaca">baby alpaca</a> es peruana y es una de las fibras más apreciadas del planeta. La variedad suri, de hebra larga y rizada, tiene un brillo y una ligereza que no da ninguna lana; el velour lleva el pelo corto y aterciopelado. Cuando alguien pide «lo mejor que tengas» para un abrigo, la respuesta no viene de Italia.</p>
<p class="lead">Así que la primera corrección es esa: nacional no significa segunda opción. Significa otra cosa.</p>

<h2 class="t-xl">Qué cambia realmente</h2>
<p class="lead">Lo que separa a una tela de otra no es la bandera del rollo, sino cuatro cosas concretas: de qué está hecha, cómo está tejida, cómo está acabada y si vas a poder conseguir más si la necesitas.</p>
<ul class="lista lead">
  <li><b>La fibra.</b> Un <a href="/telas/casimir">casimir</a> de lana merino se comporta igual venga de donde venga. Lo que cambia el resultado es el porcentaje: 100% lana cae distinto que una mezcla con poliéster, y eso lo lees en la etiqueta, no en el origen.</li>
  <li><b>El acabado.</b> Aquí sí hay tradición. Las casas europeas llevan siglos afinando el rasado y el batanado, y se nota al tacto.</li>
  <li><b>La reposición.</b> Si dentro de un año quieres el pantalón que hace juego, con una tela de stock lo tienes; con una importada de colección puntual, a veces no. A nadie le importa hasta que le pasa.</li>
  <li><b>El clima al que está pensada.</b> Una tela diseñada para el invierno inglés en Lima te va a dar calor casi todo el año.</li>
</ul>

<h2 class="t-xl">El clima de Lima decide más de lo que crees</h2>
<p class="lead">Lima es templada y húmeda buena parte del año, sin el frío que justifica un paño grueso ni el calor seco que pide lino. Por eso la <a href="/telas/lanilla">lanilla</a> funciona tan bien aquí: ligera, con la caída de la lana y sin el peso de un tejido de invierno. Y por eso el <a href="/telas/tweed">tweed</a>, que es magnífico, se queda para el saco de fin de semana y no para el terno de todos los días.</p>

<h2 class="t-xl">Cómo lo decidimos nosotros</h2>
<p class="lead">Preguntando para qué es la prenda y descartando desde ahí. Un terno de oficina que se usa cuatro días por semana pide resistencia, y ahí un <a href="/telas/richwool">Casimir Richwool</a> hace mejor trabajo que una tela más noble que se va a marcar en los codos. Un traje de gala pide caída, y entonces subimos de grado.</p>
<p class="lead">Somos distribuidores oficiales, así que trabajamos con tejeduría peruana y con casas italianas e inglesas dentro del mismo muestrario. Eso quita el problema de raíz: no hay que defender un origen, se elige el tejido que corresponde y se acabó. Puedes verlo <a href="/catalogo-de-telas">tela por tela en el catálogo</a>.</p>
''',
 'wa':'Hola%2C%20quiero%20asesor%C3%ADa%20para%20elegir%20la%20tela%20de%20mi%20prenda.',
 'rel':[('/catalogo-de-telas','El catálogo'),('/telas','Las marcas'),('/telas/casimir','Casimir')],
},
{
 'slug':'calendario-del-novio', 'pag':'art-calendario-novio', 'cat':'Novios',
 'h1':'Calendario del novio: cuándo empezar',
 'titulo':'Calendario del Novio: Cuándo Empezar el Traje | Andrés Vargas',
 'desc':'Qué determina el tiempo de un traje de novio a medida y en qué orden conviene resolver cada cosa para llegar tranquilo al día de la boda.',
 'img':'/assets/novios-duo.jpg', 'w':801, 'h':1200,
 'alt':'Trajes de novio a medida',
 'lead':'No hay un número que sirva para todos, y desconfía del que te lo dé sin preguntarte nada. Lo que sí se puede decir es qué alarga el calendario y en qué orden conviene resolverlo.',
 'cuerpo':'''
<h2 class="t-xl">Por qué no hay una cifra única</h2>
<p class="lead">Un traje a medida se construye con pruebas, y las pruebas necesitan calendario. Cuántas hagan falta depende de la prenda y del cuerpo; cuánto tarde <a href="/catalogo-de-telas">la tela</a> depende de si está en stock o hay que traerla; y cuánto se demore todo depende también de en qué mes te cases, porque hay temporadas con mucha más carga que otras.</p>
<p class="lead">Por eso, cuando nos escribes, lo primero que preguntamos es la fecha. Con la fecha en la mano te decimos con qué margen estás y qué telas llegan a tiempo. Sin ella cualquier plazo que te demos es inventado.</p>

<h2 class="t-xl">El orden importa más que el adelanto</h2>
<p class="lead">Empezar con seis meses y decidir la tela en el último mes no sirve de nada. Lo que ordena el calendario es esta secuencia:</p>
<ul class="lista lead">
  <li>Fija primero <b>hora y lugar</b> de la boda. Una ceremonia de día al aire libre y una de noche en salón no piden el mismo traje, y esa decisión condiciona el color y el peso del tejido.</li>
  <li>Después, <b>la tela</b>. Es lo que puede tener plazo de por medio y lo único que no se corrige más adelante.</li>
  <li>Luego <b>las medidas y las pruebas</b>, que son las que necesitan que tu peso esté estable. Si estás en un plan de entrenamiento fuerte, dilo: se puede trabajar con eso, pero hay que saberlo antes de cortar.</li>
  <li>Al final, <b>los complementos</b> y el cortejo.</li>
</ul>

<h2 class="t-xl">El cortejo es lo que más se subestima</h2>
<p class="lead">Vestir a <a href="/trajes-de-novio">los padrinos, al padre y a los hermanos</a> multiplica las tomas de medida y las pruebas, y hay que cuadrar la agenda de varias personas que no siempre viven en la misma ciudad. Si quieres que el conjunto se vea coherente en las fotos, esa parte hay que arrancarla casi a la vez que la tuya, no cuando ya tengas el tuyo listo.</p>

<h2 class="t-xl">Dos cosas que nadie te avisa</h2>
<p class="lead">La primera: reserva una prueba cerca de la fecha, no todas al principio. El cuerpo cambia en los meses previos a una boda, casi siempre en la misma dirección, y esa última prueba es la que salva la caída.</p>
<p class="lead">La segunda: prueba el traje completo, con la camisa, los zapatos y los gemelos que vas a llevar. Es la única forma de descubrir a tiempo que la manga tapa el puño o que el pantalón se arrastra con esos zapatos y no con los otros.</p>
<p class="lead">La experiencia de novios la hacemos en <a href="/tiendas">la tienda de Surco</a>, y puedes venir acompañado; de hecho es mejor. Escríbenos con tu fecha y te decimos con qué margen cuentas.</p>
''',
 'wa':'Hola%2C%20me%20caso%20el%20%5Bfecha%5D%20y%20quiero%20saber%20con%20qu%C3%A9%20margen%20cuento.',
 'rel':[('/trajes-de-novio','El servicio de novios'),('/telas','Las telas'),('/tiendas','Tienda de Surco')],
},
{
 'slug':'codigo-de-vestimenta', 'pag':'art-etiqueta', 'cat':'Estilo',
 'h1':'Etiqueta: qué se espera de un código de vestimenta',
 'titulo':'Códigos de Vestimenta: Qué Significa Cada Uno | Andrés Vargas',
 'desc':'Traducción práctica de lo que dice la invitación: etiqueta rigurosa, etiqueta, formal, terno oscuro y casual elegante, con lo que se espera en Lima.',
 'img':'/assets/editorial/ed-gala-pinstripe.jpg', 'w':990, 'h':1120,
 'alt':'Traje cruzado de gala',
 'lead':'La invitación dice dos palabras y tú tienes que deducir una prenda. Esta es la traducción, de lo más estricto a lo más suelto, con lo que de verdad se estila aquí.',
 'cuerpo':'''
<h2 class="t-xl">Etiqueta rigurosa</h2>
<p class="lead">Frac de noche, chaqué de día. Es el nivel más alto y casi nunca lo vas a ver escrito en Lima fuera de actos protocolares, alguna ceremonia académica y bodas muy formales. Si la invitación lo pide, lo pide en serio: no se resuelve con un terno negro.</p>
<p class="lead">El chaqué es la versión diurna, con pantalón de raya diplomática y levita; el frac es la nocturna, con corbatín blanco y chaleco blanco. Confundir uno con otro es el error clásico.</p>

<h2 class="t-xl">Etiqueta o «black tie»</h2>
<p class="lead">Esmoquin. Solapa de raso, un solo botón, pantalón con galón lateral, corbatín negro. Camisa blanca y zapato negro. La tentación es sustituirlo por un terno negro con corbata negra y no es lo mismo: el raso de la solapa es justamente lo que distingue un esmoquin de un terno, y se nota a distancia.</p>
<p class="lead">Si la boda es de noche y la invitación dice etiqueta, esto es lo que están pidiendo.</p>

<h2 class="t-xl">Formal o «terno oscuro»</h2>
<p class="lead">Aquí ya estamos en terreno conocido. Terno de dos o tres piezas en azul marino, gris oxford o negro, camisa blanca o celeste, corbata. Es el código más frecuente en matrimonios limeños de noche y en cenas de empresa.</p>
<p class="lead">La palabra que hace el trabajo es «oscuro». Un <a href="/terno-gris">gris medio</a> de oficina cumple en una reunión pero se queda corto en una ceremonia; para eso está el oxford, más cerrado. Y el <a href="/terno-azul">azul marino</a> sirve para las dos cosas, que es la razón por la que recomendamos empezar por ahí.</p>

<h2 class="t-xl">Business o ejecutivo</h2>
<p class="lead">Terno con corbata, en tonos sobrios, pensado para trabajar. Aquí manda la resistencia del tejido por encima de la finura, porque la prenda va a salir de casa muchas veces al mes. Un microdiseño rompe la monotonía sin salirse del código.</p>

<h2 class="t-xl">Casual elegante</h2>
<p class="lead">El más traicionero de todos, porque cada quien lo entiende distinto. La lectura segura es saco y pantalón que no hagan juego: un blazer con pantalón de otro tono, camisa sin corbata. Un saco de <a href="/telas/tweed">tweed</a> o de <a href="/telas/superfine">Superfine</a> funciona perfecto en ese registro.</p>
<p class="lead">Lo que sí se espera, aunque no lo digan, es que la prenda esté a tu medida. Un saco holgado en una ocasión relajada se ve peor que en una formal, no mejor.</p>

<h2 class="t-xl">Y si la invitación no dice nada</h2>
<p class="lead">Guíate por la hora y el lugar. De noche y en salón, sube el nivel; de día y al aire libre, bájalo y aclara el tono. Ante la duda, azul marino con camisa blanca: no hay evento en el que se vea mal.</p>
''',
 'wa':'Hola%2C%20tengo%20un%20evento%20con%20c%C3%B3digo%20de%20vestimenta%20y%20quiero%20asesor%C3%ADa.',
 'rel':[('/ternos-a-medida','Trajes y ternos'),('/terno-azul','Terno azul'),('/trajes-de-novio','Novios')],
},
{
 'slug':'cuidar-un-traje', 'pag':'art-cuidado', 'cat':'Cuidado',
 'h1':'Cómo cuidar un traje para que dure',
 'titulo':'Cómo Cuidar un Traje para que Dure | Andrés Vargas',
 'desc':'Colgado, cepillado, descanso entre usos y por qué la tintorería frecuente arruina la lana. Cuidado del terno en el clima húmedo de Lima.',
 'img':'/assets/traje-burdeos.jpg', 'w':412, 'h':1000,
 'alt':'Traje burdeos a medida',
 'lead':'Un terno bien hecho puede durar años. Lo que lo mata no suele ser el uso, sino tres costumbres domésticas que parecen inofensivas.',
 'cuerpo':'''
<h2 class="t-xl">El gancho es la mitad del asunto</h2>
<p class="lead">Un gancho de alambre, de esos que devuelve la tintorería, concentra todo el peso del saco en dos puntos y con el tiempo deforma el hombro, que es justamente la parte más difícil de construir y la única que no se arregla del todo. Necesitas un gancho ancho, con curvatura, que sostenga el hombro entero.</p>
<p class="lead">El pantalón, colgado del bajo con pinzas y no doblado por la mitad: el propio peso de la tela estira la arruga y evita el planchado.</p>

<h2 class="t-xl">Cepillar en lugar de lavar</h2>
<p class="lead">Después de cada uso, un cepillo de cerda suave de arriba hacia abajo. Suena a manía de otra época y es lo más eficaz que puedes hacer: saca el polvo antes de que se meta en el tejido, que es lo que apaga el color y desgasta la fibra desde dentro.</p>
<p class="lead">Una mancha reciente sale con un paño húmedo y paciencia. La tintorería déjala para cuando de verdad haga falta, un par de veces al año como mucho, porque los solventes resecan <a href="/telas/casimir">la lana</a> y le quitan la elasticidad que hace que la prenda vuelva a su forma. El terno que se manda a limpiar cada mes envejece el triple de rápido.</p>

<h2 class="t-xl">Déjalo descansar</h2>
<p class="lead">La lana necesita entre uno y dos días para recuperar su forma después de un uso. Si tienes un solo terno y te lo pones a diario, se va a marcar en los codos y en las rodillas mucho antes de tiempo. Alternar dos prendas hace que las dos duren más que si usaras una sola hasta gastarla.</p>
<p class="lead">Al llegar a casa, cuélgalo fuera del clóset un rato antes de guardarlo. Que se ventile y se enfríe.</p>

<h2 class="t-xl">Lima tiene un problema propio</h2>
<p class="lead">La humedad. En los meses de garúa un clóset cerrado y sin ventilar es el sitio perfecto para que aparezca moho en la tela y para que la polilla se instale, porque la polilla busca lana y prefiere los rincones quietos. Ventila el clóset de vez en cuando y no guardes nunca una prenda húmeda ni recién usada.</p>
<p class="lead">Para la temporada en que no lo uses, funda de tela y no de plástico. El plástico no deja respirar al tejido y encierra la humedad justo contra la fibra.</p>

<h2 class="t-xl">Vapor, no plancha</h2>
<p class="lead">Casi todas las arrugas de un terno se van solas si cuelgas la prenda en el baño mientras te duchas. Si necesitas plancha, que sea con un paño de por medio y nunca directamente sobre la solapa ni sobre el bolsillo: el calor directo aplasta el relieve y deja un brillo en la tela que ya no se quita.</p>
<p class="lead">Y si algo se descosió o el pantalón te quedó ajustado, <a href="/tiendas">tráelo</a>. Arreglar a tiempo cuesta menos trabajo que rehacer.</p>
''',
 'wa':'Hola%2C%20quiero%20consultar%20por%20el%20arreglo%20de%20una%20prenda.',
 'rel':[('/a-medida','Cómo trabajamos'),('/tiendas','Nuestras tiendas'),('/telas','Las telas')],
},
{
 'slug':'salir-del-negro', 'pag':'art-color', 'cat':'Estilo',
 'h1':'Salir del negro sin equivocarse',
 'titulo':'Colores de Terno que Funcionan en Lima | Andrés Vargas',
 'desc':'Azul, gris, burdeos, marrón y beige: qué resuelve cada color de terno, con qué combinarlo y por qué la luz de Lima cambia cómo se ven.',
 'img':'/assets/editorial/ed-blazer-salmon.jpg', 'w':990, 'h':1064,
 'alt':'Blazer en tono claro',
 'lead':'El negro es el color con el que casi todos empiezan y el que menos ocasiones resuelve. Lo que sigue no es una regla de moda: es qué hace cada color y dónde se rompe.',
 'cuerpo':'''
<h2 class="t-xl">Primero, por qué el negro no es la opción segura</h2>
<p class="lead">Lo parece porque es el color de lo formal, pero en la práctica es de los más específicos que hay. El <a href="/terno-negro">negro</a> funciona de noche, en ceremonia y en velorio; a plena luz del día, en una oficina o en un almuerzo de trabajo, se lee duro y fuera de tono.</p>
<p class="lead">Tiene además una exigencia que nadie menciona: no tiene matices donde esconderse. Se le ve todo, la caída, el corte y la calidad del paño. Es el color donde más se nota la diferencia entre una tela buena y una regular.</p>

<h2 class="t-xl">Azul, que es donde hay que empezar</h2>
<p class="lead">El <a href="/terno-azul">azul</a> hace lo que la gente cree que hace el negro: entra en cualquier sitio. Oficina, matrimonio, entrevista. Y tiene recorrido interno, desde el marino cerrado hasta el azul con microdiseño que solo se distingue de cerca, así que con dos prendas azules puedes verte distinto sin salirte de un terreno seguro.</p>
<p class="lead">Con camisa blanca es formal; con celeste baja un punto; con corbata burdeos sube. Es el color con más combinaciones posibles por sol invertido.</p>

<h2 class="t-xl">Gris, el que no llama la atención</h2>
<p class="lead">Y ese es exactamente su valor. El <a href="/terno-gris">gris</a> medio va a la oficina de lunes a viernes; el oxford, más oscuro, aguanta una ocasión formal de noche; el claro es de día y de verano. Combina con más camisas y más corbatas que cualquier otro, lo que lo hace la segunda compra más sensata después del azul.</p>

<h2 class="t-xl">El siguiente paso: burdeos, marrón, beige</h2>
<p class="lead">Estos ya no son primeros ternos, son la salida de la rutina. El <a href="/terno-burdeos">burdeos</a> se lleva bien de noche y en celebraciones, y con pantalón gris o negro funciona como saco suelto; en tweed o en paño da un abrigo con carácter.</p>
<p class="lead">El <a href="/terno-marron">marrón</a> es el color del sport y del fin de semana: pide camisa clara, va sin corbata sin verse incompleto y admite el zapato marrón que el azul y el negro complican. El <a href="/terno-beige">beige</a> es de luz, de día y de aire libre; pide camisa blanca y poco más, y se ensucia a la vista, así que es para lucirlo, no para trabajar con él.</p>

<h2 class="t-xl">La luz de Lima cambia las cuentas</h2>
<p class="lead">Buena parte del año el cielo de Lima está cubierto, y esa luz difusa apaga los tonos medios y aplana los contrastes. Un gris claro que en un catálogo se ve luminoso, aquí puede leerse lavado; un burdeos profundo, en cambio, gana. Por eso vale la pena ver la tela en la tienda, con luz natural, y no decidirla por una foto en el celular.</p>
<p class="lead">Si quieres ver los tonos uno por uno, están <a href="/catalogo-de-telas">en el catálogo, filtrados por color</a>.</p>
''',
 'wa':'Hola%2C%20quiero%20asesor%C3%ADa%20sobre%20el%20color%20de%20mi%20pr%C3%B3ximo%20terno.',
 'rel':[('/terno-azul','Terno azul'),('/terno-gris','Terno gris'),('/catalogo-de-telas','El catálogo')],
},
]


import json, html as H

SITIO = 'https://sastreriaandresvargas.pe'


def seccion(a):
    rel = '\n'.join(
        '        <a class="puerta rev"%s href="%s">\n'
        '          <span class="puerta-cuerpo"><b>%s</b></span>\n'
        '        </a>' % ((' data-d="%d"' % i if i else ''), u, t)
        for i, (u, t) in enumerate(a['rel']))
    ld = json.dumps({
        '@context': 'https://schema.org', '@type': 'Article',
        'headline': a['h1'],
        'description': a['desc'],
        'image': SITIO + a['img'],
        'datePublished': FECHA, 'dateModified': FECHA,
        'inLanguage': 'es-PE',
        'author': {'@type': 'Organization', 'name': 'Andrés Vargas Sastrería', 'url': SITIO},
        'publisher': {'@type': 'Organization', 'name': 'Andrés Vargas Sastrería',
                      'logo': {'@type': 'ImageObject', 'url': SITIO + '/assets/logo-azul.png'}},
        'mainEntityOfPage': {'@type': 'WebPage', '@id': SITIO + '/blog/' + a['slug']},
    }, ensure_ascii=False, separators=(',', ':'))
    return '''
<!-- ==================== ARTÍCULO · %(H1)s ==================== -->
<main class="pagina" data-pag="%(pag)s">
  <section class="pag-hero sobre-azul">
    <img class="pag-hero-img" src="%(img)s" alt="%(alt)s" loading="lazy" width="%(w)d" height="%(h)d">
    <div class="pag-hero-velo"></div>
    <div class="caja">
      <div class="miga"><a href="/" data-ir="inicio">Inicio</a> · <a href="/blog" data-ir="blog">Blog</a> · %(cat)s</div>
      <span class="rotulo">%(cat)s</span>
      <h1 class="t-hero">%(h1)s</h1>
      <p class="lead medida" style="margin-top:1.25rem;">%(lead)s</p>
      <p class="mini" style="margin-top:1.5rem;opacity:0.75;"><time datetime="%(fecha)s">%(fechaTxt)s</time> · Andrés Vargas Sastrería</p>
    </div>
  </section>

  <section class="seccion">
    <div class="caja">
      <article class="articulo medida rev">
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

  <section class="seccion-corta fondo-azul sobre-azul con-foto" style="--foto:url('/assets/editorial/ed-macro-orillo-fondo.jpg');">
    <div class="caja centro">
      <h2 class="t-xl">¿Te queda alguna duda?</h2>
      <p class="lead centro medida" style="margin-top:1rem;">Escríbenos y te responde un sastre, no un formulario. O pásate por cualquiera de nuestras seis tiendas de Lima.</p>
      <div class="acciones" style="justify-content:center;margin-top:2rem;">
        <a class="btn btn-claro" href="https://wa.me/51959370397?text=%(wa)s" target="_blank" rel="noopener">Escríbenos</a>
        <a class="btn btn-linea-clara" href="/blog" data-ir="blog">Ver el blog</a>
      </div>
    </div>
  </section>
  <script type="application/ld+json">%(ld)s</script>
</main>
''' % dict(a, H1=a['h1'].upper(), rel=rel, ld=ld, fecha=FECHA, fechaTxt=FECHA_TXT)
