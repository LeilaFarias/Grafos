import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q03 import graph_types

G5 = nx.petersen_graph()
print(graph_types(G5))
draw_graph(G5)

print(graph_types(G = nx.trivial_graph()))