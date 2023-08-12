# Escreva uma função, graph_types, que classifica um grafo não-direcionado, 
# considerando as seguintes categorias: 
#     Simples, Multigrafo, Pseudografo, Trivial, Nulo, Vazio, Bipartido. 
# Um mesmo grafo pode possuir mais de uma destas características. 
# Por exemplo, o grafo Trivial é também um grafo Simples, Vazio e Bipartido. 
# A função deve retornar uma lista com todas as classificações que podem ser 
# dadas ao grafo recebido como parâmetro, em qualquer ordem.
# Dicas:
#    Use o método number_of_edges da classe Graph para determinar a quantidade de arestas 
#    entre dois vértices (ver exercícios resolvidos Aula 02)
#    Use a função number_of_selfloops da seção Functions de NetworkX para determinar 
#    se o grafo possui loops
#    Use a função is_bipartite para testar se o grafo é bipartido

import networkx as nx

def graph_types (G):

  caracteristicas = []

  if nx.is_empty(G):
    caracteristicas.append("Vazio")
    if nx.number_of_nodes(G) == 0:
      caracteristicas.append("Nulo")
    elif nx.number_of_nodes(G) == 1:
      caracteristicas.append("Trivial")
  
  for v1 in G.nodes:
    for v2 in G.nodes:
      if G.number_of_edges(v1, v2) > 1:
        caracteristicas.append("Multigrafo")
      break

  if nx.number_of_selfloops(G) > 0:
    caracteristicas.append("Pseudografo")

  if "Multigrafo" not in caracteristicas and "Pseudografo" not in caracteristicas:
    caracteristicas.append("Simples")  

  if nx.is_bipartite(G):
    caracteristicas.append("Bipartido")


  return caracteristicas