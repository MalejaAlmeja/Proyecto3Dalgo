import random
from ProblemaP3 import create_individual, crossover, mutate, roulette_selection

def test_genetic_operations():
    # Test data
    test_data = ["ABC", "DEF", "GHI", "JKL"]
    
    # Test create_individual
    print("\nProbando create_individual:")
    individual = create_individual(test_data)
    print(f"Individuo creado: {individual}")
    
    # Test crossover
    print("\nProbando crossover:")
    parent1 = test_data.copy()
    parent2 = test_data.copy()
    random.shuffle(parent1)
    random.shuffle(parent2)
    print(f"Padre 1: {parent1}")
    print(f"Padre 2: {parent2}")
    child1, child2 = crossover(parent1, parent2)
    print(f"Hijo 1: {child1}")
    print(f"Hijo 2: {child2}")
    
    # Test mutation
    print("\nProbando mutation:")
    test_individual = test_data.copy()
    print(f"Antes de la mutación: {test_individual}")
    mutate(test_individual)
    print(f"Después de la mutación: {test_individual}")
    
    # Test roulette selection
    print("\nProbando roulette selection:")
    class MockIndividual:
        def __init__(self, fitness):
            self.fitness = fitness
    
    test_population = [MockIndividual(random.randint(1, 100)) for _ in range(5)]
    print("Fitness de la población:", [ind.fitness for ind in test_population])
    selected = roulette_selection(test_population)
    print(f"Fitness del individuo seleccionado: {selected.fitness}")

if __name__ == "__main__":
    test_genetic_operations() 