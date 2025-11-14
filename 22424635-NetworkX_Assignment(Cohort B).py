import networkx as nx
import matplotlib.pyplot as plt

# Define nodes
nodes = ["Francis", "Boakye", "Mensah", "Kofi", "Dorothy", "Kusi"]

# Define edges
connected_nodes = ["Francis", "Boakye", "Mensah", "Kofi", "Dorothy"]
edges = [(a, b) for i, a in enumerate(connected_nodes) for b in connected_nodes[i+1:]]

# Create graph
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Compute metrics-
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_distribution = dict(G.degree())
isolated_nodes = list(nx.isolates(G))

print("Number of nodes:", num_nodes)
print("Number of edges:", num_edges)
print("Degree distribution:", degree_distribution)
print("Isolated nodes:", isolated_nodes)

# Visualization
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12, edge_color='gray')
plt.title("Research Group Network")
plt.savefig("research_group_network.png")
plt.show()
