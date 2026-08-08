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
  },
  '/a-medida': {
    pagina: 'medida',
    titulo: 'Sastrería a Medida en Lima | Andrés Vargas',
    desc: 'Cómo se construye una prenda a medida: patrón propio sobre tus medidas, pruebas y elección de tela con nuestros sastres. En Lima desde 1982.',
  },
  '/ternos-a-medida': {
    pagina: 'trajes',
    titulo: 'Ternos y Trajes a Medida en Lima | Andrés Vargas',
    desc: 'Ternos de dos y tres piezas, esmóquines y chaqués a medida, confeccionados en nuestro taller de Lima sobre tus medidas y la tela que elijas.',
  },
  '/camisas-a-medida': {
    pagina: 'camisas',
    titulo: 'Camisas a Medida en Lima | Andrés Vargas',
    desc: 'Camisas a medida con patrón propio: cuello, puño y silueta se definen contigo. Sastrería en Lima desde 1982, con tres tiendas.',
  },
  '/telas': {
    pagina: 'telas',
    titulo: 'Telas para Ternos y Camisas en Lima | Andrés Vargas',
    desc: 'Distribuidores oficiales de telas nacionales e importadas: tejeduría peruana y casas italianas e inglesas, con asesoría de sastres.',
  },
  '/trajes-de-novio': {
    pagina: 'novios',
    titulo: 'Trajes de Novio a Medida en Lima | Andrés Vargas',
    desc: 'El traje del novio y el de su cortejo, resueltos en un solo lugar: de la primera medida a los gemelos. Experiencia de novios en Chacarilla, Surco.',
  },
  '/corporativo': {
    pagina: 'corporativo',
    titulo: 'Ternos y Uniformes Corporativos a Medida | Andrés Vargas',
    desc: 'Vestuario a medida para equipos y directivos, con la misma confección de siempre coordinada para varias personas. Sastrería en Lima desde 1982.',
  },
  '/tiendas': {
    pagina: 'tiendas',
    titulo: 'Tiendas de Sastrería en Lima | Andrés Vargas',
    desc: 'Tres tiendas en Lima: Jr. Ucayali 115, 119 y 121 y Jr. Huallaga 558 y 570 en el Cercado, y Av. Primavera 252, Chacarilla, en Surco.',
  },
  '/blog': {
    pagina: 'blog',
    titulo: 'Blog de Sastrería | Andrés Vargas',
    desc: 'Cómo elegir, cómo cuidar y cuándo empezar. Lo que hemos aprendido en 44 años de oficio, contado sin tecnicismos.',
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
    if (name === 'description') el.setAttribute('content', this.r.desc);
    else if (prop === 'og:title') el.setAttribute('content', this.r.titulo);
    else if (prop === 'og:description') el.setAttribute('content', this.r.desc);
    else if (prop === 'og:url') el.setAttribute('content', this.url);
    else if (rel === 'canonical') el.setAttribute('href', this.url);
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
      .on('body', new Cuerpo(conf.pagina))
      .transform(html);
  }

  // Archivos reales (assets, robots.txt, sitemap.xml, favicon…) siguen su curso.
  const esArchivo = /\.[a-z0-9]+$/i.test(ruta);
  if (esArchivo) return context.next();

  // Cualquier otra cosa no existe. Antes devolvía la portada con 200.
  return new Response('Not Found', {
    status: 404,
    headers: { 'content-type': 'text/plain; charset=utf-8' },
  });
}
