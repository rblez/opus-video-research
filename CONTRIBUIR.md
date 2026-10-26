# Contribuir

Este repo investiga una pregunta, no defiende una respuesta. Toda
contribución debe mantener esa honestidad.

## Cómo contribuir

1. Elige un issue abierto (o abre uno nuevo con la pregunta concreta).
2. Crea un experimento numerado: `experiments/NNN-nombre/` con:
   - el script o código (`gen.py` o equivalente),
   - `NOTAS.md` con qué se hizo, cómo correrlo y qué se verificó,
   - el video resultante (MP4 pequeño; no subas los frames sueltos).
3. Abre un PR a `main` describiendo qué cambia y qué verificaste.

## Reglas

- Todo en español.
- Nada se da por verificado sin ejecutarlo. Si no corrió, se escribe
  «sin verificar», no se afirma.
- Ningún video se da por bueno sin verlo antes: decodificación completa
  del MP4 entregado sin errores + muestreo de frames a lo largo de todo
  el video. Revisar frames sueltos antes de codificar no cuenta.
- No inventar datos, cifras ni citas. Todo dato en pantalla o en notas
  lleva su procedencia (captura, documento o fuente enlazada).
- No subir frames sueltos, capturas de verificación ni `__pycache__`
  (ver `.gitignore`). El repo guarda código, notas y el MP4 final.
- Si una hipótesis se cae con evidencia, se registra la corrección en
  `INVESTIGACION.md`, no se borra la hipótesis original.
