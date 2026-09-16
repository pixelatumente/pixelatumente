#!/usr/bin/env python3
"""Extrae un post del WP y lo vuelca a stdout + archivo temporal para comparar."""
import json, re, sys, urllib.request

SLUG = sys.argv[1]
req = urllib.request.Request(
    f'https://pixelatumente.com/wp-json/wp/v2/posts?slug={SLUG}&_fields=id,slug,title,date,content',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0.0.0',
             'Accept': 'application/json'})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.loads(r.read().decode('utf-8'))
if not data:
    print('SIN RESULTADO'); sys.exit(1)
post = data[0]
title = re.sub(r'\s+', ' ', post['title']['rendered']).strip()
# Guardar el HTML crudo para inspección
with open(f'/tmp/{SLUG}.html', 'w', encoding='utf-8') as f:
    f.write(post['content']['rendered'])
print(f'TITLE: {title}')
print(f'DATE: {post["date"][:10]}')
print(f'HTML chars: {len(post["content"]["rendered"])}')
# Estadísticas de estructura
html = post['content']['rendered']
print(f'H2: {len(re.findall(r"<h2", html))} | H3: {len(re.findall(r"<h3", html))} | párrafos: {len(re.findall(r"<p", html))}')
# Primeros 600 chars en texto plano
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text)
print(f'INICIO: {text[:600]}')
