import classic_ga.genetic_solver as gs

graph = {
    "abcd": ["uvwx", "efgh"],
    "efgh": ["uvwx"],
    "uvwx": ["alke"]
}

solver = gs.GeneticSolver(graph, operation="bfs", target_node="abcd", depth=1)
result = solver.evolve()
print("Final Answer:", result)

import classic_ga.genetic_solver as gs

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


solver = gs.GeneticSolver(
    graph=graph,
    operation="parents",
    target_node="8f14e45fce",
    generations=200
)

result = solver.evolve()
print("Final Answer:", result)