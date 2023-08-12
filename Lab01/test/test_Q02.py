import unittest
import networkx as nx
from src.Q02 import candidates
from parameterized import parameterized

# Testes Automáticos para a função candidates

G5 = nx.Graph([('Joao', 'Maria'), ('Joao', 'Otavio'), ('Maria', 'Cristina'), 
               ('Maria', 'Eduardo'), ('Eduardo', 'Cristina'), ('Cristina', 'Otavio'), 
               ('Cristina', 'Jose'), ('Otavio', 'Jose')])

class Test_candidates (unittest.TestCase):
  
  @parameterized.expand([
      ["Maria",G5,"Maria",['Jose', 'Otavio']],
      ["Joao",G5,"Joao",['Cristina', 'Eduardo', 'Jose']],
      ["Eduardo",G5,"Eduardo",['Joao', 'Jose', 'Otavio']],
      ["Cristina",G5,"Cristina",['Joao']],
      ["Otavio",G5,"Otavio",['Eduardo', 'Maria']],
      ["Jose",G5,"Jose",['Eduardo', 'Joao', 'Maria']]
  ])

  def test_base00 (self,name,G,p,expected_result):
    result = candidates(G,p)
    self.assertEqual(result,expected_result)

  def test_None (self):
    self.assertTrue(candidates(None," ") is None)
    self.assertTrue(candidates(G5,None) is None)

if __name__ == '__main__':
    unittest.main(verbosity=2)