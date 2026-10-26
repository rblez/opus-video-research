"""Experimento 002: mockup 3D con Pillow puro.

Un teléfono con la tienda dentro, dibujado en 2D, inclinado con
transformación de perspectiva + sombra suave + flotación. 5 s, 30 fps,
540x960. Sin motor 3D, sin navegador, sin MCP: Pillow + numpy + ffmpeg.
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, DUR = 540, 960, 30, 5
BG = (244, 244, 246)
GREEN = (32, 196, 90)
WHITE = (255, 255, 255)
DARK = (17, 17, 17)
GRAY = (119, 119, 119)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

f_title = ImageFont.truetype(BOLD, 44)
f_sub = ImageFont.truetype(BOLD, 24)
f_shop = ImageFont.truetype(BOLD, 26)
f_price = ImageFont.truetype(BOLD, 22)


def find_coeffs(pa, pb):
    """Coeficientes para Image.transform(PERSPECTIVE): pa = esquinas
    destino en la imagen final, pb = esquinas origen en la imagen fuente."""
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])
    a = np.array(matrix, float)
    b = np.array(pb).reshape(8)
    return np.array(np.linalg.solve(a, b)).reshape(8)


def draw_phone():
    """La tienda dibujada en plano: 360x720."""
    pw, ph = 360, 720
    img = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, pw, ph], radius=36, fill=WHITE + (255,))
    d.rounded_rectangle([0, 0, pw, 104], radius=36, fill=GREEN + (255,))
    d.rectangle([0, 68, pw, 104], fill=GREEN + (255,))
    d.text((24, 34), "Mi Tienda", font=f_shop, fill=WHITE + (255,))
    y = 140
    for thumb, price in [((228, 245, 233), "350 CUP"),
                         ((237, 238, 240), "1 200 CUP"),
                         ((228, 245, 233), "700 CUP")]:
        d.rounded_rectangle([24, y, 96, y + 72], radius=16, fill=thumb + (255,))
        d.rounded_rectangle([112, y + 8, 200, y + 26], radius=9, fill=(230, 230, 232, 255))
        d.rounded_rectangle([112, y + 38, 170, y + 54], radius=8, fill=(240, 240, 242, 255))
        d.text((336, y + 22), price, font=f_price, fill=DARK + (255,), anchor="rm")
        y += 108
    return img


phone = draw_phone()
pw, ph = phone.size
src = [(0, 0), (pw, 0), (pw, ph), (0, ph)]

for i in range(FPS * DUR):
    t = i / (FPS * DUR)
    sway = 10 * math.sin(2 * math.pi * t)
    bob = 12 * math.sin(2 * math.pi * t)
    # Cuadrilátero destino: trapecio con perspectiva + balanceo + flotación
    quad = [
        (108 + sway, 190 + bob),
        (412 - sway, 168 + bob),
        (438 - sway, 830 + bob),
        (88 + sway, 852 + bob),
    ]
    canvas = Image.new("RGB", (W, H), BG)
    # Sombra: silueta del teléfono desplazada y difuminada
    shadow_src = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_src)
    sd.rounded_rectangle([0, 0, pw, ph], radius=36, fill=(0, 0, 0, 110))
    shadow_quad = [(x + 16, y + 24) for (x, y) in quad]
    shadow = shadow_src.transform((W, H), Image.PERSPECTIVE,
                                  find_coeffs(shadow_quad, src),
                                  resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(16))
    canvas.paste(shadow, (0, 0), shadow)
    # Teléfono en perspectiva
    tilted = phone.transform((W, H), Image.PERSPECTIVE,
                             find_coeffs(quad, src),
                             resample=Image.BICUBIC)
    canvas.paste(tilted, (0, 0), tilted)
    d = ImageDraw.Draw(canvas)
    d.text((W // 2, 56), "Mockup 3D", font=f_title, fill=DARK, anchor="mm")
    d.text((W // 2, 106), "solo Pillow + ffmpeg", font=f_sub, fill=GRAY, anchor="mm")
    canvas.convert("RGB").save(f"frames/f-{i:04d}.png")

print("frames:", FPS * DUR)
