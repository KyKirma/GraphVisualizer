import networkx as nx
import matplotlib as plt

G = nx.Graph()

# Adicione nós ao grafo
nodes = ['A', 'B', 'C', 'D', 'E']
for node in nodes:
    G.add_node(node)
# Adicione arestas com pesos
G.add_edge('A', 'B', weight=7)
G.add_edge('B', 'C', weight=9)
G.add_edge('C', 'D', weight=8)
G.add_edge('D', 'E', weight=6)
G.add_edge('A', 'E', weight=14)

# Definir opções de layout e cores
options = {'node_color': 'lightblue', 'edgecolors': 'black', 'width': 2}

# Desenhar o grafo e exibir labels das arestas com pesos
nx.draw_networkx(G, labels=True, with_labels=True, edge_labels=G.get_edge_weights(), font_size=10, **options)

# Exibir o grafo
plt.show()
