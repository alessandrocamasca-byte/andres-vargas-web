/**
 * Cloudflare Pages despliega la raíz del repo, así que cualquier archivo que
 * viva aquí queda accesible por URL. Las reglas de `_redirects` NO sirven para
 * esto: los archivos estáticos tienen prioridad sobre ellas y se sirven igual.
 *
 * Este middleware sí se ejecuta antes que el archivo estático, así que hace
 * tres cosas:
 *
 *  1. Bloquea la documentación interna del proyecto.
 *  2. Da a cada sección su propia URL con su propio <title> y descripción,
 *     reescritos AQUÍ y no en el navegador. La web es de una sola página; sin
 *     esto Google solo puede posicionar una URL y el resto del contenido no
 *     compite por nada.
 *  3. Devuelve 404 de verdad en lo que no existe. Antes cualquier ruta
 *     inventada respondía 200 con la portada entera: contenido duplicado en
 *     infinitas direcciones, que es peor que no tener rutas.
 */

const BLOQUEADO = [
  /^\/(CLAUDE|NOTAS|DESIGN-SYSTEM|README)\.md$/i,
  /^\/pauta(\/|$)/i,
  /^\/\.git(\/|$)/i,
];

const SITIO = 'https://andres-vargas-web.pages.dev';

/* Cada ruta apunta a la página interna que abre el script y lleva el texto con
   el que se presenta en buscadores. Los títulos abren con el término que la
   gente escribe —en Perú «terno», no «traje»— y dejan la marca al final. */
const RUTAS = {
  '/': {
    pagina: 'inicio',
    titulo: 'Ternos y Trajes a Medida en Lima | Sastrería Andrés Vargas',
    desc: 'Sastrería en Lima desde 1982. Ternos, trajes y camisas a medida, traje de novio y vestuario corporativo. Tres tiendas. Escríbenos por WhatsApp.',
    imagen: 'hero.jpg',
  },
  '/a-medida': {
    pagina: 'medida',
    titulo: 'Sastrería a Medida en Lima | Andrés Vargas',
    desc: 'Cómo se construye una prenda a medida: patrón propio sobre tus medidas, pruebas y elección de tela con nuestros sastres. En Lima desde 1982.',
    imagen: 'traje-petroleo.jpg',
    miga: 'A medida',
  },
  '/ternos-a-medida': {
    pagina: 'trajes',
    titulo: 'Ternos y Trajes a Medida en Lima | Andrés Vargas',
    desc: 'Ternos de dos y tres piezas, esmóquines y chaqués a medida, confeccionados en nuestro taller de Lima sobre tus medidas y la tela que elijas.',
    imagen: 'editorial-duo.jpg',
    miga: 'Ternos y trajes',
  },
  '/camisas-a-medida': {
    pagina: 'camisas',
    titulo: 'Camisas a Medida en Lima | Andrés Vargas',
    desc: 'Camisas a medida con patrón propio: cuello, puño y silueta se definen contigo. Sastrería en Lima desde 1982, con tres tiendas.',
    imagen: 'traje-gris.jpg',
    miga: 'Camisas',
  },
  '/telas': {
    pagina: 'telas',
    titulo: 'Telas para Ternos y Camisas en Lima | Andrés Vargas',
    desc: 'Distribuidores oficiales de telas nacionales e importadas: tejeduría peruana y casas italianas e inglesas, con asesoría de sastres.',
    imagen: 'editorial-esmoquin-negro.jpg',
    miga: 'Telas',
  },
  '/trajes-de-novio': {
    pagina: 'novios',
    titulo: 'Trajes de Novio a Medida en Lima | Andrés Vargas',
    desc: 'El traje del novio y el de su cortejo, resueltos en un solo lugar: de la primera medida a los gemelos. Experiencia de novios en Chacarilla, Surco.',
    imagen: 'novios-trio-wide.jpg',
    miga: 'Trajes de novio',
  },
  '/corporativo': {
    pagina: 'corporativo',
    titulo: 'Ternos y Uniformes Corporativos a Medida | Andrés Vargas',
    desc: 'Vestuario a medida para equipos y directivos, con la misma confección de siempre coordinada para varias personas. Sastrería en Lima desde 1982.',
    imagen: 'editorial-esmoquin-marfil.jpg',
    miga: 'Corporativo',
  },
  '/tiendas': {
    pagina: 'tiendas',
    titulo: 'Tiendas de Sastrería en Lima | Andrés Vargas',
    desc: 'Tres tiendas en Lima: Jr. Ucayali 115, 119 y 121 y Jr. Huallaga 558 y 570 en el Cercado, y Av. Primavera 252, Chacarilla, en Surco.',
    imagen: 'hero.jpg',
    miga: 'Tiendas',
  },
  '/catalogo-de-telas': {
    pagina: 'catalogo',
    titulo: 'Catálogo de Telas para Ternos | Andrés Vargas',
    desc: 'Todo el muestrario Barrington, tela por tela. Filtra por colección, grado, tejido, composición y color, y escríbenos con el código.',
    imagen: 'editorial-esmoquin-negro.jpg',
    miga: 'Catálogo de telas',
  },
  '/blog': {
    pagina: 'blog',
    titulo: 'Blog de Sastrería | Andrés Vargas',
    desc: 'Cómo elegir, cómo cuidar y cuándo empezar. Lo que hemos aprendido en 44 años de oficio, contado sin tecnicismos.',
    imagen: 'editorial-duo.jpg',
    miga: 'Blog',
  },
};

/* Reescribe el <head> al vuelo. Hacerlo aquí y no en el navegador importa:
   así el título correcto ya viene en el HTML, sin depender de que el rastreador
   ejecute JavaScript. */
class Meta {
  constructor(ruta, url) { this.r = ruta; this.url = url; }
  element(el) {
    const t = el.tagName;
    if (t === 'title') { el.setInnerContent(this.r.titulo); return; }
    const name = el.getAttribute('name');
    const prop = el.getAttribute('property');
    const rel = el.getAttribute('rel');
    const img = SITIO + '/assets/' + this.r.imagen;
    if (name === 'description') el.setAttribute('content', this.r.desc);
    else if (prop === 'og:title') el.setAttribute('content', this.r.titulo);
    else if (prop === 'og:description') el.setAttribute('content', this.r.desc);
    else if (prop === 'og:url') el.setAttribute('content', this.url);
    else if (prop === 'og:image') el.setAttribute('content', img);
    else if (name === 'twitter:title') el.setAttribute('content', this.r.titulo);
    else if (name === 'twitter:description') el.setAttribute('content', this.r.desc);
    else if (name === 'twitter:image') el.setAttribute('content', img);
    else if (rel === 'canonical') el.setAttribute('href', this.url);
    // og:image:width/height se quedan como están: cada foto tiene su tamaño,
    // pero declararlo mal es peor que no declararlo, así que se eliminan
    // cuando la imagen no es la de portada.
    else if ((prop === 'og:image:width' || prop === 'og:image:height') && this.r.imagen !== 'hero.jpg') el.remove();
  }
}

/* Miga de pan: es lo que Google usa para mostrar «andres-vargas › Telas» en
   lugar de la URL cruda en el resultado de búsqueda. */
class Miga {
  constructor(ruta, url) { this.r = ruta; this.url = url; }
  element(el) {
    if (!this.r.miga) return;
    const datos = {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Inicio', item: SITIO + '/' },
        { '@type': 'ListItem', position: 2, name: this.r.miga, item: this.url },
      ],
    };
    el.append('<script type="application/ld+json">' + JSON.stringify(datos) + '</script>', { html: true });
  }
}

/* Deja únicamente la sección que pide la URL.
   Sin esto, las nueve direcciones servían el mismo HTML de 142 KB con las
   nueve secciones dentro y solo cambiaba un atributo: para un buscador eran
   nueve páginas casi idénticas, y para los rastreadores de IA —que en su
   mayoría no ejecutan JavaScript— preguntar por «trajes de novio» devolvía
   una página que hablaba sobre todo de otra cosa.

   También pone `activa` en la que sobrevive: `.pagina` es `display:none` por
   defecto, así que sin esta clase el contenido llegaría oculto, que es
   justo lo que los buscadores descuentan. */
class Podar {
  constructor(pagina) { this.pagina = pagina; }
  element(el) {
    if (el.getAttribute('data-pag') !== this.pagina) { el.remove(); return; }
    const clases = el.getAttribute('class') || '';
    if (!/\bactiva\b/.test(clases)) el.setAttribute('class', (clases + ' activa').trim());
  }
}

/* Marca en el <body> qué sección abrir, para que el script no tenga que
   deducirla de la URL por su cuenta. El tema de Corporativo se pone aquí
   también: si esperara al script, la página entraría azul y viraría a ciruela
   a la vista del visitante. */
class Cuerpo {
  constructor(pagina) { this.pagina = pagina; }
  element(el) {
    el.setAttribute('data-ruta', this.pagina);
    if (this.pagina === 'corporativo') el.setAttribute('class', 'tema-corporativo');
  }
}

/* El menú trae «Inicio» marcado como activo en el HTML. Sin esto, en /telas se
   vería Inicio subrayado hasta que arrancara el script. */
class MenuSub {
  constructor(pagina) { this.pagina = pagina; }
  element(el) {
    const clases = (el.getAttribute('class') || '').replace(/\bon\b/g, '').trim();
    const nuevo = el.getAttribute('data-ir') === this.pagina ? (clases + ' on').trim() : clases;
    if (nuevo) el.setAttribute('class', nuevo); else el.removeAttribute('class');
  }
}

class Menu {
  constructor(pagina) {
    this.pagina = pagina;
    this.activo = { trajes: 'medida', camisas: 'medida', catalogo: 'telas' }[pagina] || pagina;
  }
  element(el) {
    const clases = (el.getAttribute('class') || '').replace(/\bon\b/g, '').trim();
    // El submenú se marca por coincidencia exacta, no por sección padre.
    const enSub = /submenu/.test(el.getAttribute('data-nivel') || '');
    const objetivo = enSub ? this.pagina : this.activo;
    const nuevo = el.getAttribute('data-ir') === objetivo ? (clases + ' on').trim() : clases;
    if (nuevo) el.setAttribute('class', nuevo); else el.removeAttribute('class');
  }
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  let ruta = url.pathname;

  if (BLOQUEADO.some((re) => re.test(ruta))) {
    return new Response('Not Found', {
      status: 404,
      headers: { 'content-type': 'text/plain; charset=utf-8' },
    });
  }

  // Sin barra final, salvo la raíz: /telas/ y /telas no pueden ser dos URLs.
  if (ruta.length > 1 && ruta.endsWith('/')) {
    return Response.redirect(SITIO + ruta.slice(0, -1) + url.search, 301);
  }
  // /index.html sería una segunda dirección para la portada.
  if (ruta === '/index.html') return Response.redirect(SITIO + '/' + url.search, 301);

  const conf = RUTAS[ruta];
  if (conf) {
    const res = await context.env.ASSETS.fetch(new URL('/index.html', url));
    const html = new Response(res.body, res);
    html.headers.set('content-type', 'text/html; charset=utf-8');
    return new HTMLRewriter()
      .on('title, meta, link[rel="canonical"]', new Meta(conf, SITIO + (ruta === '/' ? '/' : ruta)))
      .on('head', new Miga(conf, SITIO + (ruta === '/' ? '/' : ruta)))
      .on('.menu > li > a[data-ir]', new Menu(conf.pagina))
      .on('.submenu a[data-ir]', new MenuSub(conf.pagina))
      .on('body', new Cuerpo(conf.pagina))
      .on('main[data-pag]', new Podar(conf.pagina))
      .transform(html);
  }

  /* Archivos reales (assets, robots.txt, sitemap.xml, favicon…).
     Cloudflare Pages responde a un archivo que no existe con la portada entera
     y un 200: pedir /assets/loquesea.png devolvía HTML haciéndose pasar por
     imagen. Eso engaña a los rastreadores y rompe cualquier comprobación de
     «¿existe este archivo?». Si lo que vuelve no es del tipo que se pidió, es
     que no está: 404. */
  const ext = (ruta.match(/\.([a-z0-9]+)$/i) || [])[1];
  if (ext) {
    const res = await context.next();
    const tipo = res.headers.get('content-type') || '';
    const esHtml = /text\/html/i.test(tipo);
    if (esHtml && !/^html?$/i.test(ext)) {
      return new Response('Not Found', {
        status: 404,
        headers: { 'content-type': 'text/plain; charset=utf-8' },
      });
    }
    return res;
  }

  // Cualquier otra cosa no existe. Antes devolvía la portada con 200.
  return new Response('Not Found', {
    status: 404,
    headers: { 'content-type': 'text/plain; charset=utf-8' },
  });
}
