#!/usr/bin/env python3
"""Resume um piloto local; não chama serviços nem modelos."""
import argparse
import csv
import json
import math
from pathlib import Path

TEMPOS = ['tempo_manual_min', 'tempo_ia_min', 'revisao_min', 'correcao_min']
CRITERIOS = ['fatos_corretos_0_1', 'completo_0_1', 'formato_correto_0_1']


def avaliar(arquivo):
    completos, pendentes = [], []
    with Path(arquivo).open(encoding='utf-8-sig', newline='') as f:
        leitor = csv.DictReader(f)
        faltam = set(['caso', *TEMPOS, *CRITERIOS]) - set(leitor.fieldnames or [])
        if faltam:
            raise ValueError('Colunas ausentes: ' + ', '.join(sorted(faltam)))
        for linha, r in enumerate(leitor, 2):
            valores = {}
            for chave in TEMPOS + CRITERIOS:
                raw = (r.get(chave) or '').strip()
                if not raw:
                    continue
                try:
                    x = float(raw)
                except ValueError:
                    raise ValueError(f'Linha {linha}, {chave}: número inválido') from None
                if not math.isfinite(x) or x < 0 or (chave in CRITERIOS and x not in (0, 1)):
                    raise ValueError(f'Linha {linha}, {chave}: valor fora do domínio')
                valores[chave] = x
            if len(valores) != len(TEMPOS + CRITERIOS):
                pendentes.append(r['caso'])
            else:
                completos.append(valores)
    manual = sum(r[TEMPOS[0]] for r in completos)
    assistido = sum(sum(r[k] for k in TEMPOS[1:]) for r in completos)
    return {
        'casos_completos': len(completos),
        'casos_pendentes': pendentes,
        'tempo_manual_min': manual,
        'tempo_assistido_com_revisao_min': assistido,
        'tempo_economizado_min': manual - assistido,
        'reducao_percentual': round(100 * (manual - assistido) / manual, 2) if manual else None,
        'casos_aprovados_em_todos_criterios': sum(all(r[k] == 1 for k in CRITERIOS) for r in completos),
        'nota': 'Só casos completos entram no cálculo. Economia negativa indica aumento do tempo. Não extrapole uma amostra pequena.'
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv', type=Path)
    a = p.parse_args()
    try:
        resultado = avaliar(a.csv)
    except (ValueError, OSError) as e:
        p.exit(2, str(e) + '\n')
    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
