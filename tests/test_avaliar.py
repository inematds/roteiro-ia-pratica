import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path
spec = importlib.util.spec_from_file_location('avaliar', Path(__file__).parents[1] / 'scripts/avaliar.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class Avaliacao(unittest.TestCase):
    def run_csv(self, rows):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'casos.csv'
            with p.open('w') as f:
                w = csv.writer(f)
                w.writerow(['caso', *m.TEMPOS, *m.CRITERIOS])
                w.writerows(rows)
            return m.avaliar(p)

    def test_revisao_pode_eliminar_ganho(self):
        r = self.run_csv([['a', 10, 2, 7, 3, 1, 1, 1]])
        self.assertEqual(r['tempo_economizado_min'], -2)
        self.assertEqual(r['reducao_percentual'], -20)

    def test_incompleto_nao_conta_como_sucesso(self):
        r = self.run_csv([['a', 10, 2, '', 0, 1, 1, 1], ['b', 10, 2, 1, 0, 0, 1, 1]])
        self.assertEqual(r['casos_completos'], 1)
        self.assertEqual(r['casos_pendentes'], ['a'])
        self.assertEqual(r['casos_aprovados_em_todos_criterios'], 0)

    def test_valor_invalido_e_rejeitado(self):
        for valor in ['nan', 'inf', -1, 'abc']:
            with self.subTest(valor=valor), self.assertRaises(ValueError):
                self.run_csv([['a', valor, 2, 1, 0, 1, 1, 1]])

    def test_base_zero_nao_divide(self):
        self.assertIsNone(self.run_csv([['a', 0, 0, 0, 0, 1, 1, 1]])['reducao_percentual'])

if __name__ == '__main__':
    unittest.main()
