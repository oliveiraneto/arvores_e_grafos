import networkx as nx
import matplotlib.pyplot as plt

# Criação do grafo
G = nx.Graph()

# Adição dos nós
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Adição das arestas
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

# Visualização do grafo
nx.draw(G, with_labels=True)
plt.show()
