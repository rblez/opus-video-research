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
- Corrección de alcance (Ray, 2026-10-26): el 3D objetivo es tipo
  mockup (dispositivos, tarjetas UI con profundidad, sombras y
  perspectiva), NO animación cinematográfica de personajes. El brief de
  Duolingo queda como ejemplo de brief detallado, no como estilo visual
  objetivo.
- Experimento 002 (2026-10-26, mockup 3D): teléfono con la tienda en
  perspectiva + sombra + flotación, solo Pillow. 150 frames, 5 s, decode
  OK, visto en 3 puntos. Defecto encontrado al verlo (precios cortados
  en el borde) y corregido (alineación derecha). El mockup 3D sí sale
  con Pillow; queda medirlo contra la vía HTML en el issue 2.
- Reenfoque (Ray, 2026-10-26): el repo se centra en cómo hacen las
  empresas grandes estos videos (pipeline, herramientas, decisiones).
  Lo de Opus/Pillow pasa a línea experimental, no es la pregunta.
  Enfoque: entender el sistema, no copiar el truco.

## Verificado / sin verificar

- VERIFICADO (ejecutado): Pillow 10.2.0 disponible, ffmpeg disponible,
  experimento 001 codifica y decodifica sin errores (ver notas del experimento).
- SIN VERIFICAR: que Opus 5.5 use Pillow para sus videos; que la vía Pillow
  alcance calidad de motion graphics profesional (tipografía, easing,
  composición); costes, herramientas exactas y prompts que usa.
