# Use este comando no terminal para executar esta suite de testes
# python -m unittest -v test/test_Q01.py

import unittest
import networkx as nx
from parameterized import parameterized
from src.Q01 import triangles

# Test Data
Null = nx.Graph()
Trivial = nx.complete_graph(1)
K3 = nx.complete_graph(3)
K5 = nx.complete_graph(5)
K3_3 = nx.complete_multipartite_graph([0,1,2],[3,4,5])
E6 = nx.empty_graph(6)
W4 = nx.wheel_graph(4)
Bull = nx.bull_graph()

class Test_triangles (unittest.TestCase):

  @parameterized.expand([
      ['Null',Null,[]],
      ['Grafo Trivial', Trivial, []],
      ['K3',K3,[[0, 1, 2]]],
      ['K5',K5,[[0, 1, 2],[0, 1, 3],[0, 1, 4],[0, 2, 3],[0, 4, 2],[0, 3, 4],[1, 2, 3],[1, 2, 4],[1, 3, 4],[2, 3, 4]]],
      ['K3_3',K3_3,[]],
      ['E6',E6,[]],
      ['W4',W4,[[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]],
      ['Bull',Bull,[[2,1,0]]],
  ])

  def test_base (self,name,G,expected_result):
    result = triangles(G)
    self.assertEqual(len(result),len(expected_result))
    self.assertTrue(all(any(set(l2)==set(l1) for l1 in expected_result) for l2 in result))

  def test_None (self):
    self.assertTrue(triangles(None) is None)

if __name__ == '__main__':
    unittest.main(verbosity=2)