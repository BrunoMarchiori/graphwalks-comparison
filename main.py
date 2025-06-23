import classic_ga.genetic_solver as gs
import utils as ut

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

ut.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="parents",
    target_node="8f14e45fce",
    generations=200,
)

result = solver.evolve()
resposta_correta = solver.parents(solver.target_node)
print("Final Answer:", result)
ut.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")
ut.desenhar_subgrafo_colorido(result, graph, resposta_correta, titulo="Visualização do Melhor Indivíduo com Feedback")


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

graph = ut.construir_grafo(arestas)
ut.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="parents",
    target_node="3416a75f4c",
    generations=1000,
)

result = solver.evolve()
print("Final Answer:", result)
ut.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")

arestas = """
    cfcd208495 -> a87ff679a2
    cfcd208495 -> a87ff679a2
    cfcd208495 -> e4da3b7fbb
    cfcd208495 -> c9f0f895fb
    c4ca4238a0 -> cfcd208495
    c4ca4238a0 -> 1679091c5a
    c4ca4238a0 -> e4da3b7fbb
    c4ca4238a0 -> eccbc87e4b
    c81e728d9d -> a87ff679a2
    c81e728d9d -> c81e728d9d
    c81e728d9d -> c9f0f895fb
    c81e728d9d -> cfcd208495
    eccbc87e4b -> d3d9446802
    eccbc87e4b -> d3d9446802
    eccbc87e4b -> a87ff679a2
    eccbc87e4b -> 1679091c5a
    a87ff679a2 -> c81e728d9d
    a87ff679a2 -> cfcd208495
    a87ff679a2 -> e4da3b7fbb
    a87ff679a2 -> e4da3b7fbb
    e4da3b7fbb -> c81e728d9d
    e4da3b7fbb -> cfcd208495
    e4da3b7fbb -> eccbc87e4b
    e4da3b7fbb -> 45c48cce2e
    1679091c5a -> a87ff679a2
    1679091c5a -> 8f14e45fce
    1679091c5a -> c81e728d9d
    1679091c5a -> c81e728d9d
    8f14e45fce -> d3d9446802
    8f14e45fce -> 45c48cce2e
    8f14e45fce -> eccbc87e4b
    8f14e45fce -> eccbc87e4b
    c9f0f895fb -> cfcd208495
    c9f0f895fb -> 1679091c5a
    c9f0f895fb -> a87ff679a2
    c9f0f895fb -> c81e728d9d
    45c48cce2e -> 1679091c5a
    45c48cce2e -> 45c48cce2e
    45c48cce2e -> 8f14e45fce
    45c48cce2e -> c4ca4238a0
    d3d9446802 -> 45c48cce2e
    d3d9446802 -> c9f0f895fb
    d3d9446802 -> eccbc87e4b
    d3d9446802 -> 45c48cce2e
    """

graph = ut.construir_grafo(arestas)
ut.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="bfs",
    generations=1000,
    target_node="8f14e45fce",
    depth=4
)

result = solver.evolve()
resposta_correta = solver.bfs(solver.target_node, solver.depth)
print("Final Answer:", result)
ut.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")
ut.desenhar_subgrafo_colorido(result, graph, resposta_correta, titulo="Visualização do Melhor Indivíduo com Feedback")


arestas = """
    cfcd208495 -> 8f14e45fce
    cfcd208495 -> cfcd208495
    cfcd208495 -> 37693cfc74
    c4ca4238a0 -> 182be0c5cd
    c4ca4238a0 -> c4ca4238a0
    c4ca4238a0 -> c51ce410c1
    c81e728d9d -> aab3238922
    c81e728d9d -> 182be0c5cd
    c81e728d9d -> 4e732ced34
    eccbc87e4b -> 1ff1de7740
    eccbc87e4b -> c81e728d9d
    eccbc87e4b -> c20ad4d76f
    a87ff679a2 -> c74d97b01e
    a87ff679a2 -> 6f4922f455
    a87ff679a2 -> 6f4922f455
    e4da3b7fbb -> a87ff679a2
    e4da3b7fbb -> a5bfc9e079
    e4da3b7fbb -> eccbc87e4b
    1679091c5a -> 33e75ff09d
    1679091c5a -> 33e75ff09d
    1679091c5a -> 8e296a067a
    8f14e45fce -> eccbc87e4b
    8f14e45fce -> eccbc87e4b
    8f14e45fce -> c9f0f895fb
    c9f0f895fb -> 33e75ff09d
    c9f0f895fb -> 37693cfc74
    c9f0f895fb -> 6ea9ab1baa
    45c48cce2e -> b6d767d2f8
    45c48cce2e -> c74d97b01e
    45c48cce2e -> 33e75ff09d
    d3d9446802 -> 1c383cd30b
    d3d9446802 -> 9bf31c7ff0
    d3d9446802 -> 6512bd43d9
    6512bd43d9 -> 33e75ff09d
    6512bd43d9 -> 19ca14e7ea
    6512bd43d9 -> c81e728d9d
    c20ad4d76f -> 02e74f10e0
    c20ad4d76f -> c4ca4238a0
    c20ad4d76f -> d3d9446802
    c51ce410c1 -> c81e728d9d
    c51ce410c1 -> c74d97b01e
    c51ce410c1 -> e369853df7
    aab3238922 -> 182be0c5cd
    aab3238922 -> c51ce410c1
    aab3238922 -> 8e296a067a
    9bf31c7ff0 -> c81e728d9d
    9bf31c7ff0 -> c20ad4d76f
    9bf31c7ff0 -> 1679091c5a
    c74d97b01e -> c16a5320fa
    c74d97b01e -> 1c383cd30b
    c74d97b01e -> c51ce410c1
    70efdf2ec9 -> 1c383cd30b
    70efdf2ec9 -> a5bfc9e079
    70efdf2ec9 -> 34173cb38f
    6f4922f455 -> 1679091c5a
    6f4922f455 -> 8f14e45fce
    6f4922f455 -> c81e728d9d
    1f0e3dad99 -> 6364d3f0f4
    1f0e3dad99 -> c9f0f895fb
    1f0e3dad99 -> 37693cfc74
    98f1370821 -> 1f0e3dad99
    98f1370821 -> 02e74f10e0
    98f1370821 -> a87ff679a2
    3c59dc048e -> 4e732ced34
    3c59dc048e -> 37693cfc74
    3c59dc048e -> 1c383cd30b
    b6d767d2f8 -> 1f0e3dad99
    b6d767d2f8 -> 182be0c5cd
    b6d767d2f8 -> 6ea9ab1baa
    37693cfc74 -> c20ad4d76f
    37693cfc74 -> c74d97b01e
    37693cfc74 -> e4da3b7fbb
    1ff1de7740 -> 8e296a067a
    1ff1de7740 -> 6364d3f0f4
    1ff1de7740 -> 33e75ff09d
    8e296a067a -> eccbc87e4b
    8e296a067a -> a87ff679a2
    8e296a067a -> c16a5320fa
    4e732ced34 -> 8e296a067a
    4e732ced34 -> 02e74f10e0
    4e732ced34 -> 37693cfc74
    02e74f10e0 -> 37693cfc74
    02e74f10e0 -> 1679091c5a
    02e74f10e0 -> 182be0c5cd
    33e75ff09d -> 182be0c5cd
    33e75ff09d -> cfcd208495
    33e75ff09d -> 3c59dc048e
    6ea9ab1baa -> 8e296a067a
    6ea9ab1baa -> aab3238922
    6ea9ab1baa -> 8e296a067a
    34173cb38f -> 34173cb38f
    34173cb38f -> 6f4922f455
    34173cb38f -> 45c48cce2e
    c16a5320fa -> c51ce410c1
    c16a5320fa -> 19ca14e7ea
    c16a5320fa -> e369853df7
    6364d3f0f4 -> aab3238922
    6364d3f0f4 -> 6364d3f0f4
    6364d3f0f4 -> e369853df7
    182be0c5cd -> 02e74f10e0
    182be0c5cd -> aab3238922
    182be0c5cd -> e4da3b7fbb
    e369853df7 -> c74d97b01e
    e369853df7 -> 1f0e3dad99
    e369853df7 -> 3c59dc048e
    1c383cd30b -> 1ff1de7740
    1c383cd30b -> a5bfc9e079
    1c383cd30b -> 4e732ced34
    19ca14e7ea -> aab3238922
    19ca14e7ea -> a5bfc9e079
    19ca14e7ea -> 34173cb38f
    a5bfc9e079 -> cfcd208495
    a5bfc9e079 -> 6f4922f455
    a5bfc9e079 -> c51ce410c1
    """

graph = ut.construir_grafo(arestas)
ut.visualizar_grafo_completo(graph)

solver = gs.GeneticSolver(
    graph=graph,
    operation="bfs",
    target_node="70efdf2ec9",
    depth=4,
    generations=1000
)

result = solver.evolve()
resposta_correta = solver.bfs(solver.target_node, solver.depth)
print("Final Answer:", result)
ut.desenhar_subgrafo(result, graph, titulo="Visualização do Melhor Indivíduo")
ut.desenhar_subgrafo_colorido(result, graph, resposta_correta, titulo="Visualização do Melhor Indivíduo com Feedback")