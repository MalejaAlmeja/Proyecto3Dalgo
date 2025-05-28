# Integrantes:
# Daniela González: 202320856
# Sofía Arias: 202310260
# María Alejandra Carrillo: 202321854

import sys
import random
from pyeasyga import pyeasyga

#constantes globales
TAMANO = 102
LONG = 4
longitud_minima = TAMANO * LONG

# Subcadenas
FRAGMENTOS = [
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

# control greedy
generados_greedy = 0
MAXIMO_GREEDY = 25

def reconstruccion_optima(n: int, k: int, bloques: list):
    valores = list(range(1, n + 1))
    algoritmo = pyeasyga.GeneticAlgorithm(valores,
                                          population_size=50,
                                          generations=150,
                                          crossover_probability=0.8,
                                          mutation_probability=0.2,
                                          elitism=True,
                                          maximise_fitness=False)

    algoritmo.create_individual = nuevo_individuo
    algoritmo.crossover_function = cruzamiento
    algoritmo.mutate_function = mutacion
    algoritmo.selection_function = seleccion_ruleta
    algoritmo.fitness_function = evaluar
    algoritmo.run()

    aptitud, mejor = algoritmo.best_individual()
    return mejor, aptitud

def nuevo_individuo(data):
    global generados_greedy
    if generados_greedy < MAXIMO_GREEDY:
        generados_greedy += 1
        return generar_greedy()
    cromosoma = data[:]
    random.shuffle(cromosoma)
    return cromosoma

def cruzamiento(padre1, padre2):
    punto = random.randint(1, TAMANO - 1)
    mitad1 = padre1[:punto]
    hijo1 = mitad1 + [x for x in padre2 if x not in mitad1]

    mitad2 = padre2[punto:]
    hijo2 = [x for x in padre1 if x not in mitad2] + mitad2

    return hijo1, hijo2

def mutacion(cromosoma):
    i, j = random.sample(range(len(cromosoma)), 2)
    cromosoma[i], cromosoma[j] = cromosoma[j], cromosoma[i]

def evaluar(cromosoma, _):
    global longitud_minima
    reconstruida = FRAGMENTOS[cromosoma[0] - 1]
    contador = {}

    if len(cromosoma)==101:
        print("STOP")
            
    for idx in range(1, TAMANO):
        actual = FRAGMENTOS[cromosoma[idx] - 1]
        anterior = reconstruida[-LONG:]
        solape = 0
        for i in range(LONG, 0, -1):
            if anterior[-i:] == actual[:i]:
                solape = i
                break
        reconstruida += actual[solape:]

    if len(reconstruida) < longitud_minima:
        longitud_minima = len(reconstruida)

    return len(reconstruida) - longitud_minima

def seleccion_ruleta(poblacion):
    total = sum(1 / (ind.fitness + 1e-7) for ind in poblacion)
    umbral = random.random()
    acumulado = 0
    for ind in poblacion:
        prob = (1 / (ind.fitness + 1e-7)) / total
        acumulado += prob
        if umbral <= acumulado:
            return ind

def generar_greedy():
    added={}
    first=random.randint(0, TAMANO-1)
    added[first]=0
    secuencia=[first+1]

    while len(secuencia)<TAMANO: 
        ultimo = FRAGMENTOS[secuencia[-1] - 1]
        maxOverlap=-1
        maxIdx=-1
        
        for i in range(0, TAMANO-1):
            if i not in added:
                overlap=calcular_solape(ultimo, FRAGMENTOS[i])
                if maxOverlap<overlap:
                    maxOverlap=overlap
                    maxIdx=i
                       
        secuencia.append(maxIdx+1)
        added[maxIdx]=0
        
    return secuencia

def calcular_solape(a, b):
    for i in range(LONG, 0, -1):
        if a[-i:] == b[:i]:
            return i
    return 0

'''
linea = sys.stdin.readline().strip()
ncasos = int(linea)
for _ in range(ncasos):
    subcadenas = []
    dicc_subcadenas={}
    linea = sys.stdin.readline().strip()
    n, k = map(int, linea.split())
    for _ in range(n):
        subcadena = sys.stdin.readline().strip()
        if subcadena not in dicc_subcademnas:
            subcadenas.append(subcadena)
            dicc_subcadenas[subcadena]=0
            
    SUBCADENAS = subcadenas
    NUMERO = len(subcadenas)
    LONGITUD = k
    rta = texto_minimo_reconstruible(int(n), int(k), subcadenas)
    print(rta[0])
'''
# 
respuesta = reconstruccion_optima(TAMANO, LONG, FRAGMENTOS)
orden_final = respuesta[0]
texto = FRAGMENTOS[orden_final[0] - 1]

for idx in range(1, TAMANO):
    anterior = texto[-LONG:]
    actual = FRAGMENTOS[orden_final[idx] - 1]
    anadir = actual
    for i in range(LONG, 0, -1):
        if anterior[-i:] == actual[:i]:
            anadir = actual[i:]
            break
    texto += anadir

print("Orden Final:", orden_final)
print("Fitness Final:", respuesta[1])
print("Texto Reconstruido:", texto)
print("Longitud Total:", len(texto))
