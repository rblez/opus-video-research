# Bitácora de investigación

## 2026-10-26 — Arranque

- Pregunta de Ray: investigar qué hace Opus 5.5 para generar videos así
  sin MCP, solo con Python Pillow (referencia: brief del video de Duolingo).
- Contexto previo: la investigación del 2026-10-26 documentó la vía
  HTML/headless/ffmpeg; la vía Pillow es hipótesis sin verificar todavía.
- Experimento 001: Pillow puro (ver `experiments/001-pillow-basico/`).
- Resultado 001 (ejecutado y visto): 150 frames, 5 s, 30 fps, 540x960,
  MP4 22 KB, decodificación completa sin errores, 3 frames muestreados
  (0.5/2.5/4.5 s) limpios: círculo con ease-out, texto y barra de progreso
  avanzando. Prueba el mecanismo (Pillow dibuja, ffmpeg une), NO prueba
  que Opus lo use así.
- Corrección 2026-10-26 (PDF del brief de Duolingo leído completo): el
  brief asigna a Pillow/OpenCV solo herramientas auxiliares y prohíbe
  simular 3D cinematográfico con imágenes 2D; exige motor 3D real
  (Blender/Cycles). La hipótesis «solo Pillow» no describe ese brief.

## Verificado / sin verificar

- VERIFICADO (ejecutado): Pillow 10.2.0 disponible, ffmpeg disponible,
  experimento 001 codifica y decodifica sin errores (ver notas del experimento).
- SIN VERIFICAR: que Opus 5.5 use Pillow para sus videos; que la vía Pillow
  alcance calidad de motion graphics profesional (tipografía, easing,
  composición); costes, herramientas exactas y prompts que usa.
