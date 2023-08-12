import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q01 import non_neighbor

# Ambiente para testes manuais
G = nx.Graph()
G.add_nodes_from([2, 3, 4])
G.add_edges_from([(2, 3), (2, 4), (2, 2)])
M = nx.Graph()

v = 3
ns = non_neighbor(G, v)

print(f"Não vizinhos de {v}: {ns}")
draw_graph(G)