import unittest
import networkx as nx
from src.Q03 import graph_types

class Test_graph_types (unittest.TestCase):
  
  def test_grafo_nulo (self):
    G = nx.Graph()
    result = graph_types(G)
    self.assertCountEqual(result,["Simples","Nulo","Vazio","Bipartido"])

  def test_grafo_trivial (self):
    G = nx.trivial_graph()
    result = graph_types(G)
    self.assertCountEqual(result,["Simples","Trivial","Vazio","Bipartido"])

  def test_grafo_comloop (self):
    G = nx.Graph([(0,0)])
    result = graph_types(G)
    self.assertCountEqual(result,["Pseudografo"])

  def test_grafo_comarestasparalelas (self):
    G = nx.MultiGraph([(0,1),(1,0)])
    result = graph_types(G)
    self.assertCountEqual(result,["Multigrafo", "Bipartido"])

  def test_grafo_simples (self):
    G = nx.Graph([(0,1),(1,2)])
    result = graph_types(G)
    self.assertCountEqual(result,["Simples", "Bipartido"])

  def test_path_graph (self):
    G = nx.path_graph(8)
    result = graph_types(G)
    self.assertCountEqual(result,["Simples", "Bipartido"])

  def test_cycle_even_graph (self):
    G = nx.cycle_graph(8)
    result = graph_types(G)
    self.assertCountEqual(result,["Simples", "Bipartido"])

  def test_K5 (self):
    G = nx.complete_graph(5)
    result = graph_types(G)
    self.assertCountEqual(result,["Simples"])

if __name__ == '__main__':
    unittest.main(verbosity=2)