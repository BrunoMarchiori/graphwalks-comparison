import classic_ga.genetic_solver as gs
import classic_ga.utils as utga

graph = {
    "cfcd208495": ["cfcd208495", "1679091c5a", "c81e728d9d", "c4ca4238a0"],
    "c4ca4238a0": ["c9f0f895fb", "45c48cce2e", "eccbc87e4b"],
    "c81e728d9d": ["45c48cce2e", "eccbc87e4b", "c9f0f895fb"],
    "eccbc87e4b": ["d3d9446802", "a87ff679a2", "c4ca4238a0"],
    "a87ff679a2": ["1679091c5a", "eccbc87e4b", "cfcd208495", "e4da3b7fbb"],
    "e4da3b7fbb": ["c4ca4238a0", "1679091c5a", "45c48cce2e"],
    "1679091c5a": ["8f14e45fce", "e4da3b7fbb", "a87ff679a2"],
    "8f14e45fce": ["45c48cce2e", "e4da3b7fbb", "8f14e45fce", "cfcd208495"],
    "c9f0f895fb": ["eccbc87e4b", "cfcd208495", "8f14e45fce"],
    "45c48cce2e": ["cfcd208495", "1679091c5a", "a87ff679a2"],
    "d3d9446802": ["8f14e45fce", "d3d9446802", "45c48cce2e", "e4da3b7fbb"]
}

utga.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="parents",
    target_node="8f14e45fce",
    generations=20,
)

result = solver.evolve()
print("Final Answer:", result)
utga.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")

graph = {
    "cfcd208495": ["eccbc87e4b", "c9f0f895fb", "e4da3b7fbb", "1679091c5a", "c4ca4238a0"],
    "c4ca4238a0": ["1679091c5a", "c4ca4238a0", "eccbc87e4b", "c9f0f895fb"],
    "c81e728d9d": ["e4da3b7fbb", "a87ff679a2", "1679091c5a"],
    "eccbc87e4b": ["eccbc87e4b", "e4da3b7fbb", "8f14e45fce", "c4ca4238a0"],
    "a87ff679a2": ["cfcd208495", "c9f0f895fb", "e4da3b7fbb"],
    "e4da3b7fbb": ["1679091c5a", "a87ff679a2", "8f14e45fce", "c4ca4238a0"],
    "1679091c5a": ["c4ca4238a0", "a87ff679a2", "e4da3b7fbb", "cfcd208495"],
    "8f14e45fce": ["a87ff679a2", "cfcd208495", "c9f0f895fb", "eccbc87e4b", "c81e728d9d"],
    "c9f0f895fb": ["c81e728d9d", "8f14e45fce", "eccbc87e4b"]
}

utga.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="parents",
    target_node="e4da3b7fbb",
    generations=30,
)

result = solver.evolve()
print("Final Answer:", result)
utga.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")

arestas = """
    cfcd208495 -> 45c48cce2e
    c4ca4238a0 -> c74d97b01e
    c81e728d9d -> 1c383cd30b
    eccbc87e4b -> d645920e39
    a87ff679a2 -> e369853df7
    e4da3b7fbb -> c74d97b01e
    1679091c5a -> 70efdf2ec9
    8f14e45fce -> d645920e39
    c9f0f895fb -> aab3238922
    45c48cce2e -> 1f0e3dad99
    d3d9446802 -> d645920e39
    6512bd43d9 -> 34173cb38f
    c20ad4d76f -> eccbc87e4b
    c51ce410c1 -> 182be0c5cd
    aab3238922 -> a1d0c6e83f
    9bf31c7ff0 -> a5771bce93
    c74d97b01e -> 70efdf2ec9
    70efdf2ec9 -> aab3238922
    6f4922f455 -> c4ca4238a0
    1f0e3dad99 -> f7177163c8
    98f1370821 -> c20ad4d76f
    3c59dc048e -> aab3238922
    b6d767d2f8 -> 4e732ced34
    37693cfc74 -> e369853df7
    1ff1de7740 -> 33e75ff09d
    8e296a067a -> 3c59dc048e
    4e732ced34 -> c81e728d9d
    02e74f10e0 -> 6ea9ab1baa
    33e75ff09d -> c74d97b01e
    6ea9ab1baa -> 98f1370821
    34173cb38f -> 37693cfc74
    c16a5320fa -> 33e75ff09d
    6364d3f0f4 -> 3c59dc048e
    182be0c5cd -> a87ff679a2
    e369853df7 -> 8e296a067a
    1c383cd30b -> a5771bce93
    19ca14e7ea -> d3d9446802
    a5bfc9e079 -> 1c383cd30b
    a5771bce93 -> 98f1370821
    d67d8ab4f4 -> d3d9446802
    d645920e39 -> 9bf31c7ff0
    3416a75f4c -> c9f0f895fb
    a1d0c6e83f -> 182be0c5cd
    17e62166fc -> 182be0c5cd
    f7177163c8 -> c16a5320fa
    6c8349cc72 -> 17e62166fc
    """

graph = utga.construir_grafo(arestas)
utga.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="parents",
    target_node="3416a75f4c",
    generations=1000,
)

result = solver.evolve()
print("Final Answer:", result)
utga.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")