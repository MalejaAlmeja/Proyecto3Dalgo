# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

def texto_minimo_reconstruible(n: int, k: int, subcadenas: list):
    ga = pyeasyga.GeneticAlgorithm(subcadenas,
                                   population_size=50,
                                   generations=100,
                                   crossover_probability=0.8,
                                   mutation_probability=0.2,
                                   elitism=True,
                                   maximise_fitness=False)

    ga.create_individual = create_individual
    ga.crossover_function = crossover
    ga.mutate_function = mutate
    ga.selection_function = roulette_selection  
    ga.fitness_function = fitness  # pendiente 

    ga.run()

    best_fitness = ga.best_individual()[0]
    text = ga.best_individual()[1]
    return text, best_fitness

def create_individual(data):
    individuo = list(data)
    random.shuffle(individuo)
    return individuo

def crossover(parent_1, parent_2):
    size = len(parent_1)
    cut = random.randint(1, size - 1)
    child1 = parent_1[:cut] + parent_2[cut:]
    child2 = parent_2[:cut] + parent_1[cut:]
    return child1, child2

def mutate(individual):
    mutation_type = random.choice(["swap", "extreme_edit"])

    if mutation_type == "swap":
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    else:
        idx = random.randint(0, len(individual) - 1)
        subcadena = individual[idx]
        if len(subcadena) > 1:
            action = random.choice(["remove_start", "remove_end"])
            if action == "remove_start":
                individual[idx] = subcadena[1:]
            else:
                individual[idx] = subcadena[:-1]

def fitness(individual, data):
    return random.randint(1, 100)

def roulette_selection(population):
    max_fitness = max(individual.fitness for individual in population)
    adjusted_fitnesses = [(max_fitness - individual.fitness + 1) for individual in population]
    total_fitness = sum(adjusted_fitnesses)

    pick = random.uniform(0, total_fitness)
    current = 0

    for individual, adjusted in zip(population, adjusted_fitnesses):
        current += adjusted
        if current >= pick:
            return individual

def main():
    linea = sys.stdin.readline().strip()
    ncasos = int(linea)
    for _ in range(ncasos):
        subcadenas = []
        linea = sys.stdin.readline().strip()
        n, k = map(int, linea.split())
        for _ in range(n):
            subcadena = sys.stdin.readline().strip()
            subcadenas.append(subcadena)
        rta = texto_minimo_reconstruible(int(n), int(k), subcadenas)
        print(rta[0])

if __name__ == "__main__":
    main()
