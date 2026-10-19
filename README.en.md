# AI in practice: a roadmap

**[Português](README.md) · [English](README.en.md) · [Español](README.es.md)**

## About

This artificial intelligence study and practice kit is for anyone who wants to understand the subject and make a first improvement at work. It brings together a video analysis, a glossary, and templates for assessing a process, writing a prompt and evaluating results. Start with a real task and check the outcome before automating it. To use the documents, simply read and copy them; the optional evaluation tool runs in Python without external services.

## User guide

[English guide](https://inematds.github.io/roteiro-ia-pratica/guia/en/).

## Knowledge and resources

The following documents and resources are in Portuguese:

- [Critical analysis and practical takeaways](conhecimento/analise.md)
- [Glossary](conhecimento/glossario.md)
- [Sources and chapters](fontes/README.md)
- [Process assessment](recursos/diagnostico-de-processo.md)
- [Prompt template](recursos/prompt-de-trabalho.md)
- [Seven-day pilot](recursos/piloto-sete-dias.md)
- [Pilot brief](recursos/brief-de-piloto.md)
- [Evaluation spreadsheet](recursos/avaliacao.csv)
- [Quality checklist](recursos/checklist-de-qualidade.md)

## Optional local evaluation

Python 3, standard library only. Fill in the spreadsheet before calculating:

```bash
python3 scripts/avaliar.py recursos/avaliacao.csv
python3 -m unittest discover -s tests -v
```

The calculation includes review and correction time; incomplete cases remain pending. There are no model calls or external services.

## Source and limitations

An analysis of [The Last AI Roadmap Video You’ll Ever Watch, by Nick Saraev](https://www.youtube.com/watch?v=KjKlBvX9G7w). The practice resources are original and identified as supplementary material. We do not reproduce the full transcript or promise financial results.

The guide is available in Portuguese, English and Spanish. The detailed documents and resources are in Portuguese.

## Video production

Scripts and status are available in [roteiros](roteiros/) and [tasks/current.md](tasks/current.md), both in Portuguese. Pending video production and publication work must not be presented as completed.

- [Catalog of cited and additional resources (in Portuguese)](recursos/catalogo-de-estudo.md)
