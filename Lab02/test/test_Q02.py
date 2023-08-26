# Use este comando no terminal para executar esta suite de testes
# python -m unittest -v test/test_Q02.py
import unittest
import networkx as nx
from parameterized import parameterized
from src.Q02 import walk_type

# Test Data
Trivial = nx.complete_graph(1)
Barbell = nx.barbell_graph(4,1)
print("Barbell")
Turan = nx.turan_graph(6,3)
print("Turan")

class Test_walk_type (unittest.TestCase):

  @parameterized.expand([
      ['Grafo Trivial', Trivial, [0], "caminho"],
      ['Barbell1',Barbell, [0], "caminho"],
      ['Barbell2',Barbell, [0,1], "caminho"],
      ['Barbell3',Barbell, [0,1,3,5], "não é passeio"],
      ['Barbell4',Barbell, [3,4,5,8], "caminho"],
      ['Barbell5',Barbell, [2,1,3,4,5,7,6,5], "passeio aberto"],
      ['Barbell6',Barbell, [2,1,2], "passeio fechado"],
      ['Barbell7',Barbell, [5,6,7,8,5], "ciclo simples"],
      ['Turan1',Turan,[4,3,1,5,3,0,4],"ciclo"],
      ['Turan2',Turan,[0,5,1,2],"caminho"]
  ])

  def test_base (self,name,G,X,expected_result):
    result = walk_type(G,X)
    self.assertEqual(result,expected_result)

  def test_None (self):
    self.assertIsNone(walk_type(None,[0]))
    self.assertIsNone(walk_type(Turan, None)) 

  def test_not_vertex (self):
     self.assertIsNone(walk_type(Turan, [0,4,99]))

if __name__ == '__main__':
    unittest.main(verbosity=2)