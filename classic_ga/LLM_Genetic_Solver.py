import random
import matplotlib.pyplot as plt

class GeneticSolver:
    def __init__(self, graph, operation, target_node, generations=1000, population_size=100, mutation_rate=0.1, depth=None):
        self.graph = graph
        self.operation = operation
        self.target_node = target_node
        self.generations = generations
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.depth = depth
        self.nodes = list(graph.keys())
        self.historico_fitness_medio = []

    # ================= BFS =====================
    def bfs(self, start_node, max_depth):
        visited = set()
        queue = [(start_node, 0)]
        result = set([start_node])

        while queue:
            node, depth = queue.pop(0)
            if depth < max_depth:
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        result.add(neighbor)
                        queue.append((neighbor, depth + 1))
        return list(result)

    def fitness_bfs(self, individual):
        expected = set(self.bfs(self.target_node, self.depth))
        return len(set(individual).intersection(expected))

    def generate_individual_bfs(self):
        length = random.randint(2, min(len(self.nodes), 10))
        return random.sample(self.nodes, length)

    # ================= PARENTS =====================
    def parents(self, node):
        return [n for n, vizinhos in self.graph.items() if node in vizinhos]

    def fitness_parents(self, individual):
        expected = set(self.parents(self.target_node))
        return len(set(individual).intersection(expected))

    def generate_individual_parents(self):
        length = random.randint(1, min(len(self.nodes), 5))
        return random.sample(self.nodes, length)

    # ================= OPERADORES GENÉTICOS =====================
    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            if random.random() < 0.5 and len(individual) > 1:
                individual.pop(random.randrange(len(individual)))
            else:
                new_gene = random.choice(self.nodes)
                if new_gene not in individual:
                    individual.append(new_gene)
        return individual

    def crossover(self, parent1, parent2):
        pivot = len(parent1) // 2
        child = parent1[:pivot] + [g for g in parent2 if g not in parent1]
        return child

    # ================= EVOLUÇÃO =====================
    def evolve(self):
        if self.operation == "bfs":
            return self._evolve_generic(
                self.generate_individual_bfs,
                self.fitness_bfs,
                target_fitness=len(self.bfs(self.target_node, self.depth))
            )
        elif self.operation == "parents":
            return self._evolve_generic(
                self.generate_individual_parents,
                self.fitness_parents,
                target_fitness=len(self.parents(self.target_node))
            )
        else:
            raise NotImplementedError("Operação não suportada: use 'bfs' ou 'parents'.")

    def _evolve_generic(self, generate_fn, fitness_fn, target_fitness):
        self.historico_fitness_medio = []  # zera a cada execução
        population = [generate_fn() for _ in range(self.population_size)]

        for _ in range(self.generations):
            
            population = sorted(population, key=fitness_fn, reverse=True)
            
            # Salva a média do fitness da população atual
            media = sum(fitness_fn(ind) for ind in population) / len(population)
            self.historico_fitness_medio.append(media)

            if fitness_fn(population[0]) == target_fitness:
                break

            next_gen = population[:5]  # elitismo
            while len(next_gen) < self.population_size:
                p1, p2 = random.sample(population[:20], 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                next_gen.append(child)
            population = next_gen


        plt.plot(range(1, self.generations + 1), self.historico_fitness_medio)
        plt.xlabel("Geração")
        plt.ylabel("F1 médio")
        plt.title("Progresso Evolutivo")
        plt.grid(True)
        plt.show()


        return population[0]


        
