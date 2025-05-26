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
    print('Crossover entre:', parent_1, 'y', parent_2)
    crossover_index = random.randrange(1, NUMERO)
    child_1a = parent_1[:crossover_index]
    child_1b = [i for i in parent_2 if i not in child_1a]
    child_1 = child_1a + child_1b

    child_2a = parent_2[crossover_index:]
    child_2b = [i for i in parent_1 if i not in child_2a]
    child_2 = child_2a + child_2b
    print('Hijos generados:', child_1, 'y', child_2)

    return child_1, child_2


def mutate(individual):
    mutate_index1 = random.randrange(len(individual))
    mutate_index2 = random.randrange(len(individual))
    individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1]


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

    for i in range(1, NUMERO+1):
        cuentas[i]=0
    for i in individual:
        cuentas[i]+=1


    for elem in cuentas:
        if cuentas[elem] == 0:
            missed+=1
        if cuentas[elem] > 1:
            repetidos+=cuentas[elem]

    print('Cadena:',cadena_reconstruida)
    print('Individuo:', individual)
    print('Cuentas:', cuentas)
    global minima_longitud_texto
    print('Minimo: ', minima_longitud_texto)

    if missed > 0 or repetidos > 0:
        return missed +repetidos+ 100 + len(cadena_reconstruida)
    elif len(cadena_reconstruida) < minima_longitud_texto:
        minima_longitud_texto = len(cadena_reconstruida)
        print('Nuevo minimo: ', minima_longitud_texto)
    return len(cadena_reconstruida) - minima_longitud_texto
   

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

SUBCADENAS = [
    'much', 'ucho', 'hosa', 'osañ', 'años', 'osde', 'desp', 'espu', 'spué', 'pués',
    'ésfr', 'sfre', 'fren', 'rent', 'ente', 'ntea', 'teal', 'ealp', 'alpe', 'lelo',
    'elot', 'otón', 'tond', 'ondef', 'defu', 'fusi', 'usil', 'sila', 'ilam', 'lami',
    'amie', 'mien', 'ient', 'ntoe', 'toel', 'elco', 'lcor', 'coro', 'oron', 'rone',
    'onel', 'nela', 'elau', 'aure', 'urel', 'elia', 'lian', 'iano', 'anob', 'nobu',
    'buend', 'endí', 'ndía', 'díah', 'íaha', 'habí', 'abía', 'biad', 'iade', 'ader',
    'dere', 'ecor', 'cord', 'orda', 'rdar', 'dara', 'raqu', 'aque', 'uell', 'ella',
    'llat', 'tard', 'arde', 'derem', 'remo', 'mota', 'taen', 'aenq', 'enqu', 'nque',
    'ques', 'esup', 'supa', 'upad', 'padre', 'drel', 'relo', 'elol', 'loll', 'lleva',
    'evóa', 'voac', 'oaco', 'cono', 'onoc', 'noce', 'ocer', 'cerel', 'erel', 'elhi',
    'hiel','ielo'
]


''''SUBCADENAS = ['nfid','conf','cial','denc','onfi','enci']'''

NUMERO = 102
LONGITUD = 4

minima_longitud_texto=NUMERO*LONGITUD
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