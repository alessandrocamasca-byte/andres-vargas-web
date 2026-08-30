# -*- coding: utf-8 -*-
"""Escribe en index.html las muestras de tela de las páginas de colección y de
color, y sus datos estructurados.

Se hace aquí y no en el navegador porque los rastreadores de IA no ejecutan
JavaScript: si la rejilla se pinta con fetch, para ellos la página está vacía.
Y los datos estructurados solo pueden describir lo que se ve en la página, así
que ambos salen de la misma lista y no se pueden desincronizar.

Uso:  python3 herramientas/telas-paginas.py
"""
import json, re, html, collections, os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = 'https://sastreriaandresvargas.pe'
CASA = 'Barrington'
MUESTRAS = 12  # divisible entre 6, 4, 3 y 2: la última fila nunca queda coja

NOMBRE = {'negro': 'Negro', 'azul': 'Azul', 'gris': 'Gris', 'burdeos': 'Burdeos',
          'marron': 'Marrón', 'beige': 'Beige', 'celeste': 'Celeste', 'verde': 'Verde'}

# Cada página declara el filtro con el que se queda, en los mismos términos que
# usa el catálogo, para que el botón «ver todas» lleve exactamente a lo mismo.
COLECCIONES = {
    'tela-s100': [('g', 'Super 100s')], 'tela-s120': [('g', 'Super 120s')],
    'tela-s140': [('g', 'Super 140s')], 'tela-casimir': [('j', 'Casimir')],
    'tela-lanilla': [('j', 'Lanilla')], 'tela-richwool': [('j', 'Casimir Richwool')],
    'tela-superfine': [('j', 'Superfine')], 'tela-tweed': [('j', 'Tweed')],
    'tela-pano': [('j', 'Paño')], 'tela-denim': [('j', 'Denim')],
    'tela-alpaca': [('j', 'Baby alpaca velour'), ('j', 'Baby alpaca suri')],
}
COLORES = ['azul', 'negro', 'gris', 'burdeos', 'marron', 'beige']


def cargar():
    d = json.load(open(os.path.join(RAIZ, 'assets/telas.json'), encoding='utf-8'))
    return d['telas'] if isinstance(d, dict) else d


def filtrar(telas, pares):
    campos = collections.defaultdict(list)
    for c, v in pares:
        campos[c].append(v)
    return [x for x in telas
            if all(any(v in x.get('u', []) if c == 'u' else x.get(c) == v for v in vs)
                   for c, vs in campos.items())]


def muestrear(lista):
    """Reparte las muestras por toda la colección en lugar de tomar las doce
       primeras, que en este catálogo son variaciones del mismo diseño."""
    if len(lista) <= MUESTRAS:
        return lista
    paso = len(lista) / MUESTRAS
    return [lista[int(i * paso)] for i in range(MUESTRAS)]


def rejilla(muestras):
    fig = []
    for t in muestras:
        alt = 'Tela %s de %s, %s %s' % (t['c'], CASA, t['j'].lower(),
                                        NOMBRE.get(t['o'], t['o']).lower())
        fig.append(
            '        <figure>'
            '<img src="/assets/telas/%s" alt="%s" loading="lazy" width="480" height="319">'
            '<figcaption><b>%s</b><span>%s</span></figcaption></figure>'
            % (t.get('i2') or t['i'], html.escape(alt, quote=True),
               html.escape(t['c']), html.escape(t.get('g') or t['j'])))
    return '\n'.join(fig)


def datos(muestras, nombre, url):
    """ItemList de exactamente las telas que se ven. Sin totales: el cliente no
       publica cuántas telas hay fuera del catálogo."""
    d = {'@context': 'https://schema.org', '@type': 'ItemList',
         'name': nombre, 'url': SITIO + url, 'itemListElement': []}
    for i, t in enumerate(muestras, 1):
        p = {'@type': 'Product', 'name': t['c'], 'sku': t['c'],
             'category': 'Tela para sastrería a medida',
             'brand': {'@type': 'Brand', 'name': CASA},
             'color': NOMBRE.get(t['o'], t['o']),
             'material': t.get('comp') or t['j'],
             'image': SITIO + '/assets/telas/' + (t.get('i2') or t['i'])}
        d['itemListElement'].append({'@type': 'ListItem', 'position': i, 'item': p})
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(d, ensure_ascii=False, separators=(',', ':')))


# El texto de cada color es de sastrería, no del cliente: cuándo se lleva y
# qué pide. Nada que no se pueda sostener delante de un sastre.
PAGS_COLOR = [
 dict(slug='terno-azul', pag='color-azul', color='azul', h1='Terno azul',
   titulo='Terno Azul a Medida en Lima | Andrés Vargas',
   desc='Telas azules para terno a medida: casimir, superfine y lanilla de Barrington. Sastrería en Lima desde 1982.',
   lead='El que más se usa y el que mejor se lleva con todo.',
   cuerpo='Es el color con el que se empieza. Sirve en la oficina, en un matrimonio y en una entrevista, y va desde el marino cerrado hasta el azul con microdiseño que solo se ve de cerca. Si vas a mandarte hacer un solo terno, hazlo azul.'),
 dict(slug='terno-negro', pag='color-negro', color='negro', h1='Terno negro',
   titulo='Terno Negro a Medida en Lima | Andrés Vargas',
   desc='Telas negras para terno a medida: casimir, lanilla y superfine de Barrington. Sastrería en Lima desde 1982.',
   lead='El de las fechas señaladas, y el que menos perdona la tela.',
   cuerpo='El negro no tiene matices donde esconderse: se le ve todo, la caída, el corte y la calidad del paño. Por eso es el color donde más se nota la diferencia entre una tela buena y una regular. Es el terno de la ceremonia y de la noche.'),
 dict(slug='terno-gris', pag='color-gris', color='gris', h1='Terno gris',
   titulo='Terno Gris a Medida en Lima | Andrés Vargas',
   desc='Telas grises para terno a medida, del gris medio de oficina al oxford de ocasión. Barrington en Lima.',
   lead='El más versátil después del azul, y el más discreto de todos.',
   cuerpo='El gris no llama la atención, y ese es el punto. El gris medio va a la oficina todos los días; el oxford, más oscuro, aguanta una ocasión formal; el claro es de día y de verano. Combina con más camisas y más corbatas que ningún otro color.'),
 dict(slug='terno-burdeos', pag='color-burdeos', color='burdeos', h1='Terno burdeos',
   titulo='Terno y Saco Burdeos a Medida en Lima | Andrés Vargas',
   desc='Telas burdeos y guinda para terno, saco y abrigo a medida, en casimir, tweed y paño. Lima, desde 1982.',
   lead='Para el que ya tiene el azul y el gris.',
   cuerpo='No es un primer terno. Es el saco con el que se sale de la rutina sin disfrazarse: se lleva de noche, en una celebración y con pantalón gris o negro. En tweed y en paño da un abrigo con carácter.'),
 dict(slug='terno-marron', pag='color-marron', color='marron', h1='Terno marrón',
   titulo='Terno y Saco Marrón a Medida en Lima | Andrés Vargas',
   desc='Telas marrones para saco sport, terno y abrigo a medida, en tweed, casimir y lanilla. Barrington en Lima.',
   lead='El color del sport, del tweed y del fin de semana.',
   cuerpo='El marrón es el que menos pisa la oficina y el que más se agradece fuera de ella. Va con el tweed y con la lanilla, se lleva con camisa clara y sin corbata, y admite el zapato marrón que el azul y el negro complican.'),
 dict(slug='terno-beige', pag='color-beige', color='beige', h1='Terno beige',
   titulo='Terno Beige y Arena a Medida en Lima | Andrés Vargas',
   desc='Telas beige y arena para terno de día y de verano, en casimir y baby alpaca. Sastrería a medida en Lima.',
   lead='El de verano, el de día y el de matrimonio al aire libre.',
   cuerpo='El beige es de luz: funciona cuando hay sol y espacio abierto. Pide camisa blanca y poco más. Es un color que se ensucia a la vista, así que se usa cuando se va a lucir, no cuando se va a trabajar.'),
]


def ficha(xs, extra=()):
    filas = list(extra)
    for et, campo in [('Tejidos', 'j'), ('Composición', 'comp'), ('Peso', 'p')]:
        v = [k for k, _ in collections.Counter(x.get(campo) for x in xs if x.get(campo)).most_common(3)]
        if v:
            filas.append((et, ' · '.join(v)))
    usos = [k for k, _ in collections.Counter(u for x in xs for u in x.get('u', [])).most_common()]
    if usos:
        filas.append(('Uso', ' · '.join(usos)))
    grados = sorted({x['g'] for x in xs if x.get('g')})
    if grados:
        filas.append(('Grado', ' · '.join(grados)))
    return '\n'.join('          <div><dt>%s</dt><dd>%s</dd></div>' % (a, html.escape(b))
                     for a, b in filas)


def seccion_color(p, telas):
    xs = filtrar(telas, [('o', p['color'])])
    muestras = muestrear(xs)
    portada = xs[0]['i']
    filtro = 'color=' + p['color']
    return '''
<!-- ==================== COLOR · %(H1)s ==================== -->
<main class="pagina" data-pag="%(pag)s">
  <section class="pag-hero sobre-azul">
    <img class="pag-hero-img" src="/assets/telas/%(portada)s" alt="Tela %(colorNom)s de %(casa)s para terno a medida" loading="lazy" width="480" height="319">
    <div class="pag-hero-velo"></div>
    <div class="caja">
      <div class="miga"><a href="/" data-ir="inicio">Inicio</a> · <a href="/telas" data-ir="telas">Telas</a> · %(h1)s</div>
      <span class="rotulo">Color</span>
      <h1 class="t-hero">%(h1)s</h1>
      <p class="lead medida" style="margin-top:1.25rem;">%(lead)s</p>
    </div>
  </section>

  <section class="seccion">
    <div class="caja dos-col">
      <div class="rev">
        <div class="marca-div izq"><i></i></div>
        <span class="rotulo">El color</span>
        <h2 class="t-xl">Cuándo se lleva</h2>
        <p class="lead" style="margin-top:1.25rem;">%(cuerpo)s</p>
        <div class="acciones" style="margin-top:2rem;">
          <a class="btn btn-azul" href="/catalogo-de-telas?%(filtro)s">Ver estas telas</a>
          <a class="btn btn-linea" href="/ternos-a-medida" data-ir="trajes">El terno a medida</a>
        </div>
      </div>
      <div class="rev" data-d="1">
        <dl class="cat-datos ficha-tela">
%(ficha)s
        </dl>
      </div>
    </div>
  </section>

  <section class="seccion fondo-nube">
    <div class="caja">
      <div class="enc centro">
        <span class="rotulo">Del muestrario</span>
        <h2 class="t-xl">Algunas de estas telas</h2>
      </div>
      <div class="rejilla-telas" data-telas="%(filtro)s">
%(rejilla)s
      </div>
      %(ld)s
      <div style="text-align:center;margin-top:2.2rem;">
        <a class="btn btn-azul" href="/catalogo-de-telas?%(filtro)s">Ver todas en el catálogo</a>
      </div>
    </div>
  </section>

  <section class="seccion-corta fondo-azul sobre-azul con-foto" style="--foto:url('/assets/editorial/ed-macro-orillo.jpg');">
    <div class="caja centro">
      <h2 class="t-xl">¿Quieres verlas en persona?</h2>
      <p class="lead centro medida" style="margin-top:1rem;">Escríbenos y te decimos disponibilidad, o pásate por cualquiera de nuestras seis tiendas de Lima a verlas y tocarlas.</p>
      <div class="acciones" style="justify-content:center;margin-top:2rem;">
        <a class="btn btn-claro" href="https://wa.me/51959370397?text=%(wa)s" target="_blank" rel="noopener">Escríbenos</a>
        <a class="btn btn-linea-clara" href="/tiendas" data-ir="tiendas">Ver tiendas</a>
      </div>
    </div>
  </section>
</main>
''' % dict(p, H1=p['h1'].upper(), casa=CASA, portada=portada, filtro=filtro,
           colorNom=NOMBRE[p['color']].lower(),
           ficha=ficha(xs), rejilla=rejilla(muestras),
           ld=datos(muestras, 'Telas ' + NOMBRE[p['color']].lower() + ' de ' + CASA, '/' + p['slug']),
           wa='Hola%2C%20quiero%20consultar%20por%20telas%20' + NOMBRE[p['color']].lower() + '.')


NOMBRE_COL = {'tela-s100': 'Telas Super 100s', 'tela-s120': 'Telas Super 120s',
              'tela-s140': 'Telas Super 140s', 'tela-casimir': 'Telas de casimir',
              'tela-lanilla': 'Telas de lanilla', 'tela-richwool': 'Telas Casimir Richwool',
              'tela-superfine': 'Telas Superfine', 'tela-tweed': 'Telas de tweed',
              'tela-pano': 'Telas de paño', 'tela-denim': 'Telas de denim',
              'tela-alpaca': 'Telas de baby alpaca'}
RUTA_COL = {'tela-s100': '/telas/super-100s', 'tela-s120': '/telas/super-120s',
            'tela-s140': '/telas/super-140s', 'tela-casimir': '/telas/casimir',
            'tela-lanilla': '/telas/lanilla', 'tela-richwool': '/telas/richwool',
            'tela-superfine': '/telas/superfine', 'tela-tweed': '/telas/tweed',
            'tela-pano': '/telas/pano', 'tela-denim': '/telas/denim',
            'tela-alpaca': '/telas/baby-alpaca'}

MARCA_INI = '<!-- === PÁGINAS DE COLOR (generadas por herramientas/telas-paginas.py) === -->'
MARCA_FIN = '<!-- === FIN PÁGINAS DE COLOR === -->'


def main():
    telas = cargar()
    ruta = os.path.join(RAIZ, 'index.html')
    s = open(ruta, encoding='utf-8').read()

    # 1. Rejilla y datos estructurados de las once páginas de colección
    for pag, pares in COLECCIONES.items():
        muestras = muestrear(filtrar(telas, pares))
        ini = s.index('data-pag="%s"' % pag)
        fin = s.index('</main>', ini)
        bloque = s[ini:fin]
        nuevo, n = re.subn(
            r'(<div class="rejilla-telas" data-telas="[^"]*">).*?(</div>)'
            r'(\s*<script type="application/ld\+json">.*?</script>)?',
            lambda m: '%s\n%s\n      %s\n      %s' % (
                m.group(1), rejilla(muestras), m.group(2),
                datos(muestras, NOMBRE_COL[pag], RUTA_COL[pag])),
            bloque, count=1, flags=re.S)
        assert n == 1, pag
        s = s[:ini] + nuevo + s[fin:]

    # 2. Las seis páginas de color, entre marcas para poder reescribirlas
    cuerpo = MARCA_INI + '\n' + '\n'.join(seccion_color(p, telas) for p in PAGS_COLOR) + '\n' + MARCA_FIN
    if MARCA_INI in s:
        s = re.sub(re.escape(MARCA_INI) + '.*?' + re.escape(MARCA_FIN), lambda _: cuerpo, s, flags=re.S)
    else:
        i = s.rindex('</main>') + len('</main>')
        s = s[:i] + '\n\n' + cuerpo + s[i:]

    open(ruta, 'w', encoding='utf-8').write(s)
    print('%d colecciones y %d colores escritos en index.html' % (len(COLECCIONES), len(PAGS_COLOR)))


if __name__ == '__main__':
    main()


# Frase corta de cada color para el bloque de entrada desde /telas. Es lo único
# que se repite entre esa rejilla y la página de destino, y va resumido.
PICO = {'azul': 'El que sirve para todo: oficina, matrimonio y entrevista.',
        'negro': 'El de la ceremonia y la noche, donde más se nota la tela.',
        'gris': 'El más discreto, y el que combina con más camisas.',
        'burdeos': 'Para el que ya tiene el azul y el gris.',
        'marron': 'El del saco sport, el tweed y el fin de semana.',
        'beige': 'El de verano, de día y al aire libre.'}

MARCA_INI_C = '<!-- === ENTRADA POR COLOR (generada por herramientas/telas-paginas.py) === -->'
MARCA_FIN_C = '<!-- === FIN ENTRADA POR COLOR === -->'


def bloque_colores(telas):
    """Sin este bloque las seis páginas de color quedan huérfanas: solo se
       llegaría por el sitemap, y una página sin enlaces internos no compite."""
    puertas = []
    for p in PAGS_COLOR:
        xs = filtrar(telas, [('o', p['color'])])
        puertas.append(
            '        <a class="puerta rev" href="/%s" data-ir="%s">\n'
            '          <span class="puerta-foto"><img src="/assets/telas/%s" alt="Tela %s de %s para terno a medida" loading="lazy" width="480" height="319"></span>\n'
            '          <span class="puerta-cuerpo"><b>%s</b><em>%s</em></span>\n'
            '        </a>'
            % (p['slug'], p['pag'], xs[0]['i'], NOMBRE[p['color']].lower(), CASA,
               p['h1'], PICO[p['color']]))
    return '''%s
  <section class="seccion">
    <div class="caja">
      <div class="enc">
        <span class="rotulo">Entender la tela · 03</span>
        <h2 class="t-xl">Y luego está el color</h2>
        <p class="lead" style="margin-top:1rem;">El grado dice cómo de fino es el hilo y el tejido de qué está hecha la tela. El color decide cuándo te la vas a poner. Estos son los seis del muestrario, con lo que resuelve cada uno.</p>
      </div>
      <div class="puertas">
%s
      </div>
    </div>
  </section>
  %s''' % (MARCA_INI_C, '\n'.join(puertas), MARCA_FIN_C)
