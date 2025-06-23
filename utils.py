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

def construir_grafo(texto_arestas):
    grafo = {}
    linhas = texto_arestas.strip().splitlines()
    for linha in linhas:
        if "->" not in linha:
            continue
        origem, destino = map(str.strip, linha.split("->"))
        if origem not in grafo:
            grafo[origem] = []
        grafo[origem].append(destino)
    return grafo

def visualizar_grafo_completo(grafo, titulo="Visualização do Grafo Completo"):
    G = nx.DiGraph()
    for origem, destinos in grafo.items():
        print(origem, destinos)
        for destino in destinos:
            print(destino)
            G.add_edge(origem, destino)
        print("\n")

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, with_labels=True, arrows=True, node_color="lightgreen", edge_color="gray", font_size=8)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()