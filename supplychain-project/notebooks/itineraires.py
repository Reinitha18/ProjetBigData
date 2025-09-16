import networkx as nx
import matplotlib.pyplot as plt

# Création d'un graphe avec distances fictives
G = nx.complete_graph(6)  # 6 noeuds : 0 = entrepôt, 1-5 = clients
distances = {
    (0,1): 10, (0,2): 15, (0,3): 20, (0,4): 25, (0,5): 30,
    (1,2): 35, (1,3): 25, (1,4): 30, (1,5): 20,
    (2,3): 15, (2,4): 10, (2,5): 25,
    (3,4): 20, (3,5): 15,
    (4,5): 10
}
nx.set_edge_attributes(G, distances, "weight")

# Algorithme du plus court chemin (TSP approx)
from networkx.algorithms import approximation as approx
cycle = approx.traveling_salesman_problem(G, weight="weight")

print("Itinéraire optimal (approx) :", cycle)

# Visualisation
pos = nx.spring_layout(G, seed=42)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=800)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
path_edges = list(zip(cycle, cycle[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
plt.show()
