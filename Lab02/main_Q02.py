import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q02 import walk_type

G1 = nx.read_graphml("gtufcg/graphs/s-u-cy-sc-p-b-01.graphml")
#print(f"Vértices: {G1.nodes}")
#print(f"Arestas: {G1.edges}\n")

lists = [['n0','n2','n3','n2','n0'],
         ['n0','n2','n3','n1','n0'],
         ['n0','n2','n3','n2','n3','n1','n0','n2'],
         ['n0','n2','n3','n1'],
         ['n3','n2','n0','n1','n3','n5','n6','n4','n3'],
         ['n0', 'n2', 'n3', 'n6', 'n3', 'n1', 'n0', 'n2']]

l = [0,4,99]
G1 = nx.turan_graph(6,3)
#for w in lists:
 # print(f"{w}: {walk_type(G1,w)}")
print(walk_type(G1, l))
#draw_graph(G1)