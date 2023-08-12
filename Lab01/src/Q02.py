# Considere um grafo onde os vértices são nomes de pessoas e as arestas relacionam 
# nomes de pessoas que são amigas.
# Implemente a função **candidates** que retorna uma lista com os nomes 
# de *candidatos a amigos* que uma certa *pessoa* pode conhecer, 
# em ordem alfabética. Os candidatos a amigos são amigos diretos de amigos 
# de *pessoa* que ainda não são amigos de *pessoa*. O nome da pessoa está 
# definido na variável **p**.

# pessoa = vértice
# procura todos os adjacentes ao vértice p
# pega todos os adjacentes aos adjacentes do vértice p e coloca na lista
# Exemplo:
# Para o grafo:
#    ['Joao', 'Maria', 'Eduardo', 'Cristina', 'Otavio', 'Jose']
#    [('Joao', 'Maria'), ('Joao', 'Otavio'), ('Maria', 'Cristina'), 
#     ('Maria', 'Eduardo'), ('Eduardo', 'Cristina'), ('Cristina', 'Otavio'), 
#      ('Cristina', 'Jose'), ('Otavio', 'Jose')]
# Se pessoa = "Maria", a função deve retornar: ['Jose','Otávio']

import networkx as nx
def candidates (G,p):

  if G is None or p is None:
    return None

  candidatos = []

  for vert in G.adj[p]:
    for vert2 in G.adj[vert]:
      if vert2 not in G.adj[p] and vert2 not in candidatos and vert2 != p:
        candidatos.append(vert2)


  return sorted(candidatos)