import random

class GeneticSolver:
    def __init__(self, graph, operation, target_node=None, depth=None,
                 population_size=100, generations=100, mutation_rate=0.3):
        self.graph = graph  # dicionário de adjacência
        self.operation = operation  # 'bfs' ou 'parents'
        self.target_node = target_node
        self.depth = depth
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def initialize_population(self):
        population = []
        available_nodes = list(self.graph.keys())
        if not available_nodes:
            return population

        for _ in range(self.population_size):
            k = random.randint(1, len(available_nodes))
            individual = random.sample(available_nodes, k=k)
            population.append(individual)

        return population

    def fitness(self, individual):
        if self.operation == 'bfs':
            expected = self.bfs(self.target_node, self.depth)
        elif self.operation == 'parents':
            expected = self.parents(self.target_node)
        overlap = set(individual) & set(expected)
        precision = len(overlap) / len(individual) if individual else 0
        recall = len(overlap) / len(expected) if expected else 0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
        return f1

    def bfs(self, start, depth):
        visited = set()
        current = [start]
        for _ in range(depth):
            next_level = []
            for node in current:
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        next_level.append(neighbor)
                        visited.add(neighbor)
            current = next_level
        return current

    def parents(self, node):
        return [src for src, targets in self.graph.items() if node in targets]

    def crossover(self, parent1, parent2):
        min_len = min(len(parent1), len(parent2))
        if min_len <= 1:
            # Não é possível fazer crossover significativo, retorna cópia de um dos pais
            return parent1.copy()
        cut = random.randint(1, min_len - 1)
        child = list(set(parent1[:cut] + parent2[cut:]))
        return child

    def mutate(self, individual):
        if not individual:
            return individual  # ignora indivíduos vazios
        if random.random() < self.mutation_rate:
            all_nodes = list(self.graph.keys())
            idx = random.randint(0, len(individual) - 1)
            individual[idx] = random.choice(all_nodes)
        return individual

    def evolve(self):
        population = self.initialize_population()
        if not population:
            print("Erro: População inicial está vazia.")
            return []

        for _ in range(self.generations):
            scored = [(ind, self.fitness(ind)) for ind in population]
            scored.sort(key=lambda x: x[1], reverse=True)
            population = [ind for ind, _ in scored[:max(2, self.population_size // 2)]]

            new_population = population.copy()
            while len(new_population) < self.population_size:
                if len(population) < 2:
                    break  # sem pais suficientes para cruzar
                p1, p2 = random.sample(population, 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population

        best = max(population, key=self.fitness)
        return best