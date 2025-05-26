# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga
import matplotlib.pyplot as plt

def datos_generacion(bestFitnessHist, avgFitnessHist, ga):
    fitness_po = [i.fitness for i in ga.current_generation]
    average = sum(fitness_po)/len(fitness_po)
    print("Fitness promedio:{} ".format(average))
    print("Mejor Individuo: {}".format(ga.best_individual()))
    bestFitnessHist.append(ga.best_individual()[0])
    avgFitnessHist.append(average)
    
    return (bestFitnessHist,avgFitnessHist)

def graficos(ga):
     
    bestFitnessHist=[]
    avgFitnessHist=[]

    for i in range(1, 101):
        print("Generacion #{}".format(i))
        ga.create_next_generation()
        info=datos_generacion(bestFitnessHist, avgFitnessHist, ga)
        bestFitnessHist=info[0]
        avgFitnessHist=info[1]
        
        
    generations = list(range(len(avgFitnessHist)))
    
    matriz_rta=  ga.best_individual()[1]
    texto=''
    for elem in matriz_rta[0]:
        if elem!=0:
            texto+=SUBCADENAS[elem-1][matriz_rta[1][elem-1]:matriz_rta[2][elem-1]+1]
    print('matriz solucion', ga.best_individual()[0])
    print('fitness:',ga.best_individual()[1])
    print(texto)

    plt.figure(figsize=(12, 5))

    # Promedio
    plt.subplot(1, 2, 1)
    plt.plot(generations, avgFitnessHist, label='Average Fitness', color='blue')
    plt.xlabel("Generación")
    plt.ylabel("Fitness Promedio")
    plt.title(f"Fitness Promedio por Generación")
    plt.grid(True)

    # Mejor fitness
    plt.subplot(1, 2, 2)
    plt.plot(generations, bestFitnessHist, label='Best Fitness', color='green')
    plt.xlabel("Generación")
    plt.ylabel("Fitness del Mejor Individuo")
    plt.title(f"Mejor Fitness por Generación")
    plt.grid(True)

    plt.tight_layout()
    plt.show()
    
    
def texto_minimo_reconstruible(n: int, k: int, subcadenas: list):
    matrix = [[i for i in range(1,n+1)],[0 for i in range(n)],[(k-1) for i in range(n)]]
    ga = pyeasyga.GeneticAlgorithm(matrix,
                                   population_size=100,
                                   generations=2000,
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
    
    graficos(ga)

    best_fitness = ga.best_individual()[0]
    text = ga.best_individual()[1]
    return text, best_fitness

def create_individual(data):
    genes = [
        data[0][:],  
        data[1][:], 
        data[2][:]  
    ]

    numero_subs = random.randint(0, NUMERO)
    random.shuffle(genes[0])

    for i in range(NUMERO):
        if i >= (NUMERO - numero_subs):
            inicio = random.randint(0, LONGITUD-1)
            fin = random.randint(inicio, LONGITUD-1)
            genes[1][i] = inicio
            genes[2][i] = fin
        else:
            genes[0][i] = 0 
    return genes

def crossover(parent_1, parent_2):
    cut = random.randint(1, NUMERO - 1)
    child1 =[ parent_1[0][:cut] + parent_2[0][cut:],
              parent_1[1][:cut] + parent_2[1][cut:],
              parent_1[2][:cut] + parent_2[2][cut:] ]
    child2 =[ parent_2[0][:cut] + parent_1[0][cut:],
              parent_2[1][:cut] + parent_1[1][cut:],
              parent_2[2][:cut] + parent_1[2][cut:]]
    return child1, child2

def mutate(individual):
    mutation_type = random.choice(["swap", "extreme_edit", "delete_substring"])

    if mutation_type == "swap":
        idx1, idx2 = random.sample(range(0,NUMERO), 2)
        individual[0][idx1], individual[0][idx2] = individual[0][idx2], individual[0][idx1]
        individual[1][idx1], individual[1][idx2] = individual[1][idx2], individual[1][idx1]
        individual[2][idx1], individual[2][idx2] = individual[2][idx2], individual[2][idx1]
    elif mutation_type == "extreme_edit":
        idx = random.randint(0, NUMERO-1)
        action = random.choice(["cambiar_inicio", "cambiar_fin"])
        if action == "cambiar_inicio":
            individual[1][idx] = random.randint(0,individual[2][idx])
        else:
            individual[2][idx] = random.randint(individual[1][idx],LONGITUD-1)
    else:
        idx = random.randint(0, NUMERO-1)
        individual[0][idx] = 0




def fitness(individual, data):
    missed = 0
    repetidos = 0
    adicional = 0
    adicionales=[]
    cuentas = {}
    cadena_reconstruida = ''
    for i in range(NUMERO):
        if individual[0][i] != 0:
            inicio=individual[1][i]
            fin=individual[2][i]
            subcadena=SUBCADENAS[individual[0][i] - 1]
            subcadena=subcadena[inicio:fin+1]
            cadena_reconstruida+=subcadena

    for i in SUBCADENAS:
        cuentas[i]=0
        for j in range(0,len(cadena_reconstruida) - LONGITUD + 1):
            sujeto=cadena_reconstruida[j:j+LONGITUD]
            if sujeto == i:
                cuentas[i]+=1

    for j in range(0,len(cadena_reconstruida) - LONGITUD + 1):
            sujeto=cadena_reconstruida[j:j+LONGITUD]
            if sujeto not in SUBCADENAS:
                    adicionales.append(sujeto)
                    adicional+=1
    
    for elem in cuentas:
        if cuentas[elem] == 0:
            missed+=1
        if cuentas[elem] > 1:
            repetidos+=1

    maximo_cadenas_teoricas_adicionales = len(cadena_reconstruida)-(LONGITUD-1)-NUMERO
    exceso = adicional - maximo_cadenas_teoricas_adicionales
    global minima_longitud
    print('Cuentas:',cuentas)
    print('Adicional: ',adicional)
    print('Adicionales: ',adicionales)
    print('Exceso:',exceso)
    print('Cadena:',cadena_reconstruida)
    print('Individuo:', individual)
    
    if missed > 0:
        return missed + 300
    elif repetidos > 0:
        return repetidos + 50
    
    global minima_longitud_set
    minima_longitud_set.add(minima_longitud)
    if len(cadena_reconstruida) <= minima_longitud:
        minima_longitud = len(cadena_reconstruida)
        minima_longitud_set.add(minima_longitud)
        print('minima:',minima_longitud)
    #elif exceso > 0:
        #return adicional
    return len(cadena_reconstruida)-minima_longitud # Premia la cadena perfecta más corta
   

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
#texto = 
SUBCADENAS = ['nfid','conf','cial','denc','onfi','enci'
]

NUMERO = 6
LONGITUD = 4
minima_longitud = 24
minima_longitud_set = set()
minima_longitud_set.add(24)
rta = texto_minimo_reconstruible(NUMERO, LONGITUD, SUBCADENAS)
texto=''
individual=rta[0]
for i in range(NUMERO):
    if individual[0][i] != 0:
        inicio=individual[1][i]
        fin=individual[2][i]
        subcadena=SUBCADENAS[individual[0][i] - 1]
        subcadena=subcadena[inicio:fin+1]
        texto+=subcadena

print('matriz solucion',rta[0])
print('fitness:',rta[1])
print(texto)
print(minima_longitud_set)