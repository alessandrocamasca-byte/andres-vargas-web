import json, re

SITIO = 'https://sastreriaandresvargas.pe'
FECHA = '2026-08-30'
FECHA_TXT = '30 de agosto de 2026'


def figura(f):
    src, w, h, alt, pie = f
    return ('<figure class="fig-art">'
            '<img src="%s" alt="%s" loading="lazy" width="%d" height="%d">'
            '<figcaption>%s</figcaption></figure>' % (src, alt, w, h, pie))


def cuerpo(a, E):
    # Las fuentes externas se escriben una sola vez y se referencian por clave,
    # así no hay dos URLs distintas del mismo sitio repartidas por los textos.
    subs = {k.upper(): '<a href="%s" target="_blank" rel="noopener">%s</a>' % v
            for k, v in E.items()}
    subs['FIG1'] = figura(a['fig'][0])
    subs['FIG2'] = figura(a['fig'][1])
    # Sustitución por token y no por formateo: los textos llevan «100% lana» y
    # el % suelto rompería cualquier plantilla con formato.
    return re.sub(r'%\((\w+)\)s', lambda m: subs[m.group(1)], a['cuerpo'])


def seccion(a, E):
    rel = '\n'.join(
        '        <a class="puerta rev"%s href="%s">\n'
        '          <span class="puerta-cuerpo"><b>%s</b></span>\n'
        '        </a>' % ((' data-d="%d"' % i if i else ''), u, t)
        for i, (u, t) in enumerate(a['rel']))

    faq_html = '\n'.join(
        '          <details>\n'
        '            <summary>%s</summary>\n'
        '            <p>%s</p>\n'
        '          </details>' % (q, r) for q, r in a['faq'])

    # El FAQPage solo describe preguntas que están visibles en la página, que es
    # lo que Google exige. Salen de la misma lista, así que no se desincronizan.
    faq_ld = json.dumps({
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q,
                        'acceptedAnswer': {'@type': 'Answer',
                                           'text': re.sub(r'<[^>]+>', '', r)}}
                       for q, r in a['faq']],
    }, ensure_ascii=False, separators=(',', ':'))

    art_ld = json.dumps({
        '@context': 'https://schema.org', '@type': 'Article',
        'headline': a['h1'], 'description': a['desc'],
        'image': SITIO + a['img'],
        'datePublished': FECHA, 'dateModified': FECHA,
        'inLanguage': 'es-PE', 'articleSection': a['cat'],
        'about': {'@type': 'Thing', 'name': 'Sastrería a medida'},
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
      <article class="articulo medida centro rev">
%(cuerpo)s
      </article>
    </div>
  </section>

  <section class="seccion fondo-nube">
    <div class="caja">
      <div class="enc"><span class="rotulo">Preguntas frecuentes</span><h2 class="t-xl">Lo que más nos preguntan</h2></div>
      <div class="faq medida" style="margin-top:2rem;">
%(faq)s
      </div>
    </div>
  </section>

  <section class="seccion">
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
  <script type="application/ld+json">%(artld)s</script>
  <script type="application/ld+json">%(faqld)s</script>
</main>
''' % dict(a, H1=a['h1'].upper(), cuerpo=cuerpo(a, E), faq=faq_html, rel=rel,
           artld=art_ld, faqld=faq_ld, fecha=FECHA, fechaTxt=FECHA_TXT)
