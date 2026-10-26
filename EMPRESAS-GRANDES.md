# Cómo hacen las empresas grandes sus videos de producto (mockups 3D)

Síntesis de la investigación del 2026-10-26 para el repo. Investigación vía
índice web; ninguna fuente se verificó en navegador en vivo.

## Hallazgo central y honesto

NO existe un pipeline interno público de Apple, Stripe o Linear para sus
videos de producto. Lo que sigue se sostiene con lo sí verificable:
créditos reales (BUCK para Microsoft), casos de estudio y sistemas de
motion de interfaz documentados. El caso «iPhone de Apple» de Sktch
Studios es un proyecto personal, no un encargo de Apple.

## Pipeline en 11 etapas

1. Brief y mensaje único.
2. Guion y voz en off.
3. Storyboard y styleframes.
4. Animatic y previs.
5. Reconstrucción de la UI en Figma.
6. Modelado y lookdev.
7. Animación.
8. Render por pases.
9. Compositing y color.
10. Audio.
11. Entrega.

Cada etapa tiene un coste de cambio distinto: lo que se decide tarde
(guion, mensaje) es lo caro de corregir; lo visual se itera antes.

## Herramientas por etapa

- Figma: reconstrucción de la UI.
- Illustrator / Photoshop: assets.
- Cinema 4D o Blender: 3D.
- Octane / Redshift / Arnold: render.
- After Effects: centro del pipeline (composición y motion).
- Cavalry: 2D procedural, complemento de After Effects (gratis para
  individuos desde v2.7, abril 2026).
- Rive: state machines para producto interactivo, no produce video.
- Lottie: solo reproduce animación, no la crea.
- Remotion: video programático con React.
- GSAP / Framer: web, no video.
- Rotato / SmoothCapture: mockup rápido sin pipeline completo.

Flujo canónico: Figma → C4D/Blender + Octane/Redshift → After Effects →
color y audio.

## 2.5D vs 3D real

La «prueba de la órbita» decide: si la cámara orbita el objeto y se ven
sus lados, hace falta 3D real; si el movimiento es frontal con parallax,
basta 2.5D. Ejemplos: Moonb y Yans Cyclops en 2.5D; Sktch iPhone en 3D;
BUCK Surface mezclando live-action con 3D. El híbrido (shell 3D + UI 2D)
es lo más frecuente en SaaS.

Costes orientativos (cifras de freelance y agencia, NO presupuestos de
Apple o BUCK, que no son públicos): 60 s en 2D, 2–4 semanas; 2.5D, 4–5
semanas; 3D, 4–8 semanas y hasta 3+ meses en hero fotorealista.

## Sistemas de motion con valores

- Material 3: estándar cubic-bezier(0.2, 0, 0, 1); emphasized-decelerate
  (0.05, 0.7, 0.1, 1); emphasized-accelerate (0.3, 0, 0.8, 0.15);
  duraciones 50–1000 ms en 16 pasos, enfatizada 500 ms.
- Carbon: productiva (0.2, 0, 0.38, 0.9); expresiva (0.4, 0.14, 0.3, 1).
- Apple: solo filosofía HIG y springs secundarios (damping 1.0 por
  defecto); sin sistema con valores publicado.
- Escala genérica: micro 100–200 ms, UI 200–400 ms, hero 400–800 ms,
  cámara de video 800–2000 ms. Stagger 40–80 ms en listas y 20–40 ms en
  rejillas, tope 600–800 ms. Regla 1/3. Las salidas son más rápidas que
  las entradas.
- Stripe: solo descripción cualitativa (artículo de opinión), no
  verificado. Duolingo: sin sistema con valores localizado.

## Roles y tamaños de equipo

De los créditos reales de BUCK Surface Pro: director creativo de grupo,
director creativo, Head of 3D, director técnico / supervisor VFX,
storyboard, previs, compositing, editor, colorista y sonido externo.
Tamaños por alcance: 3–5 personas para SaaS en 2.5D; 15–25 para un film
tipo BUCK.

## Fuentes

- https://buck.co/work/microsoft-surface-pro
- https://www.moonb.io/blog/2-5d-animation
- https://www.sktchstudios.com/cgcommercials/iphone14commercial
- https://artofstyleframe.com/blog/easing-curves-motion-design-guide/
- https://adamarant.com/en/blog/brand-motion-design-how-one-easing-curve-sets-a-products-tone
- https://schoolofmotion.com/blog/cavalry-houdini-of-2d-after-effects
- https://www.smoothcapture.app/blog/3d-product-animation-for-apps
