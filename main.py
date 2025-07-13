
import classic_ga.genetic_solver as gs
import classic_ga.LLM_Genetic_Solver as gs2
import utils as ut
from datasets import load_dataset, Dataset, DatasetDict


ds = load_dataset("openai/graphwalks")

instancia = ds['train'][26]['prompt']
gabarito = ut.extrair_gabarito(ds['train'][26]['answer_nodes'])
arestas, alvo, operacao, profundidade = ut.extrair_prompt(instancia)



graph = ut.construir_grafo(arestas)
ut.visualizar_grafo_completo(graph)

if (operacao == 0):
    
    solver1 = gs.GeneticSolver(
        graph=graph,
        operation="parents",
        target_node=alvo,
        generations=1000,
    )

    solver2 = gs2.GeneticSolver(
        graph=graph,
        operation="parents",
        target_node=alvo,
        generations=1000,
    )

else:
    
    solver1 = gs.GeneticSolver(
    graph=graph,
    operation="bfs",
    target_node= alvo,
    depth=profundidade,
    generations=1000
    )


    solver2 = gs2.GeneticSolver(
    graph=graph,
    operation="bfs",
    target_node= alvo,
    depth=profundidade,
    generations=1000
)


result1 = solver1.evolve()
result2 = solver2.evolve()
print("Final Answer:", result1)
print("Final Answer2:", result2)



print("Resposta Correta:", gabarito)


ut.desenhar_subgrafo(result1, graph, titulo="Melhor Indivíduo")
ut.desenhar_subgrafo(result2, graph, titulo="Melhor Indivíduo")
ut.desenhar_subgrafo_colorido(result1, graph, gabarito, titulo="Com Feedback (Parents)")
ut.desenhar_subgrafo_colorido(result2, graph, gabarito, titulo="Com Feedback (Parents)")

