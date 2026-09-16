#!/usr/bin/env python3
"""Genera favicon + og-image para pixelatumente (dibujo PIL, sin cairosvg)."""
from PIL import Image, ImageDraw, ImageFont

ARENA = (243, 240, 232)
ARENA_OSC = (232, 228, 216)
INK = (17, 17, 17)
ACCENT = (255, 90, 54)   # #FF5A36 terracota del .es actual
ACCENT_ALT = (1, 105, 111)  # #01696F verde-azulado


def draw_mark(d, s, ox=0, oy=0):
    """Pixel ('P') geométrico: cuadrado con la P partida — logo minimalista."""
    # cuadrado exterior (borde 2px estilo brutalista)
    d.rectangle([ox + 6 * s, oy + 6 * s, ox + 58 * s, oy + 58 * s], outline=INK, width=max(2, int(3 * s)))
    # bloque P (asta)
    d.rectangle([ox + 14 * s, oy + 16 * s, ox + 20 * s, oy + 48 * s], fill=ACCENT)
    # cabeza P (bucle)
    d.rectangle([ox + 20 * s, oy + 16 * s, ox + 40 * s, oy + 28 * s], fill=ACCENT)
    d.rectangle([ox + 36 * s, oy + 16 * s, ox + 40 * s, oy + 28 * s], fill=ARENA)
    d.rectangle([ox + 20 * s, oy + 24 * s, ox + 40 * s, oy + 28 * s], fill=ACCENT)
    # punto final naranja (abajo derecha)
    d.rectangle([ox + 44 * s, oy + 40 * s, ox + 50 * s, oy + 46 * s], fill=ACCENT_ALT)


def make_favicon(size):
    img = Image.new('RGB', (size, size), ARENA)
    d = ImageDraw.Draw(img)
    s = size / 64.0
    draw_mark(d, s)
    return img


def make_og():
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), ARENA)
    d = ImageDraw.Draw(img)
    # borde interior estilo brutalista
    d.rectangle([24, 24, W - 24, H - 24], outline=INK, width=6)
    # marca grande a la izquierda
    s = 8.0
    draw_mark(d, s, ox=70, oy=180)
    # texto
    try:
        font_t = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 84)
        font_s = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 40)
    except Exception:
        font_t = ImageFont.load_default()
        font_s = ImageFont.load_default()
    d.text((360, 200), 'Pixelatumente', fill=INK, font=font_t)
    d.text((360, 320), 'Aprendo, pruebo y publico.', fill=ACCENT, font=font_s)
    # banda inferior
    d.rectangle([0, H - 24, W, H], fill=ACCENT)
    return img


def main():
    base = '/home/hermes/projects/pixelatumente-2/public'
    make_favicon(32).save(f'{base}/favicon.png')
    make_favicon(180).save(f'{base}/apple-touch-icon.png')
    img32 = make_favicon(32)
    img32.save(f'{base}/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    make_og().save(f'{base}/og-default.png')
    print('OK: favicon.png / apple-touch-icon.png / favicon.ico / og-default.png')


if __name__ == '__main__':
    main()
