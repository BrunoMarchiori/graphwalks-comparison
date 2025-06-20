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