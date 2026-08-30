# -*- coding: utf-8 -*-
"""Enlaces externos de los artículos. Todos comprobados: responden 200 y el
título de la página confirma que son quien dicen ser.

Regla: se enlaza a casas de tela, a organismos del sector y a fuentes
oficiales. Nunca a otra sastrería, que sería mandarle el cliente al vecino.
"""
E = {
 'barrington':   ('https://barrington.com.pe/', 'Barrington'),
 'vbc':          ('https://www.vitalebarberiscanonico.com/', 'Vitale Barberis Canonico'),
 'albini':       ('https://www.albinigroup.com/', 'Albini'),
 'thomasmason':  ('https://www.thomasmason.com/', 'Thomas Mason'),
 'creditex':     ('https://www.creditex.com.pe/', 'Creditex'),
 'woolmark':     ('https://www.woolmark.com/', 'The Woolmark Company'),
 'woolmarkcare': ('https://www.woolmark.com/care/', 'The Woolmark Company'),
 'iwto':         ('https://iwto.org/', 'IWTO'),
 'harris':       ('https://www.harristweed.org/', 'Harris Tweed Authority'),
 'senamhi':      ('https://www.senamhi.gob.pe/', 'SENAMHI'),
}

def a(clave, texto=None):
    url, nombre = E[clave]
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, texto or nombre)
