# IA en la práctica: hoja de ruta

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## Qué es

Este es un kit de estudio y práctica sobre inteligencia artificial para quienes quieren comprender el tema y aplicar una primera mejora en el trabajo. Reúne el análisis de un vídeo, un glosario y plantillas de diagnóstico, instrucciones y evaluación. Empiezas con una tarea real y compruebas el resultado antes de automatizar. Para usar los documentos, basta con leer y copiar; el evaluador opcional funciona con Python, sin servicios externos.

## Guía de uso

[Guía en español](https://inematds.github.io/roteiro-ia-pratica/guia/es/).

## Conocimiento y recursos

Los siguientes documentos están en portugués:

- [Análisis crítico y aplicaciones](conhecimento/analise.md)
- [Glosario](conhecimento/glossario.md)
- [Fuentes y capítulos](fontes/README.md)
- [Diagnóstico del proceso](recursos/diagnostico-de-processo.md)
- [Plantilla de prompt](recursos/prompt-de-trabalho.md)
- [Prueba piloto de siete días](recursos/piloto-sete-dias.md)
- [Brief de la prueba piloto](recursos/brief-de-piloto.md)
- [Hoja de evaluación](recursos/avaliacao.csv)
- [Lista de control de calidad](recursos/checklist-de-qualidade.md)

## Evaluación local opcional

Python 3, solo biblioteca estándar. Completa la hoja antes de calcular:

```bash
python3 scripts/avaliar.py recursos/avaliacao.csv
python3 -m unittest discover -s tests -v
```

El cálculo incluye revisión y corrección; los casos incompletos quedan pendientes. No hay llamadas a modelos ni a servicios externos.

## Origen y límites

Análisis del vídeo [The Last AI Roadmap Video You’ll Ever Watch, de Nick Saraev](https://www.youtube.com/watch?v=KjKlBvX9G7w). Los recursos de práctica son originales y están identificados como complementos. No reproducimos la transcripción íntegra ni prometemos resultados económicos.

La guía tiene versiones PT/EN/ES. Los documentos detallados y los recursos están en portugués.

## Producción de vídeos

Guiones y estado en [roteiros](roteiros/) y [tasks/current.md](tasks/current.md), en portugués. La producción audiovisual y las publicaciones pendientes no deben presentarse como terminadas.

- [Catálogo de recursos citados y complementarios (en portugués)](recursos/catalogo-de-estudo.md)
