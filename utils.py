import networkx as nx
import matplotlib.pyplot as plt


def extrair_prompt(prompt):
    
    _,__, separado = prompt.split("The graph has the following edges:")
    comEspaco, task = separado.split("Operation:")
    arestas = comEspaco.strip()
    parts = task.split("You should immediately return")[0].strip()


    if parts.startswith("Find"):
        
        node = parts.split(".")[0]
        return arestas, node.split(" ")[-1], 0, None

    else:
    
        node, depth_part = parts.split(" with depth ")
        
        depth = int(depth_part.split(".")[0])

        return arestas, node.split(" ")[-1], 1, depth
    
def extrair_gabarito(gabarito):
    
    oficial = []
    for ins in gabarito:
        oficial.append(str(ins))

    return oficial 

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
        for destino in destinos:
            G.add_edge(origem, destino)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(14, 8))
    nx.draw(G, pos, with_labels=True, arrows=True, node_color="lightgreen", edge_color="gray", font_size=8)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()

def desenhar_subgrafo_colorido(individuo, grafo, resposta_correta, titulo="Subgrafo com origem destacada"):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph()
    
    for origem in individuo:
        for destino in grafo.get(origem, []):
            G.add_edge(origem, destino)

    pos = nx.spring_layout(G, seed=42)

    origem_inicial = individuo[0] if individuo else None
    acertos = set(individuo) & set(resposta_correta)
    erros = set(individuo) - acertos

    cores_nos = []
    for node in G.nodes():
        if node == origem_inicial:
            cores_nos.append("royalblue")
        elif node in acertos:
            cores_nos.append("limegreen")
        elif node in erros:
            cores_nos.append("salmon")
        else:
            cores_nos.append("lightgray")

    plt.figure(figsize=(12, 7))
    nx.draw(G, pos,
            with_labels=True,
            arrows=True,
            node_color=cores_nos,
            edge_color="gray",
            font_size=8,
            node_size=1300)

    plt.title(titulo)
    plt.tight_layout()
    plt.show()