# -*- coding: utf-8 -*-
"""Mete los seis artículos nuevos en index.html, el middleware y el sitemap.

Idempotente: si un artículo ya está instalado, lo salta. Así se puede volver a
correr después de retocar un texto sin duplicar nada.
"""
import re, sys
sys.path.insert(0, 'herramientas')
from blog_fuentes import E
from blog_render import seccion, FECHA, FECHA_TXT
from blog_textos2 import ARTS2

# Resumen de la tarjeta del listado: una frase, no la meta description entera.
TEASER = {
 'camisa-a-medida-lima': 'El cuello y el puño se deciden antes, y no se corrigen después.',
 'telas-italianas-en-lima': 'Cuándo una tela italiana es la decisión correcta y cuándo no.',
 'telas-barrington-muestrario-completo': 'Las 483 telas publicadas, con código y composición.',
 'sastreria-abierta-domingo-lima': 'Huallaga 558 y Chacarilla, domingos de 10 a 16.',
 'como-llegar-a-nuestras-tiendas': 'Seis tiendas, dos zonas y horarios que no son iguales.',
 'terno-a-medida-o-de-tienda': 'La diferencia está en el hombro, no en el forro.',
}

# ------------------------------------------------------------------ index.html
h = open('index.html', encoding='utf-8').read()
puestos = []
for a in ARTS2:
    if 'data-pag="%s"' % a['pag'] in h:
        print('  ya estaba, salto:', a['slug']); continue
    # Se insertan justo antes de la página de privacidad, que es la última
    # tanda que añadimos, para no romper el orden de los artículos existentes.
    ancla = '<main class="pagina" data-pag="privacidad">'
    assert h.count(ancla) == 1
    h = h.replace(ancla, seccion(a, E) + '\n' + ancla)
    puestos.append(a)

# tarjetas del listado del blog
i = h.find('data-pag="blog"'); fin = h.find('</main>', i)
listado = h[i:fin]
# El punto de inserción es el cierre de <div class="rejilla r3">, contando
# anidamiento. Buscar el último </a> del listado no sirve: el último enlace de
# la página es el botón de WhatsApp del pie, y las tarjetas caían fuera de la
# rejilla, a todo el ancho y con la foto enorme.
_gi = listado.find('<div class="rejilla r3">')
_prof = 0
ultima = None
for _m in re.finditer(r'<div\b|</div>', listado[_gi:]):
    _prof += 1 if _m.group(0) != '</div>' else -1
    if _prof == 0:
        ultima = _gi + _m.start()
        break
assert ultima, 'no encontre el cierre de la rejilla del listado'
tarjetas = ''
for a in ARTS2:
    if '/blog/%s"' % a['slug'] in listado: continue
    f = a['fig'][0]
    tarjetas += ('\n        <a class="nota rev" href="/blog/%s">\n'
                 '          <div class="nota-img"><img src="%s" alt="%s" loading="lazy" width="%d" height="%d"></div>\n'
                 '          <div class="nota-cuerpo doble-filete"><span class="nota-meta">%s · %s</span>'
                 '<h3>%s</h3><p>%s</p></div>\n'
                 '        </a>' % (a['slug'], f[0], f[3], f[1], f[2],
                                   a['cat'], FECHA_TXT, a['h1'], TEASER[a['slug']]))
if tarjetas:
    h = h[:i] + listado[:ultima] + tarjetas + listado[ultima:] + h[fin:]

open('index.html', 'w', encoding='utf-8').write(h)
print('  páginas en index.html:', h.count('class="pagina"'))
print('  tarjetas en el listado:', h[h.find('data-pag="blog"'):h.find('</main>', h.find('data-pag="blog"'))].count('<a class="nota rev"'))

# ------------------------------------------------------------------ middleware
m = open('functions/_middleware.js', encoding='utf-8').read()
ancla_r = "  '/privacidad': {"
nuevas = ''
for a in ARTS2:
    ruta = "  '/blog/%s': {" % a['slug']
    if ruta in m: continue
    nuevas += ("  '/blog/%s': {\n"
               "    pagina: '%s',\n"
               "    titulo: '%s',\n"
               "    desc: '%s',\n"
               "    imagen: '%s',\n"
               "    miga: '%s',\n"
               "    padre: 'blog',\n"
               "  },\n" % (a['slug'], a['pag'],
                           a['titulo'].replace("'", "\\'"),
                           a['desc'].replace("'", "\\'"),
                           a['img'].replace('/assets/', ''),
                           a['cat'].replace("'", "\\'")))
if nuevas:
    assert m.count(ancla_r) == 1
    m = m.replace(ancla_r, nuevas + ancla_r)
open('functions/_middleware.js', 'w', encoding='utf-8').write(m)
print('  rutas en el middleware:', m.count("    pagina: '"))

# ------------------------------------------------------------------ sitemap
s = open('sitemap.xml', encoding='utf-8').read()
add = ''
for a in ARTS2:
    loc = 'https://sastreriaandresvargas.pe/blog/%s' % a['slug']
    if loc + '<' in s: continue
    add += ('  <url>\n    <loc>%s</loc>\n    <lastmod>2026-08-31</lastmod>\n'
            '    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n' % loc)
if add:
    s = s.replace('</urlset>', add + '</urlset>')
open('sitemap.xml', 'w', encoding='utf-8').write(s)
print('  URLs en el sitemap:', s.count('<loc>'))
