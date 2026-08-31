/**
 * Puente entre el formulario corporativo y GoHighLevel.
 *
 * El navegador manda aquí, no a GHL: la URL del webhook vive como secreto del
 * proyecto y no aparece en el HTML. Un webhook expuesto en el código es un
 * buzón abierto —cualquiera puede meter contactos falsos en el CRM— y con un
 * bot son cientos en una noche.
 *
 * No se guarda nada: esta función recibe y reenvía. Los datos viven en GHL.
 *
 * Para activarlo:
 *   npx wrangler pages secret put GHL_WEBHOOK
 * Mientras el secreto no exista, responde 503 y el formulario cae solo a
 * WhatsApp, que es lo que hacía antes. Nunca se queda sin salida.
 */

const CAMPOS = ['nombre', 'telefono', 'correo', 'empresa', 'puesto', 'detalle'];
const LIMITES = { nombre: 120, telefono: 40, correo: 160, empresa: 160, puesto: 120, detalle: 3000 };

const json = (obj, status = 200) =>
  new Response(JSON.stringify(obj), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });

export async function onRequestPost(context) {
  const { request, env } = context;

  if (!env.GHL_WEBHOOK) return json({ ok: false, motivo: 'sin-destino' }, 503);

  let d;
  try {
    d = await request.json();
  } catch {
    return json({ ok: false, motivo: 'json-invalido' }, 400);
  }

  // Trampa para bots: el campo va oculto por CSS, una persona nunca lo llena.
  // Se responde 200 a propósito: si el bot ve un error, reintenta.
  if (d.web) return json({ ok: true });

  const limpio = {};
  for (const c of CAMPOS) {
    const v = String(d[c] ?? '').trim().slice(0, LIMITES[c]);
    if (!v && c !== 'detalle') return json({ ok: false, motivo: 'falta-' + c }, 400);
    limpio[c] = v;
  }
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(limpio.correo)) {
    return json({ ok: false, motivo: 'correo-invalido' }, 400);
  }

  const cuerpo = {
    ...limpio,
    origen: 'Formulario corporativo · sastreriaandresvargas.pe',
    pagina: request.headers.get('referer') || '',
    recibido: new Date().toISOString(),
  };

  try {
    const r = await fetch(env.GHL_WEBHOOK, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(cuerpo),
    });
    // GHL responde 200 al aceptar. Cualquier otra cosa es un fallo suyo y el
    // formulario tiene que enterarse para ofrecer WhatsApp.
    if (!r.ok) return json({ ok: false, motivo: 'ghl-' + r.status }, 502);
    return json({ ok: true });
  } catch {
    return json({ ok: false, motivo: 'sin-conexion' }, 502);
  }
}

// Cualquier método que no sea POST no tiene nada que hacer aquí.
export const onRequest = (context) =>
  context.request.method === 'POST'
    ? onRequestPost(context)
    : new Response('Method Not Allowed', { status: 405, headers: { allow: 'POST' } });
