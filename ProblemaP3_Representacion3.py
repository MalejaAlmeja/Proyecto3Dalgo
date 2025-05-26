# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

def texto_minimo_reconstruible(n: int, k: int, subcadenas: list):
    vector = [i for i in range(1,n+1)]
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
    random.shuffle(genes)

    return genes

def crossover(parent_1, parent_2):
    cut = random.randint(1,NUMERO)
    child1 = parent_1[:cut] + parent_2[cut:]
    child2 = parent_2[:cut] + parent_1[cut:]
    
    return child1, child2

def mutate(individual):
    idx = random.randint(0,NUMERO-1)
    subcadena_aleatoria = random.randint(1,NUMERO)
    individual[idx] = subcadena_aleatoria


def fitness(individual, data):
    missed = 0
    repetidos = 0
    adicional = 0
    adicionales=[]
    cuentas = {}
    cadena_reconstruida = ''
    #Se genera la subcadena en el orden que corresponde; se verifican las intersecciones
    for i in range(NUMERO):
        if i == 0:
            cadena_reconstruida += SUBCADENAS[individual[0]-1]
        else:
            ultima_k_subcadena = cadena_reconstruida[-LONGITUD:]
            actual = SUBCADENAS[individual[i]-1]
            letras_adicionales = actual
            for j in range(LONGITUD,0,-1):
                if ultima_k_subcadena[-j:] == actual[:j]:
                    letras_adicionales = actual[j:]
                    break

            cadena_reconstruida+=letras_adicionales

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

for i in range(NUMERO):
        if i == 0:
            texto += SUBCADENAS[individual[0]-1]
        else:
            ultima_k_subcadena = texto[-LONGITUD:]
            actual = SUBCADENAS[individual[i]-1]
            letras_adicionales = actual
            for j in range(LONGITUD,0,-1):
                if ultima_k_subcadena[-j:] == actual[:j]:
                    letras_adicionales = actual[j:]
                    break

            texto+=letras_adicionales

print('matriz solucion',rta[0])
print('fitness:',rta[1])
print(texto)