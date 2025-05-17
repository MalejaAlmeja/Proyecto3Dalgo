#Integrantes:
#Daniela González: 202320856
#Sofía Arias: 202310260
#María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

def texto_minimo_reconstruible(n:int, k:int, subcadenas:list):
    ga = pyeasyga.GeneticAlgorithm(representation(n,k),
                            population_size=50,
                            generations=100,
                            crossover_probability=0.8,
                            mutation_probability=0.2,
                            elitism=True,
                            maximise_fitness=False)
    
    ga.create_individual = create_individual
    ga.crossover_function = crossover
    ga.mutate_function = mutate
    ga.selection_function = selection
    ga.fitness_function = fitness
    
    ga.run()
    
    best_fitness=ga.best_individual()[0]
    text=ga.best_individual()[1]
    return text, best_fitness

def representation(n,k):
    matrix = [[1 for i in range(n)],
              [0 for i in range(n)],
              [k-1 for i in range(n)]]
    return matrix

def create_individual(data):
    print('')

def crossover(parent_1, parent_2):
    child1=""
    child2=""
    return child1, child2

def mutate(individual):
    print('')
    
def selection(population):
    roulette = []
    return roulette
        
def fitness (individual, data):
    number=0
    return number


def main():
    linea = sys.stdin.readline().strip()
    ncasos = int(linea)
    for i in range(ncasos):
        subcadenas = []
        linea = sys.stdin.readline().strip()
        n,k= linea.split(" ")
        for j in range(int(n)):
            linea = sys.stdin.readline()
            subcadenas.append(linea)
        rta = texto_minimo_reconstruible(int(n),int(k),subcadenas)
        print(rta)

main()