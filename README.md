# opus-video-research

Repo de investigación (nombre de trabajo, sin publicar todavía).
Pregunta central: **¿qué hace Claude Code Opus 5.5 para generar videos así, sin necesidad de un MCP, solo con Python Pillow?**

## Hipótesis a verificar (de Ray, 2026-10-26 — NO es un hecho)

Desde un brief detallado (como el brief del video de Duolingo que Ray compartió),
Opus escribe un script Python que dibuja cada frame con Pillow y lo une con
ffmpeg. Sin MCP, sin navegador, sin motor de animación web.

**Corrección 2026-10-26 (leído el PDF del brief):** el brief de Duolingo NO
dice «solo Pillow». Asigna a Pillow y OpenCV solo herramientas auxiliares
(procesamiento de imágenes, composición, texturas, control de fotogramas) y
prohíbe simular un render 3D cinematográfico únicamente con imágenes 2D.
Para calidad cinematográfica exige un motor 3D programable real
(Blender/Cycles automatizado con Python o equivalente). La hipótesis
«solo Pillow» queda, por tanto, como pregunta abierta, no como descripción
del brief.

## Hipótesis rival (de la investigación del 2026-10-26)

El modelo escribe HTML/CSS/JS donde cada estado es función del tiempo; un
navegador headless captura frame a frame (seek) y FFmpeg une los frames en MP4.
Herramientas: GSAP, Remotion, HyperFrames. Ver el informe completo en la página
«Cómo hacen videos los diseñadores» (artefacto) y en
`research_notes/como-disenadores-hacen-videos-motion-gra-20261026-0329/`.

## Método

1. Reproducir el mínimo de cada vía con el mismo brief corto.
2. Comparar: calidad visual, control tipográfico, esfuerzo, errores típicos.
3. Registrar en `INVESTIGACION.md` qué se verificó ejecutándolo y qué sigue
   siendo afirmación sin probar. Nada se da por cierto sin correrlo.

## Alcance (corrección de Ray, 2026-10-26)

El «3D» que investiga este repo es **3D tipo mockup**: dispositivos,
tarjetas de interfaz con profundidad, sombras y perspectiva (un teléfono
flotando en ángulo con la tienda dentro, tarjetas con espesor). NO es
animación cinematográfica de personajes (el mundo 3D del brief de Duolingo
con Duo). El brief de Duolingo sirve aquí solo como ejemplo de brief
detallado, no como estilo visual objetivo. Esto importa porque el mockup
3D sí es alcanzable dibujando en 2D con perspectiva y sombras, sin motor
3D real — y por eso la hipótesis «solo Pillow» se vuelve plausible en
este alcance.

## Regla dura

**Ningún video sale sin verlo antes.** Ver = decodificación completa sin
errores + muestreo de frames a lo largo de todo el video. Revisar frames
sueltos antes de codificar NO cuenta: el MP4 entregado es lo que se verifica.

## Experimentos

- `experiments/001-pillow-basico/` — Pillow puro, 5 s, 30 fps, vertical.
  Dibuja fondo, círculo con ease-out y texto. Codifica con ffmpeg.

## Contribuir

Ver `CONTRIBUIR.md`. En corto: elige un issue abierto, crea un experimento
numerado (`experiments/NNN-nombre/` con script, notas y video verificado),
y abre un PR a `main`. Todo en español. Nada se da por verificado sin
ejecutarlo, y ningún video se da por bueno sin verlo antes.
