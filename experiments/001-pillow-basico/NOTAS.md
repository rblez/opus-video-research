# Experimento 001 — Pillow básico

## Qué hace

Dibuja un video mínimo solo con Pillow: fondo verde, círculo blanco que
entra con ease-out cúbico, texto y barra de progreso. 5 s, 30 fps, 540x960.

## Cómo correrlo

```bash
python3 gen.py
ffmpeg -y -framerate 30 -i frames/f-%04d.png -c:v libx264 -pix_fmt yuv420p -crf 23 pillow-001.mp4
```

## Verificado (2026-10-26)

- 150 frames generados, MP4 de 5,0 s y 22 KB.
- Decodificación completa sin errores (`ffmpeg -i pillow-001.mp4 -f null -`).
- 3 frames muestreados del MP4 final (0.5 / 2.5 / 4.5 s) vistos y limpios:
  círculo completo, texto legible, barra avanzando (10 % → 50 % → 90 %).

## Límites

No prueba que Opus 5.5 use Pillow. No tiene tipografía de marca real,
ni múltiples escenas, ni audio. Es la prueba mínima del mecanismo.
