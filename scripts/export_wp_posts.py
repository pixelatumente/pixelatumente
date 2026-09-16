#!/usr/bin/env python3
"""Extrae posts reales de pixelatumente.com (WP REST API) y los guarda como Markdown
para el blog Astro (src/content/blog/<slug>.md). HTML → Markdown básico."""
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

SLUGS = [
    'dominios-gratis',
    'herramientas-para-arreglar-enlaces-rotos',
    'broken-link-checker-arregla-enlaces-rotos',
    'local-llm',
    'marketing-para-emprendedores',
    'eliminar-resenas-google',
]

OUT_DIR = '/home/hermes/projects/pixelatumente-2/src/content/blog'
BASE = 'https://pixelatumente.com/wp-json/wp/v2/posts?slug='


def fetch(slug):
    url = BASE + slug + '&_fields=id,slug,title,date,content'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': 'application/json',
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.loads(r.read().decode('utf-8'))
    if not data:
        print(f'!! {slug}: sin resultado')
        return None
    return data[0]


class MdParser(HTMLParser):
    """Convierte HTML de WP a Markdown razonable. Gestiona p, h2-h4, ul/ol/li,
    strong, em, a, blockquote, table básico, hr."""
    def __init__(self):
        super().__init__()
        self.out = []
        self.list_stack = []      # 'ul' | 'ol'
        self.in_table = False
        self.table_rows = []
        self.row_cells = []
        self.in_cell = False
        self.cell_buf = []
        self.cell_is_head = False
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('p', 'div'):
            self._flush_cell()
            self.out.append('\n\n')
        elif tag in ('h2', 'h3', 'h4'):
            self.out.append('\n\n' + '#' * int(tag[1]) + ' ')
        elif tag == 'ul':
            self.list_stack.append('ul')
            self.out.append('\n\n')
        elif tag == 'ol':
            self.list_stack.append('ol')
            self.out.append('\n\n')
        elif tag == 'li':
            marker = '-' if (self.list_stack and self.list_stack[-1] == 'ul') else '1.'
            self.out.append('\n' + marker + ' ')
        elif tag == 'strong' or tag == 'b':
            self.out.append('**')
        elif tag == 'em' or tag == 'i':
            self.out.append('*')
        elif tag == 'a':
            href = a.get('href', '')
            self.out.append('[')
            self._link_href = href
        elif tag == 'br':
            self.out.append('\n')
        elif tag == 'blockquote':
            self.out.append('\n\n> ')
        elif tag == 'hr':
            self.out.append('\n\n---\n\n')
        elif tag == 'table':
            self.in_table = True
            self.table_rows = []
        elif tag == 'thead':
            pass
        elif tag == 'tbody':
            pass
        elif tag == 'tr':
            self.row_cells = []
        elif tag in ('td', 'th'):
            self.in_cell = True
            self.cell_is_head = (tag == 'th')
            self.cell_buf = []
        elif tag == 'img':
            src = a.get('src', '')
            alt = a.get('alt', '')
            if src and not src.startswith('data:'):
                self.out.append(f'\n\n![{alt}]({src})\n\n')
        elif tag == 'figure':
            self.out.append('\n\n')
        elif tag == 'figcaption':
            self.out.append('\n*')
        elif tag == 'span' or tag == 'code':
            pass
        elif tag == 'pre':
            self.out.append('\n\n```\n')
        elif tag == 'iframe':
            self.out.append(f'\n\n[Contenido embebido: {a.get("src", "")}]({a.get("src", "")})\n\n')

    def handle_endtag(self, tag):
        if tag in ('p', 'div'):
            self.out.append('\n\n')
        elif tag in ('h2', 'h3', 'h4'):
            self.out.append('\n\n')
        elif tag == 'ul' or tag == 'ol':
            if self.list_stack:
                self.list_stack.pop()
            self.out.append('\n\n')
        elif tag == 'li':
            self.out.append('')
        elif tag == 'strong' or tag == 'b':
            self.out.append('**')
        elif tag == 'em' or tag == 'i':
            self.out.append('*')
        elif tag == 'a':
            href = getattr(self, '_link_href', '')
            self.out.append(f']({href})')
            self._link_href = ''
        elif tag == 'blockquote':
            self.out.append('\n\n')
        elif tag == 'figcaption':
            self.out.append('*\n\n')
        elif tag == 'pre':
            self.out.append('\n```\n\n')
        elif tag == 'table':
            self._flush_cell()
            self.in_table = False
            # render tabla
            if self.table_rows:
                self.out.append('\n\n')
                for ri, row in enumerate(self.table_rows):
                    self.out.append('| ' + ' | '.join(row) + ' |\n')
                    if ri == 0:
                        self.out.append('|' + '|'.join(['---'] * len(row)) + '|\n')
                self.out.append('\n\n')
        elif tag == 'tr':
            self._flush_cell()
            if self.row_cells:
                self.table_rows.append(self.row_cells)
        elif tag in ('td', 'th'):
            self.in_cell = False

    def handle_data(self, data):
        if self.in_cell:
            self.cell_buf.append(data)
        else:
            self.out.append(data)

    def _flush_cell(self):
        if self.in_cell:
            txt = ''.join(self.cell_buf).strip()
            self.row_cells.append(txt)
            self.cell_buf = []
            self.in_cell = False


def clean_text(s):
    """Limpia saltos excesivos y espacios raros."""
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = s.strip()
    return s


def html_to_md(html):
    p = MdParser()
    p.feed(html)
    p.close()
    md = ''.join(p.out)
    return clean_text(md)


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else SLUGS
    for slug in only:
        post = fetch(slug)
        if not post:
            continue
        title = re.sub(r'\s+', ' ', post['title']['rendered']).strip()
        date = post['date'][:10]
        body_html = post['content']['rendered']
        md = html_to_md(body_html)
        # Primera frase como description (hasta ~160 chars)
        desc_match = re.search(r'^([^#\n*]{40,200})', md, re.M)
        description = (desc_match.group(1).strip() if desc_match else title)[:200]
        description = re.sub(r'\s+', ' ', description).strip()
        frontmatter = f'---\ntitle: "{title.replace(chr(34), chr(39))}"\ndescription: "{description.replace(chr(34), chr(39))}"\ndate: "{date}"\n---\n\n'
        path = f'{OUT_DIR}/{slug}.md'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + md + '\n')
        print(f'OK {slug}: {title[:60]} | {len(md)} chars -> {path}')


if __name__ == '__main__':
    main()
