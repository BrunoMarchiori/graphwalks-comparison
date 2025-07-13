
import classic_ga.genetic_solver as gs
import utils as ut
from datasets import load_dataset, Dataset, DatasetDict


ds = load_dataset("openai/graphwalks")

instancia = ds['train'][501]['prompt']
gabarito = ut.extrair_gabarito(ds['train'][501]['answer_nodes'])
arestas, alvo, operacao, profundidade = ut.extrair_prompt(instancia)



graph = ut.construir_grafo(arestas)
ut.visualizar_grafo_completo(graph)

if (operacao == 0):
    
    solver = gs.GeneticSolver(
        graph=graph,
        operation="parents",
        target_node=alvo,
        generations=1000,
    )

else:
    
    solver = gs.GeneticSolver(
    graph=graph,
    operation="bfs",
    target_node= alvo,
    depth=profundidade,
    generations=1000
)


result = solver.evolve()
print("Final Answer:", result)

'''
if (operacao ==0): 
    #resposta_correta = solver.parents(solver.target_node)
    
else: 
    #resposta_correta = solver.bfs(solver.target_node, solver.depth)
'''


print("Melhor Indivíduo:", result)
print("Resposta Correta:", gabarito)

ut.desenhar_subgrafo(result, graph, titulo="Melhor Indivíduo")
ut.desenhar_subgrafo_colorido(result, graph, gabarito, titulo="Com Feedback (Parents)")


'''




------------------------------------------------------------------------------------------------------------------------------------------


import utils as ut
import classic_ga.LLM_Genetic_Solver as gs2
import utils as ut
from datasets import load_dataset, Dataset, DatasetDict

ds = load_dataset("openai/graphwalks")

instancia = ds['train'][502]['prompt']
gabarito = ut.extrair_gabarito(ds['train'][502]['answer_nodes'])

arestas, alvo, operacao, profundidade = ut.extrair_prompt(instancia)



graph = ut.construir_grafo(arestas)
ut.visualizar_grafo_completo(graph)


if (operacao == 0):
    
    solver = gs2.GeneticSolver(
        graph=graph,
        operation="parents",
        target_node=alvo,
        generations=1000,
    )

else:
    
    solver = gs2.GeneticSolver(
    graph=graph,
    operation="bfs",
    target_node= alvo,
    depth=profundidade,
    generations=1000
)


result = solver.evolve()
print("Final Answer:", result)


if (operacao ==0): 
    resposta_correta = solver.parents(solver.target_node)
    

else: 
    resposta_correta = solver.bfs(solver.target_node, solver.depth)
    

    
print("Melhor Indivíduo:", result)
print("Resposta Correta:", gabarito)

ut.desenhar_subgrafo(result, graph, titulo="Melhor Indivíduo")
ut.desenhar_subgrafo_colorido(result, graph, gabarito, titulo="Com Feedback (Parents)")
'''