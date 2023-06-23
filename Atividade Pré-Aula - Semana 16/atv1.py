import networkx as nx
import matplotlib.pyplot as plt

# Criação do grafo
G = nx.Graph()

# Adição dos nós
G.add_nodes_from(['A', 'B', 'C'])

# Adição das arestas
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C')])

# Visualização do grafo
nx.draw(G, with_labels=True)
plt.show()
