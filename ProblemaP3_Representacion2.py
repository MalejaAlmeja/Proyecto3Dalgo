# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

def texto_minimo_reconstruible(n: int, k: int, subcadenas: list):
    vector = [i for i in range(0,(n*k)+1)]
    ga = pyeasyga.GeneticAlgorithm(vector,
                                   population_size=100,
                                   generations=1000,
                                   crossover_probability=0.8,
                                   mutation_probability=0.2,
                                   elitism=True,
                                   maximise_fitness=False)

    ga.create_individual = create_individual
    ga.crossover_function = crossover
    ga.mutate_function = mutate
    ga.selection_function = roulette_selection  
    ga.fitness_function = fitness 
    ga.run()

    best_fitness = ga.best_individual()[0]
    text = ga.best_individual()[1]
    return text, best_fitness

def create_individual(data):
    genes = data[:] 
    cte=(NUMERO*LONGITUD)
    numero_letras = random.randint(1,cte)
    numero_ceros = cte - numero_letras
    genes[0] = numero_ceros - 1

    for i in range(1,cte+1):
        if i <= numero_letras:
            letra_aleatoria=random.choice(LETRAS)
            genes[i] = letra_aleatoria
        else:
            genes[i] = 0

    return genes

def crossover(parent_1, parent_2):
    cte=(NUMERO*LONGITUD)
    #Implementación 1: Los ceros tienen que ser consecutivos
    '''
    cut1 = random.randint(1, parent_1[0])
    cut2 = random.randint(1, parent_2[0])
    if cut1>=cut2:
        child1 = parent_1[1:cut2] + parent_2[cut2:]
        child2 = parent_2[1:cut2] + parent_1[cut2:]
    else:
        child1 = parent_1[1:cut1] + parent_2[cut1:]
        child2 = parent_2[1:cut1] + parent_1[cut1:]
    '''
    #Implementación 2: Los ceros no son consecutivos
    cut = random.randint(1,cte)
    print('papa: ',parent_1)
    print('papa: ',parent_2)
    child1 = [0] + parent_1[1:cut] + parent_2[cut:]
    child2 = [0] + parent_2[1:cut] + parent_1[cut:]
    print('hijo1: ',child1)
    print('hijo2: ',child2)
    ceros_child1 = 0
    ceros_child2 = 0

    for letra in child1:
        if letra == 0:
            ceros_child1 += 1

    for letra in child2:
        if letra == 0:
            ceros_child2 += 1
    child1[0]= ceros_child1
    child2[0]= ceros_child2
    
    return child1, child2

def mutate(individual):
    tipo_mutacion = random.choice(["cambio_letra", "eliminar_letra","anadir_letra"])
    idx = random.randint(1,NUMERO*LONGITUD)
    print(individual)
    print(idx)
    if individual[idx] == 0:
        letra_aleatoria = random.choice(LETRAS)
        individual[0]-=1
        individual[idx] = letra_aleatoria
    else:
        tipo_mutacion = random.choice(["cambio_letra", "eliminar_letra"])
        if tipo_mutacion == "cambio_letra":
            letra_aleatoria = random.choice(LETRAS)
            individual[idx] = letra_aleatoria
        else:
            individual[0]+=1
            individual[idx] = 0



def fitness(individual, data):
    missed = 0
    repetidos = 0
    adicional = 0
    adicionales=[]
    cuentas = {}
    cadena_reconstruida = ''
    #Se genera la subcadena a partir de las letras que estén en la solución
    for i in range(1,NUMERO):
        if individual[i] != 0:
            cadena_reconstruida+=individual[i]

    #Se verifica cuántas veces se repiten las cadenas de entrada
    for i in SUBCADENAS:
        cuentas[i]=0
        for j in range(0,len(cadena_reconstruida) - LONGITUD + 1):
            sujeto=cadena_reconstruida[j:j+LONGITUD]
            if sujeto == i:
                cuentas[i]+=1
    #Se verifica cuántas subcadenas de tamaño k hay en la solución que no estén dentro del arreglo de subcadenas
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

    print('Cuentas:',cuentas)
    print('Adicional: ',adicional)
    print('Adicionales: ',adicionales)
    print('Exceso:',exceso)
    print('Cadena:',cadena_reconstruida)
    print('Individuo:', individual)

    if missed > 0:
        return missed + 200
    elif repetidos > 0:
        return repetidos + 50
    #comento lo de adicionales porque no estoy segura
    #elif adicional > 0:
        #return adicional
    else:
        return len(cadena_reconstruida)  # Premia la cadena perfecta más corta
   

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

SUBCADENAS = ['nfid','conf','cial','denc','onfi','enci']
NUMERO = 6
LONGITUD = 4
letras = set()
for sub in SUBCADENAS:
    for letra in sub:
        letras.add(letra)
LETRAS = list(letras)

rta = texto_minimo_reconstruible(NUMERO, LONGITUD, SUBCADENAS)
individual= rta[0]
texto=''
for i in range(1,NUMERO*LONGITUD):
        if individual[i] != 0:
            texto+=individual[i]

print('matriz solucion',rta[0])
print('fitness:',rta[1])
print(texto)