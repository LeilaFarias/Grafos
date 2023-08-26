# Implemente a função **triangles** que recebe um grafo simples G como entrada e 
# retorna uma lista com grupos de 3 vértices que são mutuamente adjacentes entre si.
# Como exemplo, considere o grafo G, onde:
#
#    V(G) = {0,1,2,3}
#    E(G) = {01,02,12,13,23}
#
# Este grafo possui dois grupos de vértices mutuamente adjacentes. Portanto, a função deverá retornar a seguinte lista:
#
#    [[0,1,2], [1,2,3]]
#
# Os vértices e as listas não precisam estar necessariamente na nesta ordem.

import networkx as nx

def triangles (G):

  if (G is None):
    return None
  
  result = []

  if (nx.number_of_nodes(G) > 1 and not nx.is_empty(G)):
    for v in G.nodes():
      for j in G.neighbors(v):
         for u in G.neighbors(j):

          if (G.has_edge(u, v) and sorted([u, v, j]) not in result):
            result.append(sorted([u, j, v]))

  return result  

