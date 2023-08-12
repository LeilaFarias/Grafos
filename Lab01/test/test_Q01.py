import unittest
import networkx as nx
from src.Q01 import non_neighbor

# Testes Automáticos para a função non_neighbor
class Test_non_neighbor (unittest.TestCase):

  def test_grafo_trivial (self):
    G = nx.trivial_graph()
    result = non_neighbor(G,0)
    self.assertCountEqual(result,[0])

  def test_grafo_comloop (self):
    G = nx.Graph([(0,0),(0,1),(1,2)])
    result = non_neighbor(G,0)
    self.assertCountEqual(result,[2])

  def test_grafo_comarestasparalelas (self):
    G = nx.MultiGraph([(0,1),(1,0),(1,2)])
    result = non_neighbor(G,0)
    self.assertCountEqual(result,[0,2])

  def test_grafo_simples (self):
    G = nx.Graph([(0,1),(1,2),(2,3),(0,4)])
    result = non_neighbor(G,1)
    self.assertCountEqual(result,[1,3,4])

  def test_null (self):
    self.assertTrue(non_neighbor(nx.Graph(),0) is None)

  def test_None (self):
    self.assertTrue(non_neighbor(None,0) is None)

  def test_not_vertex (self):
    G = nx.Graph([(0,1),(1,2),(2,3),(0,4)])
    self.assertTrue(non_neighbor(G,9) is None)

if __name__ == '__main__':
    unittest.main(verbosity=2)