# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

def texto_minimo_reconstruible(n: int, k: int, subcadenas: list):
    matrix = [[i for i in range(1,n+1)],[0 for i in range(n)],[k-1 for i in range(n)]]
    ga = pyeasyga.GeneticAlgorithm(matrix,
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
    numero_subs = random.randint(1,NUMERO)
    random.shuffle(data[0])
    for i in range(NUMERO):
        if i >= NUMERO-numero_subs: #No va a estar en el rango de aquellos que no serán tomados en cuenta
            inicio = random.randint(0,LONGITUD)
            fin = random.randint(inicio,LONGITUD)
            data[1][i]=inicio
            data[2][i]=fin
        else:
            data[0][i]=0
    return data

def crossover(parent_1, parent_2):
    cut = random.randint(1, NUMERO - 1)
    child1 =[ [ parent_1[0][:cut] + parent_2[0][cut:] ],
              [ parent_1[1][:cut] + parent_2[1][cut:] ],
              [ parent_1[2][:cut] + parent_2[2][cut:] ] ]
    child2 =[ [ parent_2[0][:cut] + parent_1[0][cut:] ],
              [ parent_2[1][:cut] + parent_1[1][cut:] ],
              [ parent_2[2][:cut] + parent_1[2][cut:] ] ]
    return child1, child2

def mutate(individual):
    mutation_type = random.choice(["swap", "extreme_edit"])

    if mutation_type == "swap":
        idx1, idx2 = random.sample(range(NUMERO), 2)
        print(idx1, idx2)
        print(len(individual[0]),len(individual[1]),len(individual[2]))
        #mirar que pasa por qué se están camibando los tamaños de las listas!
        individual[0][idx1], individual[0][idx2] = individual[0][idx2], individual[0][idx1]
        individual[1][idx1], individual[1][idx2] = individual[1][idx2], individual[1][idx1]
        individual[2][idx1], individual[2][idx2] = individual[2][idx2], individual[2][idx1]
    else:
        idx = random.randint(0, NUMERO-1)
        print(idx)
        print(len(individual[0]),len(individual[1]),len(individual[2]))
        action = random.choice(["cambiar_inicio", "cambiar_fin"])
        if action == "cambiar_inicio":
            individual[1][idx] = random.randint(0,individual[2][idx])
        else:
            individual[2][idx] = random.randint(individual[1][idx],LONGITUD)

def fitness(individual, data):
    for i in range(NUMERO):
        missed = 0
        cadena_reconstruida = ''
        if individual[0][i] != 0:
            inicio=individual[1][i]
            fin=individual[2][i]
            cadena_reconstruida+=SUBCADENAS[individual[i]-1][inicio:fin+1]
    for i in SUBCADENAS:
        if i not in cadena_reconstruida:
            missed+=1

    return missed

def roulette_selection(population):
    fitness_reciproco =[]
    probabilidades = []
    suma=0
    for individuo in population:
       fitness_reciproco.append(1 / (individuo.fitness + 0.0000001))
       suma+= (1 / (individuo.fitness + 0.0000001))
    for f in fitness_reciproco:
        probabilidades.append(f/suma)
    r=random.random()
    acumuladas = []
    acumulado = 0
    for p in probabilidades:
        acumulado += p
        acumuladas.append(acumulado)
    for i in range(len(acumuladas)):
        if r <= acumuladas[i]:
            return population[i]

'''
linea = sys.stdin.readline().strip()
ncasos = int(linea)
for _ in range(ncasos):
    subcadenas = []
    linea = sys.stdin.readline().strip()
    n, k = map(int, linea.split())
    for _ in range(n):
        subcadena = sys.stdin.readline().strip()
        subcadenas.append(subcadena)
        SUBCADENAS = subcadenas
        NUMERO = n
        LONGITUD = k
    rta = texto_minimo_reconstruible(int(n), int(k), subcadenas)
    print(rta[0])
'''

SUBCADENAS = ['aab','baa','aaa','bbb']
NUMERO = 4
LONGITUD = 3
rta = texto_minimo_reconstruible(NUMERO, LONGITUD, SUBCADENAS)
print(rta[0])