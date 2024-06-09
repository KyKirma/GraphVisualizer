import networkx as nx
import random

# Definir parâmetros
num_nodes = 50
edge_probability = 0.2

# Gerar grafo aleatório
G = nx.gnp_random_graph(num_nodes, edge_probability, directed=True)

# Criar arquivo CSV
with open('grafo_aleatorio.csv', 'w') as f:
    for edge in G.edges:
        source, target = edge
        f.write(f"{source},{target}\n")