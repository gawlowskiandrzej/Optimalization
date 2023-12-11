import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt 

class drawer:
    def __init__(self):
        return
    def drawGraph(self, distances, roadload):
        G = nx.Graph()
        liczba_wierzcholkow = len(distances)

        for i in range(liczba_wierzcholkow):
            G.add_node(i+1)  # Numeracja wierzchołków od 1

        for i in range(liczba_wierzcholkow):
            for j in range(i, liczba_wierzcholkow):
                if distances[i].pathList[j] > 0:
                    G.add_edge(i+1, j+1, weight=distances[i].pathList[j], parameter=roadload[i].pathList[j])

        # Rysowanie grafu z numerami wierzchołków i dystansami
        pos = nx.fruchterman_reingold_layout(G, k=0.15)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=400, node_color='skyblue')

        # Dodanie etykiet dystansów
        edge_labels = {(i+1, j+1): f"{distances[i].pathList[j]},{roadload[i].pathList[j]}" for i in range(liczba_wierzcholkow) for j in range(i, liczba_wierzcholkow) if distances[i].pathList[j] > 0}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        plt.show()