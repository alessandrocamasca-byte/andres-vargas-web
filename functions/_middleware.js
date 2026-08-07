/**
 * Cloudflare Pages despliega la raíz del repo, así que cualquier archivo que
 * viva aquí queda accesible por URL. Las reglas de `_redirects` NO sirven para
 * esto: los archivos estáticos tienen prioridad sobre ellas y se sirven igual.
 *
 * Este middleware sí se ejecuta antes que el archivo estático, así que es el
 * lugar correcto para bloquear la documentación interna del proyecto.
 */
const BLOQUEADO = [
  /^\/(CLAUDE|NOTAS|DESIGN-SYSTEM|README)\.md$/i,
  /^\/pauta(\/|$)/i,
  /^\/\.git(\/|$)/i,
];

export async function onRequest(context) {
  const ruta = new URL(context.request.url).pathname;
  if (BLOQUEADO.some((re) => re.test(ruta))) {
    return new Response('Not Found', {
      status: 404,
      headers: { 'content-type': 'text/plain; charset=utf-8' },
    });
  }
  return context.next();
}
