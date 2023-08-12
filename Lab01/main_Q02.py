import networkx as nx
from gtufcg.util.networkx_util import read_multiple_CSV, draw_graph
from src.Q02 import candidates

# Ambiente para testes manuais
G5 = nx.Graph()
read_multiple_CSV(G5,vfilename='gtufcg/datasets/nomes.csv',vid='nome',
                     efilename='gtufcg/datasets/amigos.csv', esourceid='nome1', etargetid='nome2')
print(f"Vértices: {set(G5.nodes)}")
print(f"Arestas: {set(G5.edges)}")
pessoa = "Maria"
print(f"Candidatos a amigos de Maria: {candidates(G5,pessoa)}")
draw_graph(G5)