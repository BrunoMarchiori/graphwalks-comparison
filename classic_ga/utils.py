import networkx as nx
import matplotlib.pyplot as plt

def desenhar_subgrafo(individuo, grafo, titulo="Subgrafo do indivíduo"):
    G = nx.DiGraph()
    for origem in individuo:
        for destino in grafo.get(origem, []):
            G.add_edge(origem, destino)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", arrows=True)
    plt.title(titulo)
    plt.show()

def construir_grafo(arestas):
    """
    Constrói um dicionário de adjacência a partir de uma lista de arestas do tipo 'origem -> destino'.
    """
    grafo = {}
    for linha in arestas:
        if "->" not in linha:
            continue
        origem, destino = map(str.strip, linha.split("->"))
        if origem not in grafo:
            grafo[origem] = []
        grafo[origem].append(destino)
    return grafo