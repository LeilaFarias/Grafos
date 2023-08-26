# Implemente a função **walk_type** que recebe um grafo simples **G** e uma lista de vértices **W** 
# e determina o tipo de passeio que a lista representa:
#
#  * não é passeio
#  * passeio aberto
#  * passeio fechado
#  * caminho
#  * ciclo
#  * ciclo simples

# onde *passeio aberto* é todo passeio cuja origem e destino são diferentes e *passeio fechado* é 
# todo passeio cuja origem e destino são iguais.
# Note que todo ciclo é um passeio fechado, mas a função deve retornar a classificação mais 
# específica. As classificações passeio aberto e passeio fechado só devem ser dadas para passeios 
# que não podem ser classificados como caminho, ciclo ou ciclo simples.
#
# Como exemplo, considere o grafo "s-u-cy-sc-p-b-01.graphml" (ver main_Q02.py). 
# A função deve classificar as seguintes sequências de vértices como:
#
#    ['n0','n2','n3','n2','n0']: passeio fechado
#    ['n0', 'n2', 'n3', 'n1', 'n0']: ciclo simples
#    ['n0', 'n2', 'n3', 'n2', 'n3', 'n1', 'n0', 'n2']: passeio aberto
#    ['n0', 'n2', 'n3', 'n1']: caminho
#    ['n3', 'n2', 'n0', 'n1', 'n3', 'n5', 'n6', 'n4', 'n3']: ciclo
#    ['n0', 'n2', 'n3', 'n6', 'n3', 'n1', 'n0', 'n2']: não é passeio
#
#    passeio -> função path
#    passeio fechado -> se é passeio, checa se o ultimo e o primeiro vertice sao iguais, se não
#    for entao classifica como aberto
#    caminho -> se é passeio, nao repete vertice
#    ciclo -> se é passeio, checa se tem mais de 3 vertices o ultimo e o primeiro vertice sao iguais e nao repete arestas
#    ciclo simpes -> se é ciclo, checa se todos os vertices são diferentes
#
#
#
# *Dica:*
#* Use a função *repeated_edges* abaixo para determinar se um passeio possui arestas repetidas
# * Consulte o notebook da Aula 03, tópico Passeio e Caminho.
 
import networkx as nx

def repeated_edges(G, W):
  count_edges = {(u,v):0 for (u,v) in G.edges}
  for i in range(len(W)-1):
    u,v = W[i],W[i+1]
    if (u,v) in count_edges.keys():
      count_edges[(u,v)] += 1
    elif (v,u) in count_edges.keys():
      count_edges[(v,u)] += 1
  return any(count_edges[(u,v)] > 1 for (u,v) in count_edges)

def walk_type (G, W): 

  if (G is None or W is None):
    return None
  for temp in W:
    if (temp not in G.nodes()):
      return None

  result = "não é passeio"

  if (nx.is_path(G, W)):
    if (W[0] == W[len(W) - 1]):
      result = "passeio fechado"
    else:
      result = "passeio aberto"

    if (nx.is_simple_path(G, W)):
      result = "caminho"
    
    if (len(W) >= 3 and W[0] == W[len(W) - 1] and repeated_edges(G, W) == 0):
      result = "ciclo"
      if (not temVertRepetido(G, W)):
        result = "ciclo simples"
        
  return result

def temVertRepetido(G, W):
  aux = []
  vertRepetido = False
  for i in range(len(W) - 1):
    if (W[i] in aux):
      vertRepetido = True
    aux.append(W[i])

  return vertRepetido