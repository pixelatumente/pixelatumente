#!/usr/bin/env python3
"""Quita el fondo blanco exterior de un logo de disco (flood-fill desde esquinas)
preservando blancos internos. Genera versión transparente."""
import numpy as np
from PIL import Image
from scipy import ndimage

SRC = '/home/hermes/.hermes/images/upload_20260906_153007_2.png'
OUT_DIR = '/home/hermes/projects/pixelatumente-2/public'

def main():
    img = Image.open(SRC).convert('RGB')
    arr = np.array(img)
    H, W, _ = arr.shape
    print(f'Original: {W}x{H}')

    # Máscara de "blanco/near-blanco" (umbral alto) — el fondo exterior
    near_white = (arr[:, :, 0] > 235) & (arr[:, :, 1] > 235) & (arr[:, :, 2] > 235)

    # Solo el blanco CONECTADO al borde (4 esquinas) = fondo
    # Etiquetar la componente de blanco que toca esquinas
    lbl, n = ndimage.label(near_white)
    border_labels = set()
    for x in range(W):
        for y in (0, H - 1):
            if near_white[y, x]:
                border_labels.add(lbl[y, x])
    for y in range(H):
        for x in (0, W - 1):
            if near_white[y, x]:
                border_labels.add(lbl[y, x])

    background = np.isin(lbl, list(border_labels)) & (lbl > 0)
    print(f'Píxeles de fondo a quitar: {background.sum()}')

    # Crear RGBA
    rgba = np.dstack([arr, np.full((H, W), 255, dtype=np.uint8)])
    rgba[background, 3] = 0

    out = Image.fromarray(rgba, 'RGBA')

    # Recortar al contenido (bounding box de píxeles no transparentes)
    bbox = out.getbbox()
    if bbox:
        out = out.crop(bbox)
        print(f'Recortado a: {out.size}')

    # Guardar en varias tallas (cuadrado, escalado a bordes)
    sizes = {'logo': 512, 'logo-256': 256, 'favicon': 64}
    for name, size in sizes.items():
        sq = out.copy()
        # asegurar cuadrado centrado
        w, h = sq.size
        side = max(w, h)
        canvas = Image.new('RGBA', (side, side), (0, 0, 0, 0))
        canvas.paste(sq, ((side - w) // 2, (side - h) // 2))
        canvas.thumbnail((size, size), Image.LANCZOS)
        out_path = f'{OUT_DIR}/{name}.png'
        canvas.save(out_path)
        print(f'saved {out_path} ({canvas.size})')

    # ICO multi-tamaño
    fav = Image.open(f'{OUT_DIR}/favicon.png').convert('RGBA')
    fav.save(f'{OUT_DIR}/favicon.ico', format='ICO',
             sizes=[(16, 16), (32, 32), (48, 48)])
    print('saved favicon.ico')

if __name__ == '__main__':
    main()
