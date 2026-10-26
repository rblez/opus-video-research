"""Experimento 001: video mínimo dibujado solo con Pillow.

5 s, 30 fps, 540x960. Fondo verde, círculo blanco que entra con ease-out
y texto. Sin navegador, sin GSAP, sin MCP: Pillow + ffmpeg.
"""
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DUR = 540, 960, 30, 5
GREEN = (32, 196, 90)
WHITE = (255, 255, 255)
DARK = (17, 17, 17)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

font_big = ImageFont.truetype(BOLD, 64)
font_small = ImageFont.truetype(BOLD, 28)


def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


for i in range(FPS * DUR):
    t = i / (FPS * DUR)
    img = Image.new("RGB", (W, H), GREEN)
    d = ImageDraw.Draw(img)
    # Círculo que entra con ease-out (0.0 - 0.6 s del video)
    p = ease_out_cubic(min(1.0, t / 0.12))
    r = int(30 + 90 * p)
    d.ellipse([W // 2 - r, 300 - r, W // 2 + r, 300 + r], fill=WHITE)
    d.text((W // 2, 480), "Tiendly", font=font_big, fill=WHITE, anchor="mm")
    d.text((W // 2, 560), "solo Pillow + ffmpeg", font=font_small, fill=WHITE, anchor="mm")
    # Barra de progreso
    d.rectangle([60, 900, 60 + int((W - 120) * t), 912], fill=WHITE)
    img.save(f"frames/f-{i:04d}.png")

print("frames:", FPS * DUR)
