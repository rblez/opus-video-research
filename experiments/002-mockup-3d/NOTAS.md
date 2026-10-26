# Experimento 002 — Mockup 3D

## Qué hace

Un teléfono con la tienda dentro, dibujado en 2D con Pillow, inclinado
con transformación de perspectiva + sombra suave difuminada + flotación
(balanceo y subida/bajada). 5 s, 30 fps, 540x960. Esto es el «3D tipo
mockup»: dispositivos y tarjetas con profundidad, no animación
cinematográfica de personajes.

## Cómo correrlo

```bash
python3 gen.py
ffmpeg -y -framerate 30 -i frames/f-%04d.png -c:v libx264 -pix_fmt yuv420p -crf 23 mockup-3d.mp4
```

## Verificado (2026-10-26)

- 150 frames generados, MP4 de 5,0 s, decodificación completa sin errores.
- 3 frames muestreados del MP4 final (0.5 / 2.5 / 4.5 s) vistos: perspectiva,
  sombra y flotación correctos en los tres.
- Defecto encontrado al verlo: los precios se cortaban en el borde derecho
  del teléfono («350 CU…»). Causa: texto anclado a la izquierda desde x=268
  con ancho mayor que la tarjeta. Corrección: precios alineados a la derecha
  (x=336) y barras de texto más estrechas. Re-render verificado: precios
  completos («350 CUP», «1 200 CUP», «700 CUP»).

## Límites

Un solo mockup, sin múltiples escenas, sin audio, tipografía DejaVu (no de
marca). La perspectiva es un trapecio animado, no un modelo 3D real.
