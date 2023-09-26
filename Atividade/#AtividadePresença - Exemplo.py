#Atividade/Presença - Exemplo.
#Aluno: Áquila Daniel. Matrícula: 2023211510068. Turma: Sistemas para internet, P1B, Noite.
from aula06 import divisao
import unittest
from conceito_aula06 import multiplicar
from conceito_aula06 import divisao
from conceito_aula06 import soma

class TestMultiplicar(TestCase):
    class TestMultiplicar(unittest.TestCase):
        def test_multiplicar_dois_por_tres(self):
            self.assertEqual(multiplicar(2,3), 6)

class TestDivisao(TestCase):
    class TestDivisao(unittest.TestCase):

        def test_divisao_dois_por_tres(self):
            self.assertEqual(divisao(2,3), -1)

class TestSoma(unittest.TestCase):

    def test_soma_dois_por_tres(self):
        self.assertEqual(soma(2,3), 5)

if __name__ == "__main__":
    unittest.main()
