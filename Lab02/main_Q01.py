import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q01 import triangles
from matplotlib import colors

# Exemplo de uso da função
G1 = nx.read_graphml("gtufcg/graphs/s-u-cy-sc-p-03.graphml")
print(f"Vértices: {G1.nodes}")
print(f"Arestas: {G1.edges}")
ts = triangles(G1)
print(f"Triângulos: {ts}")

# Saída esperada: [['n18','n17','n16'],['n1','n9','n10']]
#draw_graph(G1,layoutid="kamada_kawai_layout",
        #   nset=ts,
       #    nsetcolor=list(colors.TABLEAU_COLORS.keys())[0:len(ts)+1])
